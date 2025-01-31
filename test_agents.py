import pytest
from unittest.mock import MagicMock
from Agents.ChatAgent import ChatAgent
from Agents.BlockAgent import BlockAgent
from Agents.AiAgent import GeminiAgent
from Agents.MockAgent import MockAgent
from MyAdventures.mcpi.vec3 import Vec3




def test_chat_agent_initialization():
    agent = ChatAgent("TestChatAgent")
    assert agent.name == "TestChatAgent"
    assert agent.mc is not None



