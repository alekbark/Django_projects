#!/bin/bash

echo "Активируем окружение..."
source .venv/bin/activate

cd config || {
  echo "Папка config не найдена!"
  exit 1
}

echo "Запускаем сервер..."
python manage.py runserver