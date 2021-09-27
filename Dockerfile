FROM python:3.9.0

WORKDIR /home/

RUN echo "tefff2s24afa222hfn"

RUN git clone https://github.com/IHAGI-c/super-system.git

WORKDIR /home/super-system/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=GIS_class2_2.settings.deploy && python manage.py collectstatic --noinput --settings=GIS_class2_2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=GIS_class2_2.settings.deploy GIS_class2_2.wsgi --bind 0.0.0.0:8000"]