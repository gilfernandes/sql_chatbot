import os

from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv
from sql_analyzer.log_init import logger

load_dotenv()


class Config:
    # model = "gpt-3.5-turbo-16k-0613"
    model = "gpt-4-0613"
    llm = ChatOpenAI(model=model, temperature=0)
    db_uri = os.getenv("DB_CONNECTION_STRING")


cfg = Config()

if __name__ == "__main__":
    logger.info("LLM %s", cfg.llm)
    logger.info("db_uri %s", cfg.db_uri)
