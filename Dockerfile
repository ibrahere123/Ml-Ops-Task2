FROM python:3.9-slim

WORKDIR /app

COPY Requirments.txt /app/

RUN pip install --no-cache-dir  -r Requirments.txt

COPY . .

EXPOSE 500

ENV FLASK_APP = app/App.py

CMD ["flask","run","--host=0.0.0.0"] 
