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

RUN mkdir /app
# copy project
COPY . /app
WORKDIR /app
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/static
RUN mkdir -p /vol/web/media

RUN adduser -D user
run chown -R user:user /vol
run chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]