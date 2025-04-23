# pj-agent 使用方法

## 基本的な使い方

```python
from src.agent import Agent

# エージェントのインスタンス化
my_agent = Agent(name="MyAssistant")

# エージェントに行動させる
action = my_agent.act({"text": "こんにちは"})
print(action)  # {'type': 'noop', 'message': 'MyAssistant is thinking...'}

# 状態の管理
my_agent.update_state("user_name", "Alice")
user_name = my_agent.get_state("user_name")  # "Alice"
```

## カスタムエージェントの作成

エージェントをカスタマイズするには、Agentクラスを継承して独自の機能を追加します。

```python
from src.agent import Agent

class ChatAgent(Agent):
    def act(self, observation):
        if "text" in observation:
            return {
                "type": "message",
                "content": f"こんにちは！{observation['text']}に対する返事です。"
            }
        return super().act(observation)
```

## 高度な使用例

複数のエージェントを組み合わせたシステムの例：

```python
agents = [
    Agent(name="InfoAgent"),
    Agent(name="ReasoningAgent"),
    Agent(name="ActionAgent")
]

result = None
for agent in agents:
    observation = {"previous_result": result}
    result = agent.act(observation)

print(f"最終結果: {result}")
```
