#!/bin/bash

echo "Активируем окружение..."
source .venv/bin/activate

echo "Сохраняем зависимости..."
pip freeze > requirements.txt

echo "Готово!"