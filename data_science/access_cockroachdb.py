#!/usr/bin/env python

import requests
import click

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.types as sqltypes


@click.command()
@click.option("--ip", help="ip for connecting to the database")
@click.option("--port", help="port for database")
def main(ip, port):
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
        'cockroachdb://prom@{}:{}/prometheus'.format(ip, port))
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    result = engine.execute("select * from metrics limit 10")
    for metric in result:
        print(metric.id, metric.ip, metric.metric_name, metric.labels,
              metric.metric_value)


if __name__ == "__main__":
    main()
