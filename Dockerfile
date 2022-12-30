# Устанавка базового образ
FROM python:3.10-alpine

# Устанавка рабочего директория внутри контейнера
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt /app/requirements.txt

# Установка зависимостей
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install webdriver-manager

# Копирование остальных файлов проекта
COPY . /app

## Запуск тестов
CMD ["pytest"]
