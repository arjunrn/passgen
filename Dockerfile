FROM python:3.6-slim-stretch

COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir -p /opt/app
COPY main.py /opt/app 
COPY passgen.py /opt/app
WORKDIR /opt/app
CMD ["python", "main.py"] 