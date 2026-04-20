# Deutsch B1 App

Інтерактивна платформа для підготовки до Goethe-Zertifikat B1 з повною симуляцією тесту, teacher dashboard, PDF-звітами, Telegram-сповіщеннями та конструктором власних курсів.

---

## Статус проєкту

Версія: **1.5.2 (Production Ready)**
Деплой: **Render** (Docker + PostgreSQL Frankfurt)

---

## Що вже реалізовано ✅

### Тестування для учня

- 5 готових повних тестів на теми B1
- 5-частинна структура іспиту: Teil 1–4 (20 + 10 + 15 + 10 завдань) + Teil 5 Schreiben
- Teil 4: Anzeigen zuordnen (оголошення → запитання)
- Teil 6: Selbstvorstellung — відеозапис із вебкамери
- Teil 7: Bildbeschreibung — відеозапис із вебкамери
- таймер проходження тесту
- автоматичний підрахунок балів і відсотка
- збереження email і телефону учня в БД
- сторінка результатів одразу після завершення
- PDF-звіт із сертифікатом — завантаження та відправка в Telegram

### Custom Courses для учнів ✅ (NEW 1.5)

- опубліковані курси (`is_published = true`) відображаються в grid поряд зі статичними тестами
- учень стартує, проходить і здає custom course через той самий test UI
- результати, PDF і Telegram для custom courses працюють автоматично (через test_number encoding)
- неопубліковані курси приховані від учнів (тільки teacher може їх бачити в Kurs-Builder)

### Teacher Dashboard

- вхід через HTTP Basic Auth
- credentials задаються через env vars `TEACHER_USERNAME` / `TEACHER_PASSWORD` (default: `admin/admin`)
- додаткові teacher accounts зберігаються в БД (bcrypt-хеш, `TeacherAccount` модель)
- перегляд усіх завершених сесій
- фільтрація за тестом, статусом, іменем
- деталі кожної сесії: помилки, відповіді, лист
- перегляд двох speaking-відео учня
- оцінювання Selbstvorstellung і Bildbeschreibung із коментарями
- статистика по тестах
- CSV export
- Leaderboard (тестові QA-записи відфільтровані)

### Teacher Accounts + Audit Trail ✅ (NEW 1.5)

- `GET  /api/teacher/accounts` — список teacher accounts
- `POST /api/teacher/accounts` — створити новий account (username ≥ 3 символи, password ≥ 8)
- `DELETE /api/teacher/accounts/{id}` — деактивувати account (soft delete)
- `GET  /api/teacher/audit-log` — audit log усіх дій із курсами та accounts
- кожна дія create / update / publish / delete на курсах і питаннях логується автоматично

### Student History Lookup ✅ (NEW 1.5.1)

- кнопка **"Meine Ergebnisse ansehen"** на стартовому екрані
- учень вводить ім'я + email або телефон → бачить усі свої тести
- картки з балами, відсотком, рівнем (A1/A2/B1), розбивкою по Teil 1–5, датою, тривалістю
- якщо teacher залишив feedback — відображається під карткою
- кнопка **PDF-Bericht herunterladen** для кожної сесії
- без реєстрації — ідентифікація тільки через ім'я + контакт



### Kurs-Builder (Teacher)

- вкладка `Kurs-Builder` у teacher dashboard
- створення / редагування / видалення власних курсів
- налаштування рівня, часу, кількості завдань
- типи питань: `mc`, `rf`, `text`, `audio`
- завантаження аудіо-файлів до питань
- **publish toggle** — тільки опубліковані курси видно учням
- синхронізація з БД (моделі `CustomCourse`, `CustomQuestion`)

### CSV Import / Export питань ✅ (NEW 1.5.2)

- `GET /api/courses/{id}/questions/export-csv` — завантажує всі питання курсу як `.csv`
- `POST /api/courses/{id}/questions/import-csv` — bulk-завантаження питань із CSV-файлу
- колонки: `order_index, teil, question_type, question_text, context_text, option_a, option_b, option_c, correct_answer, points, explanation`
- підтримує файли з BOM (Excel), пропускає невалідні рядки з описом помилок
- **шаблон для завантаження** — можна відправити в ChatGPT для AI-генерації питань
- дія логується в audit log

### PDF-звіт

1. перша сторінка — красивий сертифікат із рівнем і балами
2. детальний розбір по питаннях
3. правильні та неправильні відповіді (неправильні — червоним)
4. текст написаного листа

### Telegram інтеграція

- повідомлення про старт тесту
- PDF у Telegram після завершення тесту (включаючи custom courses)
- Teil 6 відео → Telegram + збереження `file_id` в БД
- Teil 7 відео → Telegram + збереження `file_id` в БД

### Оцінювання рівня

| Відсоток | Рівень |
|----------|--------|
| ≥ 70%    | B1     |
| ≥ 55%    | A2     |
| < 55%    | A1     |

### SEO та Legal (EU)

- meta tags, canonical, OpenGraph, Twitter Cards
- structured data (JSON-LD)
- `robots.txt` і `sitemap.xml`
- сторінки `Impressum` і `Datenschutzerklärung`
- teacher page позначена `noindex`

---

## Що ще НЕ зроблено ❌

| Пріоритет | Завдання |
|-----------|----------|
| 🟡 Speaking | Persistent video storage (зараз Render ephemeral filesystem) |
| 🟡 Speaking | Явний статус доставки відео в Telegram |
| 🟡 Builder | Preview курсу перед публікацією |
| 🟡 Builder | Дублювання курсу |
| 🟡 Builder | Валідація кількості питань проти реальних записів у БД |
| 🟢 Аналітика | Статистика по питаннях: найскладніші, success rate по Teil |
| 🟢 Аналітика | Прогрес учня по сесіях |
| 🟢 GDPR | Cookie consent banner + Google Analytics 4 + Consent Mode v2 |
| ⚪ Майбутнє | Hören / аудіо-завдання |
| ⚪ Майбутнє | Speaking simulation з оцінкою |
| ⚪ Майбутнє | Student history lookup зі збереженням відео (persistent storage) |

---

## Архітектура

### Backend

- `FastAPI` + `SQLAlchemy`
- `PostgreSQL` (Render) або `SQLite` (локально)
- `ReportLab` для PDF
- `httpx` для Telegram Bot API
- `passlib[bcrypt]` для хешування паролів

### Frontend

- чистий `HTML + CSS + JavaScript`
- `index.html` — student page
- `teacher.html` — teacher dashboard + Kurs-Builder
- `admin.html` — додаткова адмін-сторінка

---

## Структура проєкту

```text
deutsch-b1-app/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── models/
│   │   ├── database.py
│   │   ├── models.py          # TestSession, CustomCourse, CustomQuestion,
│   │   │                      # TeacherAccount, AuditLog
│   │   └── questions_data.py  # 5 статичних тестів
│   ├── routers/
│   │   ├── course_builder.py  # CRUD курсів і питань + audit log
│   │   ├── questions.py
│   │   ├── results.py
│   │   ├── schreiben.py
│   │   ├── sessions.py        # старт/фініш, відео-upload
│   │   └── teacher.py         # dashboard, accounts, audit log
│   ├── schemas/
│   │   └── schemas.py
│   └── services/
│       ├── question_resolver.py  # encode/decode custom test numbers
│       ├── report_pdf.py
│       └── telegram.py
├── frontend/
│   ├── index.html
│   ├── teacher.html
│   ├── admin.html
│   ├── datenschutz.html
│   ├── impressum.html
│   ├── robots.txt
│   └── sitemap.xml
├── Dockerfile
├── render.yaml
├── README.md
└── ROADMAP.md
```

---

## Локальний запуск

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

| URL | Призначення |
|-----|-------------|
| `http://localhost:8000` | student app |
| `http://localhost:8000/teacher` | teacher dashboard |
| `http://localhost:8000/docs` | Swagger API docs |
| `http://localhost:8000/api/health` | health check |

---

## Deploy на Render

Проєкт підготовлений під Render через `render.yaml`.

- Docker + Web Service + PostgreSQL, region: Frankfurt
- Speaking відео зберігаються **локально** (ephemeral на Render — потрібен external storage)

### Env vars

```env
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
DATABASE_URL=postgresql://...
WEB_CONCURRENCY=1
TEACHER_USERNAME=admin
TEACHER_PASSWORD=your_secure_password_here
```

---

## Teacher Auth

**Primary account** — задається через env vars `TEACHER_USERNAME` / `TEACHER_PASSWORD` (fallback: `admin/admin`).

**Додаткові accounts** — зберігаються в БД з bcrypt-хешем:

```http
POST /api/teacher/accounts
Content-Type: application/json
Authorization: Basic ...

{ "username": "maria", "password": "securepass123" }
```

---

## Автор

Stepaniuk Oleksandr — `https://stepaniuk.shop`
