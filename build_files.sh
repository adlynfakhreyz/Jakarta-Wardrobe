python3 -m venv env
pip3 install -r requirements.txt
python3 manage.py collectstatic --noinput --clear
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py import_products