FROM python:3
MAINTAINER Subhrajyoti Sen "subhrajyoti12@gmail.com"

COPY . /bot

WORKDIR /bot

RUN pip install -r requirements.txt

CMD [ "python3", "main.py" ]
