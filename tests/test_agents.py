import pytest
from unittest.mock import MagicMock
from Agents.ChatAgent import ChatAgent
from Agents.BlockAgent import BlockAgent
from Agents.AiAgent import GeminiAgent
from Agents.MockAgent import MockAgent
from MyAdventures.mcpi.vec3 import Vec3

@pytest.fixture
def mock_minecraft():
    """Creates a simulated Minecraft object with mocked methods."""
    mock_mc = MagicMock()
    mock_mc.events.pollChatPosts.return_value = []
    return mock_mc

