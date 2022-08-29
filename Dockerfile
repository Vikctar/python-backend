FROM python:3.10-slim

ENV FLASK_APP app.py
ENV FLASK_ENV production

COPY requirements.txt ./
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY app.py config.py boot.sh ./

EXPOSE 5000
CMD ./boot.sh