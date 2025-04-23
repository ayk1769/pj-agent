"""エージェントのテスト."""

import pytest
from src.agent import Agent

def test_agent_initialization():
    """エージェントの初期化テスト."""
    agent = Agent(name="TestAgent")
    assert agent.name == "TestAgent"
    assert agent.state == {}

def test_agent_state_management():
    """エージェントの状態管理テスト."""
    agent = Agent()
    
    # 状態の更新
    agent.update_state("location", "home")
    assert agent.get_state("location") == "home"
    
    # 存在しないキー
    assert agent.get_state("nonexistent") is None
    assert agent.get_state("nonexistent", "default") == "default"

def test_agent_action():
    """エージェントのアクションテスト."""
    agent = Agent(name="ActionAgent")
    action = agent.act({"type": "observation", "data": "nothing special"})
    
    assert "type" in action
    assert action["type"] == "noop"
    assert "message" in action
    assert agent.name in action["message"]
