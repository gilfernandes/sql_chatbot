# SQL Chain Playground

This project is a chatbot user interface which allows users to query a specific database using natural language.
It allows you to query in a technical, but also in a business like way.

So you can ask questions like e.g:

- Can you please show me all the indices used in this database?
- Which are the 5 most popular films?
- Which tables are referencing the actor table?

## Installation

```
# conda remove -n langchain_sql --all
conda create -n langchain_sql python=3.11
conda activate langchain_sql
pip install langchain
pip install prompt_toolkit
pip install openai
pip install mysqlclient
pip install chainlit
pip install geoalchemy2
# Support MySQL geometry types
pip install acryl-datahub
pip install black


pip install poetry
poetry install

```

### Snowflake

```
# conda activate base
# conda remove -n langchain_snowflake --all
conda create -n langchain_snowflake python=3.11
conda activate langchain_snowflake
pip install langchain
pip install snowflake-sqlalchemy
# pip install SQLAlchemy-Utils
pip install openai
pip install chainlit
# pip install black

# pip install poetry
# poetry install
```


To install as a package, please use:

```bash
pip install -e .
```

This might be useful under Ubuntu
```
sudo apt install pkg-config
```

## Run Chainlit

For development:
```
chainlit run ./sql_analyzer/mysql_analyzer_chainlit.py --port 8084 -w
```

Normally:
```
chainlit run ./sql_analyzer/mysql_analyzer_chainlit.py --port 8084
```

## Notes on the Sakila DB

We have used for testing the Sakila database. However it seems that the SQLAlchemy package does not like the "geometry" data type and so
we more some data to a varchar datatype with these commands:

```SQL
alter table address add column point_location varchar(256);
update address set point_location = ST_AsText(location);
alter table address drop column location;
```

## Notes on .env file

You will also need a `.env` file in the directory you are running this application as well as an installed MySQL database server with the Sakila database installed.

The .env file should have the following variables:

```
DB_CONNECTION_STRING=mysql+mysqldb://<user>:<password>@localhost/sakila
OPENAI_API_KEY=<openapi-key>

# Snowflake
SNOWFLAKE_ACCOUNT=****
SNOWFLAKE_USER=****
SNOWFLAKE_PASSWORD=****
SNOWFLAKE_DATABASE=SNOWFLAKE_SAMPLE_DATA
SNOWFLAKE_SCHEMA=TPCDS_SF10TCL
SNOWFLAKE_WAREHOUSE=DEMO_WH
SNOWFLAKE_HOST=****

SELECTED_DB=snowflake # snowflake or mysql
```