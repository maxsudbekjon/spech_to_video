# Virtual Video Chat Simulator (Django)

Anime uslubidagi virtual qahramon bilan video suhbatni simulyatsiya qiluvchi demo. Ilova foydalanuvchi nutqidan kalit so'zlarni aniqlab, mos video javoblarni ijro etadi. Video o'zgarishlari qora ekran yoki "flash"siz bo'lishi uchun oldindan preload qilinadi va bir vaqtning o'zida DOMda saqlanadi.

## Setup & Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requiremend.txt
cp env.example .env
python manage.py migrate
python manage.py runserver
```

Brauzer: `http://localhost:8000`

> Eslatma: SpeechRecognition faqat HTTPS yoki `localhost`da ishlaydi.

## .env sozlamalari

Minimal ishlashi uchun `.env` fayl yarating va quyidagilarni to'ldiring:

- `SECRET_KEY`: Django uchun maxfiy kalit. Terminal orqali yaratish:
  ```bash
  python3 -c "import secrets; print(secrets.token_urlsafe(50))"
  ```
- `DEBUG`: `True` yoki `False`.
- `ALLOWED_HOSTS`: masalan `localhost,127.0.0.1`.

### Database (default: SQLite)

Test va lokal development uchun default SQLite ishlatiladi. Hech qanday qo'shimcha DB sozlash shart emas.

Kerak bo'lsa `.env`da quyidagilarni yozing:

```env
DB_TYPE=SQLITE
```

### Postgres (ixtiyoriy)

Agar Postgres ishlatmoqchi bo'lsangiz:

```env
DB_TYPE=POSTGRES
DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Texnologiya tanlovi

- Django templates: tez prototip va server-side asset hosting.
- Native `<video>`: kutubxonalarsiz to'g'ridan-to'g'ri playback va preload nazorati.
- Web Speech API: bepul, brauzerga built-in STT.

## Video Playback Strategiyasi (Seamless)

- Har bir holat uchun alohida `<video>` elementi bor (idle, greeting, listening, weather, general, fallback, prompt, goodbye).
- Barcha videolar `preload="auto"` bilan yuklanadi va DOMda yashirin turadi.
- Holat o'zgarganda yangi video `play()` qilinadi, `playing` eventidan so'ng eski video `pause()` qilinadi.
- Opacity orqali almashtirish qilinadi, shuning uchun qora ekran bo'lmaydi.

## Speech Integration Logikasi

- `SpeechRecognition` / `webkitSpeechRecognition` ishlatiladi.
- Listening holati boshlanganda mic start bo'ladi.
- Natija kelgach: `hello/hi`, `weather/today`, `goodbye/bye` keywordlari tekshiriladi.
- `easter/secret` kalit so'zlari bo'lsa Easter egg video ishlaydi.
- Xato bo'lsa `fallback` video ijro etiladi.
- 9 soniya jimlik bo'lsa `prompt` video, 2-marta bo'lsa `goodbye`.
- `SpeechRecognition` onend bo'lsa va listening davom etayotgan bo'lsa, qayta start qilinadi.

## Core Requirements holati

- Seamless state transitionlar (Waiting/Idle → Greeting → Listening → Response → Listening → Goodbye → Waiting)
- SpeechRecognition integratsiyasi va mic permission handling
- Responsive dizayn + transcript ko'rsatish
- Error/fallback handling

## Stretch Goals bajarilganlar

- 8-10 soniya jimlikdan keyin prompt
- Ikkinchi jimlikdan keyin auto-end
- Mic pulse animatsiya
- Mobil responsiv dizayn
- Transcript

## Qiyinchiliklar va yechimlar

- **Black flash**: bir nechta `<video>` element va `playing` eventidan keyin eski videoni to'xtatish orqali hal qilindi.
- **Seamless switch**: yangi video birinchi frame tayyor bo'lgachgina ko'rsatiladi, shuning uchun o'tishda uzilish sezilmaydi.
- **Autoplay policy**: idle video `muted` bo'ladi, audio kerak bo'lganda `Start Chat` interactionidan so'ng yoqiladi.

## Known Limitations

- SpeechRecognition brauzerga bog'liq (Chrome/Edge tavsiya etiladi).
- STT tili hozircha `en-US`.
- Demo assets audio sifatiga bog'liq.

## Demo Video (tavsiya)

1-2 daqiqalik demo:
- To'liq flow
- Bitta failure case
- Silence prompt

## AI foydalanish

AI yordamida yozilgan bo'lsa ham, kodning har bir qismi tushunarli va maintainable bo'lishi ko'zda tutilgan.
