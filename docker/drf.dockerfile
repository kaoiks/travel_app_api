FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY docker/requirements.txt .

# install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /code

COPY . .

# copy django scripts
COPY docker/scripts/* /usr/local/bin/

RUN python manage runserver 0.0.0.0:8000

LABEL maintainer jakub-mrow
LABEL Project=django-skeleton