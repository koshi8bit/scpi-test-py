FROM python:3.10

ENV TZ="Etc/GMT-7"

RUN mkdir -p /usr/src/app/src
WORKDIR /usr/src/app/

COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt


COPY ./src /usr/src/app/src

CMD ["python", "src/main.py"]