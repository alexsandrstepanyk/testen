# 🇩🇪 Deutsch B1 Übungstest

**Інтерактивна платформа для підготовки до іспиту Goethe-Zertifikat B1**

---

## 📋 Про проект

Цей додаток допомагає учням готуватися до іспиту **Deutsch B1** з повною симуляцією тесту:

- ✅ **5 повних тестів** з різними темами
- ✅ **4 частини**: Multiple Choice, Richtig/Falsch, Leseverstehen, Schreiben (лист)
- ✅ **Таймер** для кожної частини (15 хв + 15 хв + 15 хв + 20 хв)
- ✅ **Миттєві результати** з детальним аналізом помилок
- ✅ **Панель вчителя** з переглядом результатів усіх учнів
- ✅ **Leaderboard** для змагання між учнями

---

## 🚀 Деплой на Render.com

### Крок 1: Створіть GitHub репозиторій

```bash
# Ініціалізація Git (якщо ще не створено)
git init
git add .
git commit -m "Initial commit - Deutsch B1 App"
```

### Крок 2: Завантажте на GitHub

```bash
# Створіть новий репозиторій на github.com
# Потім виконайте:
git remote add origin https://github.com/ВАШ_НІК/deutsch-b1-app.git
git branch -M main
git push -u origin main
```

### Крок 3: Зареєструйтеся на Render.com

1. Перейдіть на [render.com](https://render.com)
2. Натисніть **"Get Started for Free"**
3. Увійдіть через **GitHub** (рекомендується)

### Крок 4: Створіть новий Web Service

1. Натисніть **"New +"** → **"Web Service"**
2. Виберіть **"Connect a repository"**
3. Знайдіть ваш репозиторій `deutsch-b1-app`
4. Натисніть **"Connect"**

### Крок 5: Налаштуйте Web Service

| Параметр | Значення |
|----------|----------|
| **Name** | `deutsch-b1-app` (або ваша назва) |
| **Region** | `Frankfurt, Germany` (найближче до України) |
| **Branch** | `main` |
| **Root Directory** | залиште пустим |
| **Runtime** | `Docker` |
| **DockerfilePath** | `./Dockerfile` |
| **Plan** | `Free` |

### Крок 6: Додайте змінні оточення

Натисніть **"Advanced"** → **"Add Environment Variable"**:

```
DATABASE_URL = (буде автоматично додано з бази даних)
PYTHON_VERSION = 3.11.0
WEB_CONCURRENCY = 1
```

### Крок 7: Створіть базу даних PostgreSQL

1. Поверніться на головну Render
2. Натисніть **"New +"** → **"PostgreSQL"**
3. Заповніть:
   - **Name**: `deutsch-b1-db`
   - **Region**: `Frankfurt`
   - **Plan**: `Free`
4. Натисніть **"Create Database"**

### Крок 8: Підключіть базу даних

1. Відкрийте ваш **Web Service**
2. Перейдіть у вкладку **"Environment"**
3. Натисніть **"Add From"** → **"Database"**
4. Виберіть `deutsch-b1-db`
5. Додайте змінну `DATABASE_URL` з властивості `connectionString`

### Крок 9: Запустіть деплой

1. Поверніться на головну Web Service
2. Натисніть **"Manual Deploy"** → **"Deploy Latest Commit"**
3. Зачекайте 3-5 хвилин (перший деплой)

### Крок 10: Підключіть свій домен

1. Відкрийте Web Service → вкладка **"Settings"**
2. Знайдіть **"Custom Domains"**
3. Натисніть **"Add Custom Domain"**
4. Введіть ваш домен (наприклад, `deutsch-b1.com`)
5. Натисніть **"Save"**

#### Налаштуйте DNS у реєстратора домену:

```
Тип запису: CNAME
Ім'я: @ (або залиште пустим)
Значення: deutsch-b1-app.onrender.com
TTL: Automatic
```

**Або для піддомену:**
```
Тип запису: CNAME
Ім'я: www
Значення: deutsch-b1-app.onrender.com
TTL: Automatic
```

---

## 🔧 Локальна розробка

### Вимоги
- Python 3.10+
- pip

### Встановлення

```bash
# Встановіть залежності
cd backend
pip install -r requirements.txt

# Запустіть сервер
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Відкрийте у браузері

- **Frontend**: http://localhost:8000
- **Teacher Dashboard**: http://localhost:8000/teacher
- **Leaderboard**: http://localhost:8000/leaderboard
- **API Docs**: http://localhost:8000/docs

---

## 📁 Структура проекту

```
deutsch-b1-app/
├── backend/
│   ├── main.py              # FastAPI додаток
│   ├── models/
│   │   ├── models.py        # SQLAlchemy моделі
│   │   └── database.py      # Підключення до БД
│   ├── routers/
│   │   ├── questions.py     # API для запитань
│   │   ├── sessions.py      # API для сесій
│   │   ├── results.py       # API для результатів
│   │   ├── schreiben.py     # API для письма
│   │   └── teacher.py       # API для вчителя
│   └── schemas/
│       └── schemas.py       # Pydantic схеми
├── frontend/
│   ├── index.html           # Головна сторінка тесту
│   └── teacher.html         # Панель вчителя
├── Dockerfile               # Docker конфігурація
├── render.yaml              # Render конфігурація
└── requirements.txt         # Python залежності
```

---

## 🎯 Функціонал

### Для учнів:
- Реєстрація за іменем
- 5 тестів з різними темами
- 45 запитань + написання листа
- Таймер для кожної частини
- Миттєва перевірка з результатами
- Аналіз помилок з поясненнями

### Для вчителів:
- Перегляд усіх результатів
- Фільтри по тестах, статусі, імені
- Детальний аналіз помилок кожного учня
- Експорт результатів у CSV
- Статистика по класу

---

## 🆘 Підтримка

Якщо виникли питання:
1. Перевірте **API Docs**: `https://ВАШ_ДОМЕН/docs`
2. Перевірте логи на Render: **Logs** вкладка
3. Переконайтеся що база даних підключена

---

## 📝 Ліцензія

Цей проект створено для освітніх цілей.

---

**Успіхів у вивченні німецької! 🇩🇪**
