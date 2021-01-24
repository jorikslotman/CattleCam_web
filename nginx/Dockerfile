FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

USER root

# for static and media folder
RUN mkdir -p /vol
RUN chmod 755 /vol

RUN mkdir -p /etc/letsencrypt/live/
RUN chown nginx:nginx /etc/letsencrypt/live/
RUN chmod 755 /etc/letsencrypt/live/

USER nginx