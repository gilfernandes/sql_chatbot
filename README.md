# SQL Chain Playground


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

poetry install
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