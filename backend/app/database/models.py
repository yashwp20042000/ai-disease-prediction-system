from sqlalchemy import Table, Column, Integer, Float, MetaData

metadata = MetaData()

predictions = Table(
    "predictions",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("glucose", Float),
    Column("prediction", Integer),
)