pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py makemigrations
python manage.py migrate
python manage.py import_products