import api
import addonHandler
import gui
import ui

import wx

from .replacements import ReplacementsGUI

from ..crafter import Crafter


addonHandler.initTranslation()


class CraftGUI(wx.Dialog):

    _instance = None

    @staticmethod
    def create_craft_gui(crafter: Crafter):
        if CraftGUI._instance:
            return

        gui.mainFrame.prePopup()
        window = CraftGUI(gui.mainFrame, crafter)

        window.Show()
        gui.mainFrame.postPopup()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            return super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self, parent, crafter: Crafter):
        if self._instance is not None:
            return self._instance

        self.crafter: Crafter = crafter
        self.crafter.init_speller()
        self.crafter.init_lang_tool()

        dialog_title = _("Checking grammar and spelling")
        super().__init__(parent, title=dialog_title, size=(800, 600,))

        self.build_ui()
        self._bindEvents()

    def build_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)

        text_sizer = wx.BoxSizer(wx.HORIZONTAL)
        text_helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
        self.text = text_helper.addLabeledControl(_("Text"), wx.TextCtrl, style=wx.TE_MULTILINE | wx.HSCROLL)
        text_sizer.Add(text_helper.sizer, border=2, flag=wx.EXPAND | wx.ALL)
        main_sizer.Add(text_sizer, border=2, flag=wx.EXPAND | wx.ALL)

        errors_sizer = wx.BoxSizer(wx.VERTICAL)
        errors_helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
        errors_helper.addItem(wx.StaticText(self, wx.ID_ANY, label=_("List errors:")))
        self.errors_control = errors_helper.addItem(wx.ListBox(
            self, wx.ID_ANY, choices=self.errors,
            style=wx.LB_HSCROLL | wx.LB_NEEDED_SB | wx.LB_SINGLE,
        ))
        errors_sizer.Add(errors_helper.sizer, border=2, flag=wx.EXPAND | wx.ALL)
        main_sizer.Add(errors_sizer, border=2, flag=wx.EXPAND | wx.ALL)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_helper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.HORIZONTAL)
        self.check_button = button_helper.addItem(wx.Button(self, wx.ID_ANY, label=_("Check")))
        self.close_button = button_helper.addItem(wx.Button(self, wx.ID_ANY, label=_("Close")))
        button_sizer.Add(button_helper.sizer, border=2, flag=wx.EXPAND | wx.ALL)
        main_sizer.Add(button_sizer, border=2, flag=wx.EXPAND | wx.ALL)

        self.update()
        self.SetSizer(main_sizer)
        self.Layout()
        self.CentreOnScreen()

    def _bindEvents(self):
        self.Bind(wx.EVT_CLOSE, self.close_window)
        self.Bind(wx.EVT_CHAR_HOOK, self.process_char_hooks)

        self.Bind(wx.EVT_BUTTON, self.check, self.check_button)
        self.Bind(wx.EVT_BUTTON, self.close, self.close_button)

    def process_char_hooks(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_ESCAPE:
            self.Close(True)

        elif event.GetId() == self.text.GetId() and keycode == wx.WXK_RETURN and event.ControlDown():
            self._check()

        elif event.GetId() == self.errors_control.GetId() and keycode == wx.WXK_RETURN:
            index = self.errors_control.GetSelection()
            match = self.crafter.matches[index]
            if len(match.replacements) == 1:
                api.copyToClip(match.replacements[0], notify=True)
            else:
                wx.CallAfter(ReplacementsGUI.create_replacements_gui, match.replacements, self.output)

        event.Skip()

    def close(self, event):
        self.Close(True)

    def close_window(self, event):
        self.crafter.close()
        self.Destroy()
        self._instance = None

    def check(self, event):
        self._check()

    def _check(self):
        text = self.text.GetValue()
        corrected_text = self.crafter.correct_extended(text)
        ui.message(_("text checked"))
        api.copyToClip(corrected_text, notify=False)
        self.update()
        self.errors_control.SetFocus()

    def update(self):
        self.text.SetValue(self.crafter.text)
        self.errors_control.Clear()
        self.errors_control.Set(self.errors)

    @property
    def errors(self) -> list[str]:
        replacements = _("Replacements:")
        results = []

        for match in self.crafter.matches:
            error = match.context[match.offset:match.offset + match.errorLength]
            results.append(f"{match.message} {error} {replacements} {', '.join(match.replacements)}")

        return results

    def output(self, corrected_text: str):
        api.copyToClip(corrected_text, notify=True)
