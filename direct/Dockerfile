FROM python:3

MAINTAINER Antonio Gutierrez <chibby0ne@gmail.com>

WORKDIR /usr/src/app

COPY common/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["../common/entrypoint.sh"]

CMD ["python", "consumer.py"]
