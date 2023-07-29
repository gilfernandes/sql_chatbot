import chainlit as cl

from sql_analyzer.mysql_analyzer import agent_factory
from langchain.agents import AgentExecutor

@cl.on_chat_start
def start():
    agent_executor = agent_factory()
    cl.user_session.set("agent", agent_executor)


@cl.on_message
async def main(message):
    agent: AgentExecutor = cl.user_session.get("agent")
    cb = cl.LangchainCallbackHandler(stream_final_answer=True)

    resp = await cl.make_async(agent.run)(message, callbacks=[cb])
    geo_location_msg = cl.Message(content=resp)
    await geo_location_msg.send()

