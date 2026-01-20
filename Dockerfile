# что использует за сборку языка
FROM python:3.12-slim

WORKDIR /app

#устанавливаем системные зависимости
RUN apt-get update && apg-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/list/*

#копируем все зависимости проекта
COPY requirements.txt

#устанавливаем зависимости Python
RUN pip install --no--cashe-dir -r requiments.txt

#копируем сам проект
COPY src/app/src/

#порт на котором разворачивается
EXPOSE 8000

#команда запуска
CMD ['python','src/manage.py','runserver','0.0.0.0:8000']