# SQL Chain Playground

This project is a chatbot user interface which allows users to query a specific database using natural language.
It allows you to query in a technical, but also in a business like way.

So you can ask questions like e.g:

- Can you please show me all the indices used in this database?
- Which are the 5 most popular films?
- Which tables are referencing the actor table?

## Installation

```
conda create -n langchain_sql python=3.11
conda activate langchain_sql
pip install langchain
pip install prompt_toolkit
pip install openai
pip install python-dotenv
pip install mysqlclient
pip install chainlit
pip install geoalchemy2
# Support MySQL geometry types
pip install acryl-datahub
pip install black


pip install poetry
poetry install
```

This might be useful under Ubuntu
```
sudo apt install pkg-config
```

## Run Chainlit

For development:
```
chainlit run ./sql_analyzer/mysql_analyzer_chainlit.py --port 8082 -w
```

Normally:
```
chainlit run ./sql_analyzer/mysql_analyzer_chainlit.py --port 8083
```

## Notes on the Sakila DB

We have used for testing the Sakila database. However it seems that the SQLAlchemy package does not like the "geometry" data type and so
we more some data to a varchar datatype with these commands:

```SQL
alter table address add column point_location varchar(256);
update address set point_location = ST_AsText(location);
alter table address drop column location;
```