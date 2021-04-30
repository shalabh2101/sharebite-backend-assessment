FROM ubuntu:latest

WORKDIR /apis

RUN apt-get update && apt-get upgrade -y

RUN apt-get install python3-pip -y

RUN apt-get install libmysqlclient-dev -y

COPY apis /apis/apis

COPY shalabh /apis/shalabh

COPY manage.py /apis

COPY requirements.txt /apis

RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver"]