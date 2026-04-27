#!/bin/bash

echo "Создаем виртуальное окружение..."
python3 -m venv .venv

echo "Активируем..."
source .venv/bin/activate

echo "Готово!"
