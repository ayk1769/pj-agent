"""エージェントの基本実装."""

class Agent:
    """基本的なエージェントクラス."""
    
    def __init__(self, name="Agent"):
        """
        エージェントを初期化します。
        
        Args:
            name (str): エージェントの名前
        """
        self.name = name
        self.state = {}
    
    def act(self, observation):
        """
        観測に基づいて行動を実行します。
        
        Args:
            observation: 環境からの観測
            
        Returns:
            action: 実行するアクション
        """
        # 基本実装
        return {"type": "noop", "message": f"{self.name} is thinking..."}
    
    def update_state(self, key, value):
        """
        エージェントの内部状態を更新します。
        
        Args:
            key: 状態の識別子
            value: 状態の新しい値
        """
        self.state[key] = value
        
    def get_state(self, key, default=None):
        """
        エージェントの内部状態を取得します。
        
        Args:
            key: 状態の識別子
            default: キーが存在しない場合のデフォルト値
            
        Returns:
            value: 状態の値
        """
        return self.state.get(key, default)
