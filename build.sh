#!/usr/bin/env bash
# build.sh — runs during Railway deployment

set -o errexit

echo "==> Installing packages..."
pip install -r requirements.txt

echo "==> Running migrations..."
python manage.py migrate --noinput

echo "==> Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "==> Build done!"
