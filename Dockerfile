# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster
WORKDIR /text2pic
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /text2pic
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]