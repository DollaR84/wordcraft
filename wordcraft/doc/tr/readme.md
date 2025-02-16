# Yazım ve Dilbilgisi Araçları

* Yazar: Ruslan Dolovaniuk (Ukrayna)
* PayPal: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=B3VG4L8B7CV3Y&source=url
* Telegram Channel: https://t.me/elrusapps
* Telegram Group: https://t.me/elrus_apps


Bu eklenti, metinlerdeki dil bilgisi ve yazım hatalarını düzeltmeyi kolaylaştırmak için tasarlanmıştır.  
İki sistem kullanır: Otomatik Düzeltmeyi temel alan daha basit bir sistem ve LanguageTool'u temel alan daha karmaşık bir sistem.  

İlk sistem Otomatik Düzelt kitaplığını temel alır.  
Yazım hatalarını denetlemek ve düzeltmek için modelleri kullanır. Otomatik Düzelt kitaplığı, metni analiz etmek ve en olası düzeltmeleri önermek için doğal dil işleme (NLP) tekniklerini kullanır.  

İkinci, daha karmaşık sistem ise LanguageTool kütüphanesini temel alır.  
Hem dilbilgisi hem de yazım hatalarının derinlemesine denetimi için kullanılır. Bu kütüphane Java gerektirir ve dilsel metin analizi için güçlü bir araç kullanır.
LanguageTool, metindeki hataları tespit etmek ve düzeltmek için kurallar ve algoritmalar kullanır. Bu, yalnızca yazım hatalarını düzeltmenize değil, aynı zamanda karmaşık dilbilgisi hatalarını düzeltmenize ve metnin stilini geliştirmenize de olanak tanır.

## Kısayol tuşlarının listesi:

* NVDA+=: varsayılan yöntemi kullanarak metindeki hataları otomatik olarak düzeltir;
* NVDA+SHIFT+=: metindeki hataların alternatif bir yöntem kullanılarak otomatik olarak düzeltilmesi;
* NVDA+ALT+=: varsayılan yöntemi kullanarak sözcük değiştirme seçeneklerini alma;
* NVDA+ALT+SHIFT+=: alternatif bir yöntem kullanarak bir sözcüğü değiştirme seçeneklerinin alınması;
* NVDA+CTRL+=: eklenti penceresini açar;
* NVDA+CTRL+ALT+=: dili değiştirir;

Açık eklenti penceresinde:

* CTRL+ENTER: bir metin alanında "Denetle" düğmesinde olduğu gibi metin denetim modunu başlatır;
* ENTER: Bulunan hatalar listesindeki bir hata üzerine ENTER tuşuna basın: önerilen yalnızca bir değiştirme varsa, bunu metinde hemen değiştirir, aksi takdirde seçim için bir değiştirme listesi görüntüler ve değiştirmeyi seçip tıkladıktan sonra ENTER metinde onun yerine geçer;
