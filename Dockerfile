FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/e-commerce


COPY requirements.txt /usr/src/requirements.txt
RUN pip3 install -r /usr/src/requirements.txt

COPY . /usr/src/e-commerce

EXPOSE 8000
# CMD [ "python3", "manage.py" , "migrate"]
CMD [ "python3", "manage.py" , "runserver", "0.0.0.0:8000"]