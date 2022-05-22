FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /api

COPY requirements.txt /api/

RUN pip install -r requirements.txt

RUN apt-get update --yes --quiet 

# && apt-get install --yes --quiet --no-install-recommends \

COPY . /api/
