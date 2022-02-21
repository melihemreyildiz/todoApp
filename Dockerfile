FROM python:3.8-buster

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /backend
WORKDIR /backend/
RUN python manage.py migrate
RUN python manage.py makemigrations authentication todo
RUN python manage.py migrate
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]