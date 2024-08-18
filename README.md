## Esate Server


### Command
```
pip freeze > requirements.txt
docker compose up --build
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py fetch_apt_data
```
