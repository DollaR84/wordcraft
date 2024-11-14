# wordcraft

* Author: Ruslan Dolovaniuk (Ukraine)
* PayPal: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=B3VG4L8B7CV3Y&source=url


This addon is designed to make it easier to correct grammatical and spelling errors in texts.
It uses two systems: a simpler one based on AutoCorrect and a more complex one based on LanguageTool.

The first system is based on the AutoCorrect library.
It uses models to check and correct spelling errors. The AutoCorrect library uses natural language processing (NLP) techniques to analyze text and suggest the most likely corrections.

The second, more complex system is based on the LanguageTool library.
It is used for in-depth checking of both grammatical and spelling errors. This library requires Java and uses a powerful tool for linguistic text analysis.
LanguageTool uses rules and algorithms to detect and correct errors in text. This allows you to not only correct spelling errors, but also correct complex grammatical errors and improve the style of the text.

## List of hotkeys:
* NVDA+=: default method for autocorrecting errors;
* NVDA+SHIFT+=: alternative method for auto-correcting errors;
* NVDA+ALT+=: default method for getting replacement options;
* NVDA+ALT+SHIFT+=: alternative method for obtaining replacement options;
* NVDA+CONTROL+=: open add-on window;
* NVDA+CONTROL+ALT+=: change language;

In the open add-on window:
* CONTROL+ENTER in a text field starts the text checking mode, as with the "Check" button;
* ENTER on an error in the list of found errors: if there is only one proposed replacement, it immediately copies it to the clipboard, otherwise it displays a list of replacements for selection, and after selecting and clicking on the replacement, ENTER copies it to the clipboard;
