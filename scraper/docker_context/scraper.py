#!/usr/bin/env python

import time
import json
import requests
import click
from datetime import datetime
from data_processor import DataProcessor

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.types as sqltypes
import uuid


@click.command()
@click.option("--ip", help="ip for prometheus scraping")
@click.option("--database-ip", help="ip for connecting to the database")
def main(ip, database_ip):
    # set up cockroachdb client
    Base = declarative_base()

    class Metrics(Base):
        __tablename__ = 'metrics'
        id = Column(sqltypes.VARCHAR, primary_key=True)
        ip = Column(sqltypes.VARCHAR)
        time = Column(sqltypes.VARCHAR)
        metric_name = Column(sqltypes.VARCHAR)
        labels = Column(sqltypes.JSON)
        metric_value = Column(sqltypes.FLOAT)

    engine = create_engine(
        'cockroachdb://prom@{}/prometheus'.format(database_ip))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # set up processor
    data_processor = DataProcessor(None)

    # ip string
    collection = ip.split(".")[2]

    # main loop
    while True:
        try:
            r = requests.get("http://{}:9182/metrics".format(ip))
        except Exception as e:
            break
        data = []
        for line in r.text.split("\n"):
            data_point = data_processor.process_line(ip, line)
            if data_point is not None:
                data.append(data_point)

        metrics_to_add = []
        for data_point in data:
            computer_ip = data_point["computer_ip"]
            metric_name = data_point["data_type"]
            metric_value = data_point["value"]
            del data_point["computer_ip"]
            del data_point["data_type"]
            del data_point["value"]
            metrics_to_add.append(
                Metrics(
                    id=str(uuid.uuid4()),
                    ip=computer_ip,
                    time=str(datetime.now()),
                    metric_name=metric_name,
                    metric_value=metric_value,
                    labels=json.dumps(data_point)))
    
    
        session = Session() 
        session.add_all(metrics_to_add)
        session.commit()
        session.close()

        time.sleep(60)


if __name__ == "__main__":
    main()
