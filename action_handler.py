from diplomatic import *

class ActionHandler:
    diplomatic_relations = DiplomaticRelations()
    def __init__(self, diplomatic_relations, civilization_initializer):
        self.diplomatic_relations = diplomatic_relations
        self.civilization_initializer = civilization_initializer

    def handle_public_action(self, civ_name, target_civ_name, action):
        if action == "express_friendliness":
            self.diplomatic_relations.update_feeling(civ_name, target_civ_name, "favorable")
            print(f"{civ_name} expresses friendliness towards {target_civ_name}.")

        elif action == "initiate_cooperation":
            self.diplomatic_relations.update_relations(civ_name, target_civ_name, "cooperative")
            # 可能需要在这里或在外部调整转移矩阵
            print(f"{civ_name} initiates cooperation with {target_civ_name}.")

        elif action == "launch_annihilation_war":
            # 检查并执行战争逻辑，可能需要访问更多的游戏状态信息
            print(f"{civ_name} attempts to launch annihilation war against {target_civ_name}.")
            # 实施战争的具体逻辑在这里省略

        elif action == "reject_cooperation":
            self.diplomatic_relations.update_relations(civ_name, target_civ_name, "non-cooperative")
            print(f"{civ_name} rejects cooperation with {target_civ_name}.")

    def handle_private_action(self, civ_name, action):
        if action == "mobilize_for_war":
            # 更新文明的军事准备状态
            self.civilization_initializer.update_military_status(civ_name, "mobilized")
            print(f"{civ_name} mobilizes for war.")
