# syntax=docker/dockerfile:1
FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 80
CMD python3 get-count-hit-ip.py