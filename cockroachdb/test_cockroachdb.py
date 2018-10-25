from __future__ import print_function
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy.types as sqltypes
import uuid

Base = declarative_base()

class Metrics(Base):
    __tablename__ = 'metrics'
    id = Column(sqltypes.VARCHAR, primary_key=True)
    ip = Column(sqltypes.VARCHAR)
    metric_name = Column(sqltypes.VARCHAR)
    labels = Column(sqltypes.JSON)
    metric_value = Column(sqltypes.FLOAT)

# Create an engine to communicate` with the database. The "cockroachdb://" prefix
# for the engine URL indicates that we are connecting to CockroachDB.
engine = create_engine('cockroachdb://root@192.168.99.100:31683/prometheus')
Session = sessionmaker(bind=engine)

# Automatically create the "accounts" table based on the Account class.
Base.metadata.create_all(engine)

# Insert two rows into the "accounts" table.
session = Session()
session.add_all([
    Metrics(id=str(uuid.uuid4()), ip="127.0.0.1", metric_name="wmi", labels="{\"id\": 3}", metric_value=3.4)
])
session.commit()

# Print out the balances.
for metric in session.query(Metrics):
    print(metric.ip, metric.metric_name, metric.labels, metric.metric_value)
