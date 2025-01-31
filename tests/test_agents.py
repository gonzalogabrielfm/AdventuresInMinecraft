import pytest
from unittest.mock import MagicMock
from Agents.ChatAgent import ChatAgent
from Agents.BlockAgent import BlockAgent
from Agents.AiAgent import GeminiAgent
from Agents.MockAgent import MockAgent
from MyAdventures.mcpi.vec3 import Vec3


def test_mock_bot_initialization():
    agent = MockAgent()
    assert agent.name == "MockBot"


def test_chat_agent_initialization():
    agent = ChatAgent("TestBot")
    assert agent.name == "TestBot"


def test_block_agent_initialization():
    agent = BlockAgent("BlockBot", block_id=1)
    assert agent.name == "BlockBot"
    assert agent.block_id == 1


def test_mock_agent_listen():
    agent = MockAgent()
    # Mock the minecraft instance
    agent.mc = MagicMock()
    agent.mc.events.pollChatPosts.return_value = []

    # Test the listen method
    agent.listen()
    # Verify that pollChatPosts was called
    agent.mc.events.pollChatPosts.assert_called_once()