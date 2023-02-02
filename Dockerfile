FROM python:3.10-alpine
LABEL maintainer="qingcaomc@gmail.com"

COPY . /QCMCSign/
WORKDIR /QCMCSign
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip config set install.trusted-host mirrors.aliyun.com \
    && pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port 8000