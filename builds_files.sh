pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python migrate_db.py