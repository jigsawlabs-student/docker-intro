FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]


