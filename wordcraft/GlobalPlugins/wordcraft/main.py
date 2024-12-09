import api
import addonHandler
import globalPluginHandler
import gui
import scriptHandler
from languageHandler import getLanguage
import ui

import wx

from .config import Config
from .corrector import Corrector
from .crafter import Crafter
from .gui import CraftGUI, ReplacementsGUI
from .saver import Saver
from .settings import CrafterSettings
from .translations import Translator
from .types import CorrectType, Languages


addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "wordcraft"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.saver = Saver()
        self.config = self.saver.load()
        self.set_default_language()

        CrafterSettings.saver = self.saver
        CrafterSettings.config = self.config
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(CrafterSettings)

        self.corrector = Corrector()
        self.crafter = Crafter(self.config)

    def terminate(self):
        self.crafter.close()
        super().terminate()

    def set_default_language(self):
        if self.config.required_languages:
            return

        user_language = getLanguage()
        if not hasattr(Languages, user_language):
            return

        default_language = getattr(Languages, user_language)
        self.config.required_languages.append(default_language)
        self.config.lang_default = default_language

        self.saver.save(self.config)

    @property
    def not_lang_tool_supports_label(self) -> str:
        return Translator.available_only_for_simple_method

    @property
    def not_autocorrect_supports_label(self) -> str:
        return Translator.available_only_for_extended_method

    def output(self, corrected_text: str):
        status = False
        if self.crafter.text == corrected_text:
            return

        if not self.config.need_auto_correct and not self.config.need_copy_to_clipboard:
            ui.message(Translator.errors_found)
            wx.CallAfter(CraftGUI.create_craft_gui, self.crafter)

        if self.config.need_auto_correct:
            status = self.corrector.set_text(corrected_text)
            if status:
                wx.CallLater(500, ui.message, "\n".join([Translator.corrected_to, corrected_text]))

        if self.config.need_copy_to_clipboard:
            wx.CallLater(500, api.copyToClip, corrected_text, notify=True)

    def process(self, is_shift: bool = False):
        origin_text = self.corrector.get_text()
        if origin_text is None:
            return ui.message(Translator.no_selection)

        if self.config.correct_default == CorrectType.Extended:
            func = self.crafter.correct_simple if is_shift else self.crafter.correct_extended
            if not is_shift and not self.crafter.is_lang_tool_supports:
                ui.message(self.not_lang_tool_supports_label)
                func = self.crafter.correct_simple
            elif is_shift and not self.crafter.is_autocorrect_supports:
                ui.message(self.not_autocorrect_supports_label)
                func = self.crafter.correct_extended

        else:
            func = self.crafter.correct_extended if is_shift else self.crafter.correct_simple
            if is_shift and not self.crafter.is_lang_tool_supports:
                ui.message(self.not_lang_tool_supports_label)
                func = self.crafter.correct_simple
            elif not is_shift and not self.crafter.is_autocorrect_supports:
                ui.message(self.not_autocorrect_supports_label)
                func = self.crafter.correct_extended

        corrected_text = func(origin_text)
        self.output(corrected_text)

    def get_variants(self, is_shift: bool = False):
        origin_text = self.corrector.get_text()
        if origin_text is None:
            return ui.message(Translator.no_selection)
        elif len(origin_text.split(' ')) > 1:
            return ui.message(Translator.replacements_suggested_for_word)

        if self.config.variants_default == CorrectType.Extended:
            func = self.crafter.get_variants_simple if is_shift else self.crafter.get_variants_extended
            if not is_shift and not self.crafter.is_lang_tool_supports:
                ui.message(self.not_lang_tool_supports_label)
                func = self.crafter.get_variants_simple
            elif is_shift and not self.crafter.is_autocorrect_supports:
                ui.message(self.not_autocorrect_supports_label)
                func = self.crafter.get_variants_extended

        else:
            func = self.crafter.get_variants_extended if is_shift else self.crafter.get_variants_simple
            if is_shift and not self.crafter.is_lang_tool_supports:
                ui.message(self.not_lang_tool_supports_label)
                func = self.crafter.get_variants_simple
            elif not is_shift and not self.crafter.is_autocorrect_supports:
                ui.message(self.not_autocorrect_supports_label)
                func = self.crafter.get_variants_simple

        variants = func(origin_text)
        wx.CallAfter(ReplacementsGUI.create_replacements_gui, variants, self.output)

    @scriptHandler.script(
        description=_("Open addon window"),
        gesture="kb:NVDA+CONTROL+="
    )
    def script_open_window(self, gesture):
        if not self.crafter.is_lang_tool_supports:
            return ui.message(self.not_lang_tool_supports_label)

        wx.CallAfter(CraftGUI.create_craft_gui, self.crafter)

    @scriptHandler.script(
        description=_("change language"),
        gesture="kb:NVDA+CONTROL+ALT+="
    )
    def script_change_language(self, gesture):
        lang = self.crafter.next_language()
        ui.message(" ".join([Translator.language_changed_to, lang.value]))

    @scriptHandler.script(
        description=_("Default method auto correct errors"),
        gesture="kb:NVDA+="
    )
    def script_correct_default(self, gesture):
        self.process()

    @scriptHandler.script(
        description=_("Alternative method auto correct errors"),
        gesture="kb:NVDA+SHIFT+="
    )
    def script_correct_alternative(self, gesture):
        self.process(is_shift=True)

    @scriptHandler.script(
        description=_("Default method get variants"),
        gesture="kb:NVDA+ALT+="
    )
    def script_variants_default(self, gesture):
        self.get_variants()

    @scriptHandler.script(
        description=_("Alternative method get variants"),
        gesture="kb:NVDA+SHIFT+ALT+="
    )
    def script_variants_alternative(self, gesture):
        self.get_variants(is_shift=True)
