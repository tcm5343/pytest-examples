
FROM python:3.13

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:./test:./src

WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY requirements-dev.txt ./requirements-dev.txt
RUN pip install -r requirements.txt -r requirements-dev.txt

ENTRYPOINT [ ]
