FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY docker/requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /code

COPY . .

WORKDIR /code/src

LABEL maintainer jakub-mrow
LABEL Project=django-skeleton