#!/usr/bin/env python

import time
import requests
import logging
from datetime import datetime
from pymongo import MongoClient

folder = "/scraperlog/"
# folder = ""
filename = folder + "prometheus_scraping_{}.log".format(
    str(datetime.now()).replace(" ", "_").replace(":", "-"))
logging.basicConfig(
    filename=filename,
    filemode="a",
    format="%(asctime)s, %(msecs)d, %(name)s, %(levelname)s, %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO)
logger = logging.getLogger(__name__)

client = MongoClient("192.168.0.1", port=30001)
# client = MongoClient(port=30001)
db = client.business

while True:
    logger.info("Collecting data...") 
    
    try:
        r = requests.get("http://192.168.35.5:9182/metrics")
    except Exception as e:
        logger.info(e)
        break
    logger.info("Got request")
    data = []
    for line in r.text.split("\n"):
        data_point = {}
        if line.startswith("wmi_service_status"):

            data_string = line[18:]
            index = data_string.find("}")
            data_arr = data_string[1:index].split(",")

            for d in data_arr:
                d_split = d.split("=")
                data_point[d_split[0]] = eval(d_split[1])
            value = eval(data_string[index + 1:].strip())
            data_point["value"] = value
            data.append(data_point)

    logger.info("Placing data in db...")
    db.prometheus.insert_many(data)
    logger.info("Added data!")
    time.sleep(10)
   
   
