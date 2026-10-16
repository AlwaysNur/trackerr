FROM python:slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY trackerr ./trackerr
COPY boot.sh .

RUN chmod +x boot.sh

ENV FLASK_APP=trackerr.backend.trackerr

EXPOSE 5450

ENTRYPOINT ["./boot.sh"]