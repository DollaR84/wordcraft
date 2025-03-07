# wordcraft

* Автор: Руслан Долованюк (Україна)
* PayPal: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=B3VG4L8B7CV3Y&source=url
* Telegram Channel: https://t.me/elrusapps
* Telegram Group: https://t.me/elrus_apps


Цей аддон розроблений для полегшення виправлення граматичних та орфографічних помилок у текстах.
Він використовує дві системи: простішу на основі AutoCorrect і складнішу на основі LanguageTool.

Перша система базується на бібліотеці AutoCorrect.
Вона використовує моделі для перевірки та виправлення орфографічних помилок. Бібліотека AutoCorrect застосовує методи обробки природної мови (NLP) для аналізу тексту та пропозиції найімовірніших виправлень.

Друга, складніша система заснована на бібліотеці LanguageTool.
Вона використовується для глибокої перевірки як граматичних, і орфографічних помилок. Ця бібліотека вимагає Java та використовує потужний інструмент для лінгвістичного аналізу тексту.
LanguageTool використовує правила та алгоритми для виявлення та виправлення помилок у тексті. Це дозволяє не тільки виправляти орфографічні помилки, але й виправляти складні граматичні помилки та покращувати стиль тексту.

## Список гарячих клавіш:
* NVDA+=: автовиправлення помилок у тексті методом за замовчуванням;
* NVDA+SHIFT+=: автовиправлення помилок у тексті альтернативним методом;
* NVDA+ALT+=: отримання варіантів замін слова методом за замовчуванням;
* NVDA+ALT+SHIFT+=: отримання варіантів замін слова альтернативним методом;
* NVDA+CONTROL+=: відкрити вікно доповнення;
* NVDA+CONTROL+ALT+=: змінити мову;

У відкритому вікні доповнення:
* CONTROL+ENTER у текстовому полі запускає режим перевірки тексту, як за кнопкою "Перевірити";
* ENTER на помилці у списку знайдених помилок: якщо запропонована заміна одна - відразу замінює її в тексті, інакше видає список замін для вибору, і після вибору та натискання на заміні ENTER замінює її в тексті;
