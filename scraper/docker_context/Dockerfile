FROM python:3.6.6-slim-jessie

COPY requirements.txt .
COPY scraper.py /usr/local/bin/.

RUN chmod +x /usr/local/bin/scraper.py
RUN pip3 install -r requirements.txt

CMD ["/usr/local/bin/scraper.py", "-OPTIONAL_FLAG"]

