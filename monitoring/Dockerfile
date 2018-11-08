FROM python:3.6.6-slim-jessie

COPY requirements.txt .
COPY server_checker.py /usr/local/bin/.

RUN chmod +x /usr/local/bin/server_checker.py
RUN pip3 install -r requirements.txt

CMD python3 /usr/local/bin/server_checker.py

