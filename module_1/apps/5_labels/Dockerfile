FROM python:3

ADD labels.py /

RUN pip install prometheus_client

EXPOSE 8001
EXPOSE 8000

CMD [ "python3", "./labels.py" ]
