FROM python:3.8

ENV PYTHONUNBUFFERD=1

WORKDIR /code

RUN apt-get update
RUN apt-get upgrade
RUN apt-get install fish -y
RUN apt-get install htop
RUN apt-get install nano
RUN apt-get install sqlite3
RUN apt-get install gdal-bin -y

COPY Pipfile.lock /code/

RUN pip install --upgrade pip
RUN pip install pipenv-to-requirements
RUN pipenv_to_requirements --freeze
RUN pip install -r requirements.txt

COPY . /code/

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
