FROM python:3.6.6-slim-jessie

COPY requirements.txt .
COPY scraper.py /usr/local/bin/.
COPY data_processor.py /usr/local/bin/.

RUN chmod +x /usr/local/bin/scraper.py
RUN pip3 install -r requirements.txt

CMD python3 /usr/local/bin/scraper.py --ip $IP --database-ip $DATABASEIP

