from diplomatic import DiplomaticRelations

class Board:
    def __init__(self):
        self.diplomatic_history = []  # 存储每一回合的 DiplomaticRelations 实例

    def update_round(self, diplomatic_relations=None):
        """
        更新当前回合的外交关系。
        如果当前回合没有文明间的交互，将存储一个默认的 DiplomaticRelations 实例，表示“no interaction between civilizations”。
        """
        if diplomatic_relations is None:
            # 创建一个表示无交互的 DiplomaticRelations 实例
            diplomatic_relations = DiplomaticRelations()
            diplomatic_relations.relations = {"default": "no interaction between civilizations"}
        self.diplomatic_history.append(diplomatic_relations)

    def get_round_diplomatic_relations(self, round_number):
        """
        获取指定回合的外交关系。
        """
        if 0 <= round_number < len(self.diplomatic_history):
            return self.diplomatic_history[round_number]
        else:
            return None  # 如果请求的回合数超出范围，返回 None

    def get_latest_diplomatic_relations(self):
        """
        获取最新回合的外交关系。
        """
        if self.diplomatic_history:
            return self.diplomatic_history[-1]
        else:
            return None
