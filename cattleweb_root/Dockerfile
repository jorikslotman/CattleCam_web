# pull official base image
FROM python:3.8.3-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 and uswgi dependencies
RUN apk add --update --no-cache --virtual .tmp postgresql-dev gcc python3-dev musl-dev libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /cattleweb
# copy project
COPY . /cattleweb
WORKDIR /cattleweb

COPY ./scripts /scripts

RUN adduser -D user

run chown user:user ./database/db.sqlite3
run chown user:user ./database 
run chmod 755 ./database
run chmod 755 ./database/db.sqlite3

RUN chmod +x /scripts/*

RUN mkdir -p /vol/cattleweb/static
RUN mkdir -p /vol/cattleweb/media

run chown -R user:user /vol
run chmod -R 755 /vol/cattleweb

USER user

CMD ["entrypoint.sh"]