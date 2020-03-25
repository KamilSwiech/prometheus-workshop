FROM python:3

ADD sum.py /

RUN pip install prometheus_client

EXPOSE 8001
EXPOSE 8000

CMD [ "python3", "./sum.py" ]
