FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]