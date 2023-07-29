from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from typing import Tuple, Dict
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import MessagesPlaceholder

from sql_analyzer.config import cfg
from sql_analyzer.log_init import logger


def setup_memory() -> Tuple[Dict, ConversationBufferMemory]:
    """
    Sets up memory for the open ai functions agent.
    :return a tuple with the agent keyword pairs and the conversation memory.
    """
    agent_kwargs = {
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    }
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)

    return agent_kwargs, memory


def init_sql_db_toolkit() -> SQLDatabaseToolkit:
    db = SQLDatabase.from_uri(cfg.db_uri)
    toolkit = SQLDatabaseToolkit(db=db, llm=cfg.llm)
    return toolkit


def initialize_agent(toolkit: SQLDatabaseToolkit) -> AgentExecutor:
    agent_executor = create_sql_agent(
        llm=cfg.llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=setup_memory()
    )
    return agent_executor


def agent_factory() -> AgentExecutor:
    sql_db_toolkit = init_sql_db_toolkit()
    return initialize_agent(sql_db_toolkit)


if __name__ == "__main__":
    agent_executor = agent_factory()
    result = agent_executor.run("Describe all tables")
    logger.info("Result: %s", logger)
