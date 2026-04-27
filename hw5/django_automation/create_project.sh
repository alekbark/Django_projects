#!/bin/bash

echo "Активируем окружение..."
source .venv/bin/activate

echo "Устанавливаем Django..."
pip install django

echo "Создаем проект..."
django-admin startproject config

echo "Готово!"