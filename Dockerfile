

FROM python:3

WORKDIR /RSD

COPY requirements.txt /RSD/

RUN  pip3 install -r requirements.txt

COPY . /RSD/
CMD [ "python3","manage.py","runserver","0.0.0.0:8000" ]

EXPOSE 8000
