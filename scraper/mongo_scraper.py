#!/usr/bin/env python

import time
import requests
import logging
import click
from datetime import datetime
from pymongo import MongoClient
from data_processor import DataProcessor


@click.command()
@click.option("--ip", help="ip for prometheus scraping")
def main(ip):
    # set up logger
    folder = "/scraperlog/"
    filename = folder + "prometheus_scraping_{}_{}.log".format(
        ip,
        str(datetime.now()).replace(" ", "_").replace(":", "-"))
    logging.basicConfig(
        filename=filename,
        filemode="a",
        format="%(asctime)s, %(msecs)d, %(name)s, %(levelname)s, %(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # set up mongo client
    client = MongoClient("192.168.0.1", port=30001)
    db = client.business

    # set up processor
    data_processor = DataProcessor(logger)

    # ip string
    # ip = "192.168.35.5"
    collection = ip.split(".")[2]

    # main loop
    while True:
        logger.info("Collecting data...")

        try:
            r = requests.get("http://{}:9182/metrics".format(ip))
        except Exception as e:
            logger.info(e)
            break
        logger.info("Got request")
        data = []
        for line in r.text.split("\n"):
            data_point = data_processor.process_line(ip, line)
            if data_point is not None:
                data.append(data_point)

        logger.info("Placing data in db...")
        db.prometheus[collection].insert_many(data)
        logger.info("Added data!")
        time.sleep(10)


if __name__ == "__main__":
    main()
