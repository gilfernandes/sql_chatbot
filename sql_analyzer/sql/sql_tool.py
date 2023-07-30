from langchain.tools.sql_database.tool import BaseSQLDatabaseTool
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.tools.base import BaseTool
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from typing import Optional, List

class ListViewSQLDatabaseTool(BaseSQLDatabaseTool, BaseTool):
    """Tool for getting tables names."""

    name = "sql_db_list_views"
    description = "Input is an empty string, output is a comma separated list of views in the database."

    def _run(
        self,
        tool_input: str = "",
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Get the schema for a specific table."""
        return ", ".join(self.db._inspector.get_view_names())

    async def _arun(
        self,
        tool_input: str = "",
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        raise NotImplementedError("ListTablesSqlDbTool does not support async")
    


class ExtendedSQLDatabaseToolkit(SQLDatabaseToolkit):

    def get_tools(self) -> List[BaseTool]:
        base_tools = super(ExtendedSQLDatabaseToolkit, self).get_tools()
        list_views_tool = ListViewSQLDatabaseTool(db=base_tools[0].db)
        base_tools.append(list_views_tool)
        return base_tools