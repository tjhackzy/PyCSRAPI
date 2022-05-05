
FROM alpine:edge
FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add openssl
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD ["app_api1.py" ]
