import addonHandler


addonHandler.initTranslation()


class Translator:
    required_languages = _("Required languages:")
    default_language = _("Default language:")
    default_method_for_auto_correct = _("Default method for auto correct:")
    default_method_for_get_variants = _("Default method for get variants:")
    auto_correct = _("Auto correct")
    copy_to_clipboard = _("Copy to clipboard")

    available_only_for_simple_method = _("This language is only available for the simple method")
    available_only_for_extended_method = _("This language is only available for the extended method")
    errors_found = _("errors found")
    corrected_to = _("corrected to:")
    no_selection = _("No selection")
    replacements_suggested_for_word = _("replacements are suggested for the word")
    language_changed_to = _("language changed to ")

    main_window_title = _("Checking grammar and spelling")
    text = _("Text")
    list_errors = _("List errors:")
    check = _("Check")
    close = _("Close")
    text_checked = _("text checked")
    replacements = _("Replacements:")
