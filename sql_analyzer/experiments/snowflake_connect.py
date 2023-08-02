from sqlalchemy import create_engine
from sqlalchemy import inspect
from snowflake.sqlalchemy import URL

engine = create_engine(
    URL(
        account="onepoint_partner",
        user="GIL.FERNENDES@ONEPOINTLTD.COM",
        password="Sarovar16108!",
        database="SNOWFLAKE_SAMPLE_DATA",
        schema="TPCDS_SF10TCL",
        warehouse="DEMO_WH",
        host="onepoint_partner.west-europe.azure.snowflakecomputing.com",
    )
)

connection = None
try:
    connection = engine.connect()
    results = connection.execute("select current_version()").fetchone()
    print(results[0])
finally:
    if connection is not None:
        connection.close()
        engine.dispose()
