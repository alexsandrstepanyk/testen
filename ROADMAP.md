# Roadmap — Deutsch B1 App

Оновлено: April 2026

## Product Vision

Побудувати повноцінну платформу для підготовки до Deutsch B1, де:

- учень проходить тести, отримує сертифікат і детальний розбір
- викладач бачить аналітику і створює власні курси
- результати автоматично зберігаються, експортуються й надсилаються у Telegram

## Already Done

### Core Testing Flow

- [x] 5 повних статичних тестів
- [x] 45 питань + Schreiben
- [x] таймер проходження
- [x] автоматична перевірка відповідей
- [x] підрахунок балів і відсотка
- [x] збереження завершених сесій у БД

### Teacher Dashboard

- [x] teacher panel
- [x] фільтри по імені, тесту, статусу
- [x] деталі кожної сесії
- [x] перегляд помилок по питаннях
- [x] перегляд написаного листа
- [x] статистика по тестах
- [x] CSV export
- [x] teacher auth через HTTP Basic (`admin/admin`)

### Results and Reports

- [x] student PDF download
- [x] shared PDF generation service
- [x] повний answer key у PDF
- [x] червоне виділення неправильних відповідей
- [x] лист у PDF
- [x] certificate page на першій сторінці
- [x] красивий redesign certificate page

### Telegram Integration

- [x] повідомлення про старт тесту
- [x] PDF у Telegram після завершення тесту
- [x] налаштування через env vars

### Course Builder

- [x] teacher вкладка `Kurs-Builder`
- [x] створення власних курсів
- [x] налаштування рівня, часу, кількості завдань
- [x] створення власних питань
- [x] редагування і видалення курсів та питань
- [x] синхронізація course builder з БД

## In Progress / Next Priority

### 1. Custom Courses for Students

- [ ] показувати custom courses на student page
- [ ] запускати сесію не лише для стандартних 5 тестів, а й для custom course
- [ ] відображати структуру custom course у test UI
- [ ] рахувати результати для custom course
- [ ] включати custom course results у leaderboard або окремий рейтинг

### 2. Course Builder Completion

- [ ] preview custom course before publish
- [ ] duplicate course
- [ ] reorder questions with better UX
- [ ] validate builder counts against real number of questions
- [ ] CSV import/export for custom questions

### 3. Teacher and Admin Security

- [ ] винести `admin/admin` у env vars
- [ ] додати окремі teacher accounts
- [ ] audit trail для змін курсів
- [ ] обмежити небезпечні teacher actions

## Planned Versions

## Version 1.5 — Custom Course Delivery

- [ ] custom courses visible to students
- [ ] проходження custom course end-to-end
- [ ] PDF and certificate support for custom courses
- [ ] Telegram support for custom courses

## Version 1.6 — Better Analytics

- [ ] analytics by question
- [ ] hardest questions report
- [ ] success rate by Teil
- [ ] student progress history
- [ ] top students by teacher-created courses

## Version 1.7 — Content Operations

- [ ] CSV bulk import
- [ ] JSON import/export
- [ ] question templates
- [ ] reusable writing prompts
- [ ] media attachments for tasks

## Version 2.0 — Full Exam Platform

- [ ] Horen / audio tasks
- [ ] speaking simulation
- [ ] writing evaluation assistant
- [ ] multilingual interface
- [ ] student accounts and saved history
- [ ] teacher groups / classes
- [ ] certificates with verification code

## Technical Roadmap

- [ ] add Alembic migrations instead of only `create_all`
- [ ] add pytest coverage for API and scoring
- [ ] add CI pipeline
- [ ] add safer settings management
- [ ] split large frontend HTML files into templates or modular frontend
- [ ] improve error handling around Telegram delivery
- [ ] add backup/export strategy for teacher-created content

## Product/UX Roadmap

- [ ] better onboarding for teachers
- [ ] custom branding for certificates
- [ ] student dashboard with previous attempts
- [ ] printable teacher reports
- [ ] dedicated course publication flow
- [ ] clear separation between static official tests and teacher custom tests

## Success Criteria

Проєкт можна вважати вийшовшим на наступний рівень, коли:

- teacher can build a course and publish it
- student can open and pass that custom course
- result is saved to DB
- PDF and certificate are generated correctly
- Telegram receives the final PDF automatically
