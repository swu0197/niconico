"""LangGraph single-node graph template.

Returns a predefined response. Replace logic and configuration as needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph, add_messages

from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
from typing import Annotated, TypedDict

from langgraph_sdk import get_client
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

class Configuration(TypedDict):
    """Configurable parameters for the agent.

    Set these when creating assistants OR when invoking the graph.
    See: https://langchain-ai.github.io/langgraph/cloud/how-tos/configuration_cloud/
    """

    my_configurable_param: str


@dataclass
class State(TypedDict):
    """Input state for the agent.

    Defines the initial structure of incoming data.
    See: https://langchain-ai.github.io/langgraph/concepts/low_level/#state
    """
    # messages: Annotated[list, add_messages]
    messages: str


class WeatherResponse(BaseModel):
    conditions: str

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 定義: ユーザーのクエリを大規模言語モデルで処理する関数
async def call_model(state: State, config: RunnableConfig):
# async def call_model(state: State, config: RunnableConfig) -> Dict[str, Any]:
    """Process input and returns output.

    Can use runtime configuration to alter behavior.
    """
    # configuration = config["configurable"]
    # return {
    #     "changeme": "output from call_model. "
    #     f'Configured with {configuration.get("my_configurable_param")}'
    # }


    print("Writing...")

    model = AzureChatOpenAI(
        deployment_name=os.getenv("DEPLOYMENT_LLM_NAME"),
        temperature=0,
    )

    checkpointer = InMemorySaver()

    agent = create_react_agent(
        model=model,
        tools=[get_weather],
        prompt="You are a helpful assistant",
        # checkpointer=checkpointer,
        # response_format=WeatherResponse
    )
    # config = {"configurable": {"thread_id": "1"}}
    messages = state["messages"] # 明日は晴れですか？
    response = await agent.ainvoke(
        # {"messages": messages},
        [{"role": "user", "content": messages}],
        config
    )
    return {"messages": response.}
    # return {"messages": response["structured_response"]}


# メインアシスタントの基本グラフを定義
graph = (
    StateGraph(State, config_schema=Configuration)
    .add_node(call_model)
    .add_edge("__start__", "call_model")
    .add_edge("call_model", "__end__")
    .compile(name="New Graph")
    # .get_graph().print_ascii()
)
# graph.get_graph().print_ascii()
