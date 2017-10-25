FROM nginx:mainline

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip

#COPY nginx.conf /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/sites-enabled/manager_nginx.conf

RUN pip3 install django uwsgi

WORKDIR /var/local/manager
COPY . /var/local/manager

#COPY ./views /usr/share/nginx/html/
#WORKDIR /usr/share/nginx/html

RUN python3 manage.py collectstatic

WORKDIR /run/nginx

#CMD ["nginx", "-g", "daemon off;"]
#CMD ["uwsgi", "--http :22222", "--module manager.wsgi"]
#CMD ["uwsgi", "--socket :22222", "--module manager.wsgi"]
CMD ["uwsgi", "--ini uwsgi.ini", "--socket :22222"]


