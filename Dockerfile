FROM python:3.8-slim

WORKDIR /webtest

COPY . .

RUN pip install -r requirements.txt

CMD ["pytest"]
