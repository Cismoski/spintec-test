FROM python:3.9.7-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE spintectest.settings

RUN apt-get update --fix-missing
RUN apt-get -y install wait-for-it vim

RUN adduser --disabled-password --gecos '' spintectest && mkdir /code && chown -R spintectest /code
WORKDIR /code

USER spintectest
RUN pip install -U pip

COPY * /code/
RUN pip install -r requirements.txt

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000