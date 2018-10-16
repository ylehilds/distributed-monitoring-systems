#!/usr/bin/env python

import time
import requests
import logging
import click
from datetime import datetime
from data_processor import DataProcessor

from __future__ import print_function
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.types as sqltypes
import uuid


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

    # set up cockroachdb client
    Base = declarative_base()

    class Metrics(Base):
        __tablename__ = 'metrics'
        id = Column(sqltypes.VARCHAR, primary_key=True)
        ip = Column(sqltypes.VARCHAR)
        metric_name = Column(sqltypes.VARCHAR)
        labels = Column(sqltypes.JSON)
        metric_value = Column(sqltypes.FLOAT)

    engine = create_engine(
        'cockroachdb://maxroach@192.168.99.100:31997/prometheus')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # set up processor
    data_processor = DataProcessor(logger)

    # ip string
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

        metrics_to_add = []
        for data_point in data:
            computer_ip = data_point["computer_ip"]
            metric_name = data_point["data_type"]
            metric_value = data_point["value"]
            del data_point["computer_id"]
            del data_point["data_type"]
            del data_point["value"]
            metrics_to_add.append(
                Metrics(
                    id=str(uuid.uuid4()),
                    ip=computer_id,
                    metric_name=metric_name,
                    metric_value=metric_value,
                    labels=json.dumps(data_point)))
        session = Session()
        session.add_all(metrics_to_add)
        session.commit()

        logger.info("Added data!")
        time.sleep(30)


if __name__ == "__main__":
    main()
