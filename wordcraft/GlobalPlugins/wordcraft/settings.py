import addonHandler
import gui
from gui.settingsDialogs import SettingsPanel
from logHandler import log

import wx

from .config import Config
from .saver import Saver
from .settings_helper import SettingsMixin
from .types import CorrectType, Languages


addonHandler.initTranslation()


class CrafterSettings(SettingsPanel):
    title = "wordcraft"

    saver: Saver = None
    config: Config = None

    def makeSettings(self, settingsSizer):
        settings_sizer_helper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
        correct_types = [item.value for item in CorrectType]
        helper = SettingsMixin(self.config)

        self.required_languages = helper.get_check_list_box(settings_sizer_helper, _("Required languages:"))
        self.lang_default = helper.get_lang_default_choice(settings_sizer_helper, _("Default language:"))

        self.correct_type = settings_sizer_helper.addLabeledControl(
            _("Default method for auto correct:"),
            wx.Choice,
            choices=correct_types,
        )
        self.correct_type.SetStringSelection(self.config.correct_default.value)

        self.variants_type = settings_sizer_helper.addLabeledControl(
            _("Default method for get variants:"),
            wx.Choice,
            choices=correct_types,
        )
        self.variants_type.SetStringSelection(self.config.variants_default.value)

        self.need_auto_correct = settings_sizer_helper.addItem(wx.CheckBox(self, label=_("Auto correct")))
        self.need_auto_correct.SetValue(self.config.need_auto_correct)

        self.need_copy_to_clipboard = settings_sizer_helper.addItem(wx.CheckBox(self, label=_("Copy to clipboard")))
        self.need_copy_to_clipboard.SetValue(self.config.need_copy_to_clipboard)

    def onSave(self):
        checked_languages_indexes = list(self.required_languages.GetCheckedItems())
        self.config.required_languages = SettingsMixin.get_checked_languages(checked_languages_indexes)

        if checked_languages_indexes:
            selected_lang_default = self.lang_default.GetStringSelection()
            for language in Languages:
                if language.value == selected_lang_default:
                    self.config.lang_default = language
                    break
            else:
                self.config.lang_default = Languages.en
        else:
            self.config.lang_default = Languages.en

        selected_correct_type = self.correct_type.GetStringSelection()
        selected_variants_type = self.variants_type.GetStringSelection()

        for correct_type in CorrectType:
            if correct_type.value == selected_correct_type:
                self.config.correct_default = correct_type
            if correct_type.value == selected_variants_type:
                self.config.variants_default = correct_type

        self.config.need_auto_correct = self.need_auto_correct.IsChecked()
        self.config.need_copy_to_clipboard = self.need_copy_to_clipboard.IsChecked()

        self.saver.save(self.config)
