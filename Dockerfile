FROM alpine:3.23

WORKDIR /app
COPY . .

RUN apk update && apk add python3 py3-pip

RUN pip3 install -r requirements.txt --break-system-packages

CMD ["python3", "main.py"]