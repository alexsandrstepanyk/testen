# Roadmap — Deutsch B1 App

Оновлено: April 2026

---

## Product Vision

Повноцінна платформа для підготовки до Deutsch B1:
- учень проходить тести, отримує сертифікат і детальний розбір
- викладач бачить аналітику і створює власні курси
- результати автоматично зберігаються, експортуються й надсилаються у Telegram

---

## ✅ Зроблено

### Core Testing Flow

- [x] 5 повних статичних тестів
- [x] 5-частинна структура: Teil 1–4 (20+10+15+10) + Teil 5 Schreiben
- [x] Teil 4: Anzeigen zuordnen
- [x] 55 тестових питань + Schreiben (максимум 65 балів)
- [x] таймер проходження
- [x] автоматична перевірка відповідей і підрахунок балів
- [x] збереження завершених сесій у БД
- [x] збереження email і телефону учня в БД

### Custom Courses для учнів ✅ (Version 1.5)

- [x] опубліковані курси відображаються на student page поряд зі статичними тестами
- [x] учень стартує і проходить custom course через стандартний test UI
- [x] test_number encoding: custom course id → test_number 1000+id (прозоро для всієї системи)
- [x] PDF-звіт і Telegram для custom courses (той самий flow, що і для статичних тестів)
- [x] неопубліковані курси приховані від учнів (фільтр `is_published=True`)

### Teacher Security ✅ (Version 1.5)

- [x] credentials через env vars `TEACHER_USERNAME` / `TEACHER_PASSWORD`
- [x] fallback `admin/admin` якщо env vars не задані
- [x] `TeacherAccount` модель: нові accounts зберігаються в БД з bcrypt-хешем
- [x] `POST /api/teacher/accounts` — створити account
- [x] `GET  /api/teacher/accounts` — список accounts
- [x] `DELETE /api/teacher/accounts/{id}` — деактивувати account (soft delete)

### Audit Trail ✅ (Version 1.5)

- [x] `AuditLog` модель: teacher_username, action, resource_type, resource_id, detail, created_at
- [x] автоматичне логування: create / update / publish / delete для курсів і питань
- [x] логування create / deactivate для teacher accounts
- [x] `GET /api/teacher/audit-log` — перегляд лога

### Speaking

- [x] Teil 6: Selbstvorstellung — відеозапис із вебкамери
- [x] Teil 7: Bildbeschreibung — відеозапис із вебкамери
- [x] відправка відео в Telegram + збереження file_id в БД
- [x] локальний fallback для збереження відео

### Teacher Dashboard

- [x] teacher panel з HTTP Basic Auth
- [x] фільтри по імені, тесту, статусу
- [x] деталі кожної сесії: відповіді, помилки, лист
- [x] перегляд двох speaking-відео
- [x] оцінювання Selbstvorstellung і Bildbeschreibung із текстовим feedback
- [x] статистика по тестах
- [x] CSV export

### Results and Reports

- [x] student PDF download
- [x] certificate page на першій сторінці PDF
- [x] повний answer key у PDF (правильні + неправильні червоним)
- [x] Schreiben у PDF
- [x] PDF у Telegram після завершення тесту
- [x] PDF/Telegram для custom courses

### Leaderboard

- [x] global leaderboard
- [x] тестові QA-записи приховані з рейтингу

### Kurs-Builder (Teacher)

- [x] CRUD курсів: створення, редагування, видалення
- [x] налаштування рівня, часу, кількості завдань
- [x] CRUD питань: mc, rf, text, audio
- [x] завантаження аудіо-файлів
- [x] publish / unpublish курсу
- [x] синхронізація з БД

### SEO і Legal (DE/EU)

- [x] meta tags, canonical, OpenGraph, Twitter Cards
- [x] structured data (JSON-LD)
- [x] robots.txt + sitemap.xml
- [x] Impressum і Datenschutzerklärung
- [x] teacher page — noindex

---

## ❌ Не зроблено — Наступні кроки

### 🟡 Speaking Storage

- [ ] перенести speaking video у persistent external storage (S3 або аналог)
- [ ] прибрати залежність від ephemeral filesystem на Render
- [ ] додати явний статус доставки відео в Telegram

### 🟡 Kurs-Builder Completion

- [ ] preview курсу перед публікацією
- [ ] дублювання курсу
- [ ] reorder питань з кращим UX
- [ ] валідація кількості питань у налаштуваннях проти реальних записів у БД
- [ ] CSV import/export для власних питань

### 🟢 Аналітика (Version 1.6)

- [ ] статистика по питаннях: найскладніші, success rate по Teil
- [ ] прогрес учня по сесіях
- [ ] топ учнів по teacher-created courses
- [ ] custom course results у leaderboard або окремий рейтинг

### 🟢 GDPR і Growth

- [ ] cookie consent banner (GDPR compliant)
- [ ] Google Analytics 4 + Consent Mode v2
- [ ] AdSense тільки після consent

### 🟢 Content Operations (Version 1.7)

- [ ] CSV/JSON bulk import питань
- [ ] question templates
- [ ] reusable writing prompts
- [ ] media attachments для завдань

### ⚪ Майбутнє (Version 2.0)

- [ ] Hören — аудіо-завдання (прослухати → відповісти)
- [ ] Einkaufszentrum / Etagen-Suche задачі
- [ ] speaking simulation з оцінкою
- [ ] writing evaluation assistant
- [ ] multilingual interface
- [ ] student accounts зі збереженою історією

---

## Версійний план

| Версія | Фокус | Статус |
|--------|-------|--------|
| **1.4** | Course Builder (teacher side), Speaking 2 videos, SEO | ✅ Done |
| **1.5** | Custom Course Delivery, Teacher Accounts, Audit Trail, env var auth | ✅ Done |
| **1.6** | Better Analytics — статистика по питаннях і прогрес | ⬜ Next |
| **1.7** | Content Operations — bulk import, templates | ⬜ Planned |
| **2.0** | Full Exam Platform — Hören, speaking sim, student accounts | ⬜ Planned |
