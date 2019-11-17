FROM python:alpine3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV NAME World
ENV REDIS_HOST redis

CMD python ./lista_atividades.py