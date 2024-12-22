release: |
  pip3 install -r requirements.txt
z  python3 manage.py makemigrations
  python3 manage.py migrate

web: gunicorn JaWa.wsgi
