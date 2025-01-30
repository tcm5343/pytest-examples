
FROM python:3.13

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=$PYTHONPATH:./app/test:./app/src

WORKDIR /work

COPY ./app/requirements.txt ./requirements.txt
COPY ./app/requirements-dev.txt ./requirements-dev.txt
RUN pip install -r requirements.txt -r requirements-dev.txt

ENTRYPOINT [ ]
