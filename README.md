# Deutsch B1 App

Інтерактивна платформа для підготовки до Goethe-Zertifikat B1 з повною симуляцією тесту, teacher dashboard, PDF-звітами, Telegram-сповіщеннями та конструктором власних курсів.

## Що вже є в проєкті

- 5 готових повних тестів на теми B1
- 5-частинна структура іспиту: Teil 1-4 (20+10+15+10 завдань) + Teil 5 Schreiben
- додаткові speaking tasks: Teil 6 `Selbstvorstellung` + Teil 7 `Bildbeschreibung`
- 55 тестових питань + Schreiben (максимум 65 балів загалом)
- таймер проходження тесту
- автоматичний підрахунок балів і відсотка
- сторінка результату одразу після завершення тесту
- teacher dashboard з переглядом усіх результатів
- HTTP Basic Auth для teacher panel: `admin / admin`
- leaderboard для порівняння результатів
- PDF-звіт для учня після завершення тесту
- Telegram bot: повідомлення про старт тесту та PDF після завершення
- Telegram video flow: завантаження student presentation video і teacher review
- сертифікат на першій сторінці PDF з визначенням рівня `B1 / A2 / A1`
- детальний звіт на наступних сторінках PDF:
   - помилки
   - усі відповіді та правильні варіанти
   - виділення неправильних відповідей червоним
   - текст листа
- нова вкладка `Kurs-Builder` у teacher dashboard
- збереження власних курсів викладача в БД
- збереження власних питань викладача в БД

## Поточна логіка оцінювання сертифіката

- `B1`: від `70%`
- `A2`: від `55%`
- `A1`: нижче `55%`

## Архітектура

### Backend

- `FastAPI`
- `SQLAlchemy`
- `PostgreSQL` на Render або `SQLite` локально
- `ReportLab` для PDF
- `httpx` для Telegram Bot API

### Frontend

- чистий `HTML + CSS + JavaScript`
- окрема сторінка для учня
- окрема сторінка для викладача

## Структура проєкту

```text
deutsch-b1-app/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── questions_data.py
│   ├── routers/
│   │   ├── course_builder.py
│   │   ├── questions.py
│   │   ├── results.py
│   │   ├── schreiben.py
│   │   ├── sessions.py
│   │   └── teacher.py
│   ├── schemas/
│   │   └── schemas.py
│   └── services/
│       ├── report_pdf.py
│       └── telegram.py
├── frontend/
│   ├── datenschutz.html
│   ├── impressum.html
│   ├── index.html
│   ├── robots.txt
│   ├── sitemap.xml
│   └── teacher.html
├── Dockerfile
├── render.yaml
├── README.md
└── ROADMAP.md
```

## Основні можливості для учня

- вибір одного з 5 тестів
- проходження всіх 5 частин іспиту
- новий блок Teil 4: Anzeigen zuordnen (оголошення -> запитання)
- написання листа в Teil 5
- запис двох окремих speaking-відео з вебкамери:
   - Teil 6: Selbstvorstellung
   - Teil 7: Bildbeschreibung
- миттєвий результат після сабміту
- PDF зі звітом і сертифікатом
- збереження результату в БД
- відправка speaking-відео в Telegram після запису

## Основні можливості для викладача

- вхід у teacher panel через `admin / admin`
- перегляд усіх завершених сесій
- фільтрація за тестом, статусом, іменем
- перегляд деталей кожної спроби
- перегляд листа учня
- перегляд двох speaking-відео учня
- окреме оцінювання `Selbstvorstellung` і `Bildbeschreibung`
- аналіз помилок по кожному питанню
- CSV export
- статистика по тестах
- створення власних курсів у `Kurs-Builder`
- створення власних питань для курсів

## PDF-звіт

Після завершення тесту формується PDF, який може бути:

- відкритий учнем вручну через кнопку на сторінці результатів
- автоматично надісланий у Telegram бот

PDF містить:

1. красиву першу сторінку у форматі сертифіката
2. ім'я учня
3. отримані бали та відсоток
4. присвоєний рівень
5. детальний звіт по питаннях
6. правильні та неправильні відповіді
7. текст листа

## Telegram інтеграція

Підтримуються дві події:

1. старт тесту: повідомлення в Telegram
2. завершення тесту: PDF-документ у Telegram
3. завантаження Teil 6: student self-introduction video у Telegram + збереження file_id в БД
4. завантаження Teil 7: student image-description video у Telegram + збереження file_id в БД

Потрібні environment variables:

```env
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

## Teacher Auth

Teacher panel захищена через HTTP Basic Auth.

Поточні облікові дані:

```text
username: admin
password: admin
```

Примітка: для production варто винести ці значення в environment variables.

## Локальний запуск

### Вимоги

- Python `3.11+` для production-сумісного запуску
- `pip`

### Запуск локально

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Локальні адреси

- app: `http://localhost:8000`
- teacher: `http://localhost:8000/teacher`
- docs: `http://localhost:8000/docs`
- health: `http://localhost:8000/api/health`

## Deploy на Render

Проєкт уже підготовлений під Render через `render.yaml`.

### Що використовується на Render

- `Docker`
- `Web Service`
- `PostgreSQL`
- region: `Frankfurt`

### Основні env vars

```env
PYTHON_VERSION=3.11.0
WEB_CONCURRENCY=1
DATABASE_URL=...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
```

### Ручний деплой

1. Відкрити Render service `deutsch-b1-app`
2. Натиснути `Manual Deploy`
3. Обрати `Deploy Latest Commit`

## API секції

- `/api/questions` — отримання питань готових тестів
- `/api/sessions` — старт і завершення сесій
- `/api/results` — результати та PDF-звіти
- `/api/schreiben` — Schreiben related endpoints
- `/api/teacher` — dashboard викладача
- `/api/teacher/courses` — course builder для власних курсів

## Що вже зроблено останніми ітераціями

- перевірено production deployment і збереження сесій у БД
- виправлено teacher details loading після додавання auth
- додано авторський credit на student page
- додано student PDF download
- винесено генерацію PDF у shared service
- додано Telegram bot integration
- покращено PDF: всі відповіді, правильні рішення, лист, червоне виділення помилок
- додано certificate page на першій сторінці PDF
- перероблено certificate page у більш професійний дизайн
- додано teacher `Kurs-Builder` з БД-синхронізацією
- додано новий Teil 4 (Anzeigen zuordnen) і перенесено Schreiben у Teil 5
- оновлено student UI, teacher dashboard і PDF-звіт під 5 частин
- speaking flow розділено на два окремі video tasks:
   - Teil 6: Selbstvorstellung
   - Teil 7: Bildbeschreibung
- teacher dashboard оновлено під два speaking video blocks і два окремі feedback fields
- локально speaking video може зберігатися через fallback у static storage, якщо Telegram не налаштований
- додано фільтр тестових QA-записів у leaderboard
- виправлено production баг у teacher details modal (стабільне відкриття деталей сесії)
- додано SEO-базу для індексації:
   - meta description, canonical, Open Graph, Twitter cards
   - structured data (JSON-LD)
   - `robots.txt` + `sitemap.xml`
   - server routes для `/robots.txt` і `/sitemap.xml`
- додано юридичні сторінки для DE/EU:
   - `Impressum` (`/impressum`)
   - `Datenschutzerklaerung` (`/datenschutz`)
   - посилання на обидві сторінки у футері
- закрито teacher dashboard від індексації (`noindex`)

## Поточні обмеження

- custom courses уже можна створювати в teacher panel, але student page поки проходить тільки 5 статичних тестів
- teacher credentials поки що хардкодні
- автоматичні тести ще не додані
- міграції БД поки не використовуються; таблиці створюються через `Base.metadata.create_all()`

## Найближчі наступні кроки

1. підключити custom courses до student flow
2. дати учням можливість проходити курси, створені викладачем
3. додати оцінювання custom courses у results / PDF / Telegram
4. винести teacher credentials у env vars
5. додати cookie consent banner (GDPR) перед ads/analytics
6. додати Google Analytics 4 + Consent Mode v2
7. реалізувати нову частину `Hoeren` (аудіо -> питання по тексту)
8. реалізувати задачі типу `Einkaufszentrum / Etagen-Suche` (на якому поверсі купити річ)
9. додати automated tests

## Автор

Stepaniuk Oleksandr  
Website: `https://stepaniuk.shop`
