FROM python:3.6.2-alpine

ENV workdir=/opt/promsnaps
RUN apk --no-cache --update add openssl ca-certificates
RUN apk --no-cache add --virtual build-dependencies \
    libffi-dev build-base openssl-dev bash git
RUN pip install pip -U
RUN rm -rf $workdir
RUN mkdir -p $workdir
COPY . $workdir
WORKDIR $workdir
RUN pip install gunicorn gevent -U && pip install -e .

CMD ["./run-server.sh"]
