# Базовый образ с Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt (если есть)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Запускаем скрипт
ENTRYPOINT ["python", "main.py"]
CMD ["--port", "8000"]