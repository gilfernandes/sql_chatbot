from sql_analyzer.agent_factory import agent_factory
from sql_analyzer.log_init import logger
from prompt_toolkit import HTML, PromptSession
from prompt_toolkit.history import FileHistory

_TEXT_COLOR_MAPPING = {
    "blue": "36;1",
    "yellow": "33;1",
    "pink": "38;5;200",
    "green": "32;1",
    "red": "31;1",
}


def get_colored_text(text: str, color: str) -> str:
    """Get colored text."""
    color_str = _TEXT_COLOR_MAPPING[color]
    return f"\u001b[{color_str}m\033[1;3m{text}\u001b[0m"


if __name__ == "__main__":
    agent_executor = agent_factory()

    session = PromptSession(history=FileHistory(".agent-history-file"))
    while True:
        question = session.prompt(
            HTML("<b>Type <u>Your question</u></b>  ('q' to exit): ")
        )
        if question.lower() in ["q", "exit"]:
            break
        if len(question) == 0:
            continue
        try:
            logger.info(get_colored_text(agent_executor.run(question), "green"))
        except Exception as e:
            logger.info(
                get_colored_text("Error occurred in agent", "red"),
                get_colored_text(str(e), "red"),
            )
