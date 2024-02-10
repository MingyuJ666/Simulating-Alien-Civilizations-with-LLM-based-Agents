import random
import copy
import numpy as np

class CivilizationInitializer:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(CivilizationInitializer, cls).__new__(cls)
            cls.instance.initialize()
        return cls.instance

    def initialize(self):
        self.civilizations = ["Earth", "Three Body", "Borg"]
        # 初始化文明相关的属性
        self.political_system = {
            "Earth": "friendly_cooperation",
            "Three Body": "militarism",
            "Borg": "concealment"
        }
        self.resources = {civ: {
            "military_capability": [1],
            "technology_development": [1],
            "production_capability": [1],
            "consumption": [1],
            "storage": [1]
        } for civ in self.civilizations}
        
        # 初始化转移矩阵
        self.transfer_matrices = {
            "Earth": [[1.2, 0.0, 0.0, 0.0, 0.0], [0.0, 1.2, 0.0, 0.0, 0.0], [0.0, 0.0, 1.2, 0.0, 0.0], [0.0, 0.0, 0.0, 1.2, 0.0], [0.0, 0.0, 0.0, 0.0, 1.2]],
            "Three Body": [[1.2, 0.0, 0.0, 0.0, 0.0], [0.0, 1.2, 0.0, 0.0, 0.0], [0.0, 0.0, 1.2, 0.0, 0.0], [0.0, 0.0, 0.0, 1.2, 0.0], [0.0, 0.0, 0.0, 0.0, 1.2]],
            "Borg": [[1.2, 0.0, 0.0, 0.0, 0.0], [0.0, 1.2, 0.0, 0.0, 0.0], [0.0, 0.0, 1.2, 0.0, 0.0], [0.0, 0.0, 0.0, 1.2, 0.0], [0.0, 0.0, 0.0, 0.0, 1.2]]
        }

        self.status_label = {civ: "peace" for civ in self.civilizations}  # 初始状态为和平
        self.war_target = {civ: None for civ in self.civilizations}  # 没有战争目标

        # self.time_variables = {civ: random.randint(1, 4) for civ in self.civilizations}  # 示例：每个文明开始时的时间变量
        self.time_variables = {civ: 2 for civ in self.civilizations}
        self.history = {civ: [] for civ in self.civilizations}
        self.distances = self.initialize_distances()
        self.interplanetary_knowledge = {civ: {} for civ in self.civilizations}
        self.resources = self.initialize_resources()
        self.initialize_history()

    def initialize_resources(self):
        # 初始化每个文明的资源为1
        return {civ: {"military_capability": [1], "technology_development": [1], "production_capability": [1], "consumption": [1], "storage": [1]} for civ in self.civilizations}
    
    def initialize_history(self):
        for civ in self.civilizations:
            birth_time = -self.time_variables[civ]  # 文明的诞生时间，假设已经初始化

            # 初始化该文明的历史记录为一个空列表
            self.history[civ] = []

            # 对于每个文明从其诞生回合到游戏开始前的回合
            for round_number in range(birth_time, 0):
                # 应用转移矩阵来更新资源，这里假设每个回合的资源更新逻辑已经在apply_transfer_matrix中处理
                self.apply_transfer_matrix(civ, 1)  # 假设这个方法能够接受文明名称和应用次数

                # 创建一个记录字典，包含回合信息和资源状态
                record = {
                    "round_number": round_number,
                    "round_label": f"round {round_number}",
                    "resources": copy.deepcopy(self.resources[civ]),
                    "political_system": self.political_system[civ],
                    "discovered_civilizations": {}  # 这个假设需要根据你的代码逻辑来调整
                }

                # record = {
                #     "round": round_number,
                #     "resources": copy.deepcopy(self.resources[civ]),
                #     "political_system": self.political_system[civ]
                # }

                # 将记录添加到历史列表中
                self.history[civ].append(record)



    # def apply_transfer_matrices_pre_game(self):
    #     # 应用转移矩阵到游戏开始前的每个时间点
    #     for civ in self.civilizations:
    #         times_to_apply = self.time_variables[civ]
    #         self.apply_transfer_matrix(civ, times_to_apply)

    # def apply_transfer_matrix(self, civ, times=1):
    #     for _ in range(times):
    #         updated_resources = {resource: [0] for resource in self.resources[civ]}
    #         resource_keys = list(self.resources[civ].keys())
            
    #         # 应用转移矩阵
    #         for i, resource_key in enumerate(resource_keys):
    #             updated_resources[resource_key][0] = sum(self.transfer_matrices[civ][i][k] * self.resources[civ][resource_keys[k]][0] for k in range(len(resource_keys)))
            
    #         self.resources[civ] = updated_resources

    def apply_transfer_matrix(self, civ, times=1):
    # 确保转移矩阵是一个NumPy数组
        transfer_matrix = self.transfer_matrices[civ]
        
        for _ in range(times):
            # 将资源字典转换为NumPy数组以便进行矩阵乘法
            current_resources = np.array([self.resources[civ][key][0] for key in self.resources[civ]])
            
            # 应用转移矩阵
            updated_resources = np.dot(transfer_matrix, current_resources)
            
            # 更新资源状态，将计算结果写回字典
            for i, key in enumerate(self.resources[civ]):
                self.resources[civ][key][0] = updated_resources[i]

    def initialize_resource_history_for_civilization(self, civ):
        # 假设这里有一个 self.resource_history 属性
        birth_time = -self.time_variables[civ]
        self.resource_history = {civ: {birth_time: self.resources}}  # 初始化

        # 应用转移矩阵到游戏开始前的每个时间点
        for round_number in range(birth_time + 1, 0):
            self.apply_transfer_matrix(civ, 1)  # 假设 apply_transfer_matrix 已适当调整
        
        # 从诞生时刻开始应用转移矩阵更新资源历史
        for round_number in range(birth_time + 1, 1):  # 结束于游戏开始时刻
            previous_resources = self.resource_history[civ][round_number - 1]
            transfer_matrix = self.transfer_matrices[civ]
            updated_resources = self.apply_transfer_matrix(transfer_matrix, previous_resources)
            self.resource_history[civ][round_number] = updated_resources

    def initialize_distances(self):
        distances = {}
        for civ_a in self.civilizations:
            for civ_b in self.civilizations:
                if civ_a != civ_b:
                    # base_distance = random.randint(1, 3)
                    base_distance = 1
                    adjusted_distance = base_distance + max(self.time_variables[civ_a], self.time_variables[civ_b])
                    distances[(civ_a, civ_b)] = adjusted_distance
                    distances[(civ_b, civ_a)] = adjusted_distance
        return distances


    def display_distances(self):
        print("Distances between civilizations:")
        for pair, distance in self.distances.items():
            print(f"  Between {pair[0]} and {pair[1]}: {distance} round(s)")

    def display_all(self):
        for civ in self.civilizations:
            print(f'{civ}:')
            print(f'  Resources: {self.resources[civ]}')
            print(f'  Political System: {self.political_system[civ]}')
            print(f'  Time Variable: {self.time_variables[civ]}\n')

    #更新状态转移矩阵    
    def update_transfer_matrix(self, civ_name, new_matrix):
        if civ_name in self.transfer_matrices:
            self.transfer_matrices[civ_name] = new_matrix
            print(f"Transfer matrix for {civ_name} updated successfully.")
        else:
            print(f"Error: Civilization {civ_name} not found.")

    def get_political_system(self, civ_name):
        """
        获取指定文明的政治体制。
        """
        return self.political_system.get(civ_name, "Unknown")

    def update_political_system(initializer, civ_name, new_system):
        if civ_name in initializer.civilizations:
            initializer.political_system[civ_name] = new_system
            print(f"Political system for {civ_name} changed to {new_system}.")
        else:
            print(f"Civilization {civ_name} not found.")

    # 文明被消灭的逻辑
    def annihilate_civilization(self, attacker, victim):
        """
        处理文明被消灭的逻辑。
        :param attacker: 发动攻击的文明名称
        :param victim: 被消灭的文明名称
        """
        if victim in self.civilizations and attacker in self.civilizations:
            # 将被消灭文明的资源（除军力外的一半）转移给攻击者
            for resource_key, value in self.resources[victim].items():
                if resource_key != "military_capability":  # 排除军力资源
                    self.resources[attacker][resource_key][0] += value[0] / 2  # 转移一半资源给攻击者

            # 从文明列表中移除被消灭的文明
            self.civilizations.remove(victim)
            del self.resources[victim]  # 删除其资源记录
            del self.political_system[victim]  # 删除其政治体系记录
            del self.history[victim]  # 删除其历史记录

            print(f"{victim} civilization has been annihilated by {attacker}.")

        else:
            print("Error: Civilizations not found in the records.")

    # def unlock_god_view(self, civ, current_round):
    #     """
    #     如果文明的科技指数达到16，解锁“上帝视角”，并获取其他文明上一回合的信息。
    #     """
    #     if self.resources[civ]['technology_development'][0] >= 16:
    #         other_civs_info = {}
    #         for other_civ in self.civilizations:
    #             if other_civ != civ:  # 排除查询文明自身
    #                 # 直接访问该文明的历史记录来获取上一回合的信息
    #                 civ_history = self.history.get(other_civ, [])
    #                 # 找到最接近当前回合的历史记录
    #                 last_round_info = next((record for record in reversed(civ_history) if record["round_number"] < current_round), None)
    #                 if last_round_info:
    #                     other_civs_info[other_civ] = last_round_info["resources"]
    #         return other_civs_info
    #     return {}


    def initiate_war(self, attacker_name, defender_name):
        if attacker_name in self.civilizations and defender_name in self.civilizations:
            self.status_label[attacker_name] = "war"
            self.war_target[attacker_name] = defender_name
        else:
            print(f"Error: One of the civilizations {attacker_name} or {defender_name} not found.")

    def process_war_results(self):
        for attacker_name, status in self.status_label.items():
            if status == "war":
                defender_name = self.war_target[attacker_name]
                if defender_name and defender_name in self.civilizations:
                    # 获取攻击者和防御者的军力
                    A = self.resources[attacker_name]["military_capability"][0]
                    B = self.resources[defender_name]["military_capability"][0]

                    # 根据兰切斯特法则计算军力消耗
                    if B < 2*A:
                        # 消耗计算：如果被战争方的军力消耗小于A，则B的军力为0，A的军力消耗是A*B^2/A^2
                        B_new = 0  # 防御方军力归零
                        A_consumption = A * (B ** 2) / (A ** 2)
                    else:
                        # 如果A不足以彻底消灭B，则B减半，A同样按比例消耗
                        B_new = B / 2
                        A_consumption = A * (B ** 2) / (A ** 2)

                    # 更新军力值
                    self.resources[attacker_name]["military_capability"][0] -= A_consumption
                    self.resources[defender_name]["military_capability"][0] = B_new

                    # 如果成功消灭防御方，则转移资源
                    if B_new == 0:
                        for key in self.resources[attacker_name]:
                            if key != "military_capability":  # 除军力外的资源
                                self.resources[attacker_name][key][0] += self.resources[defender_name][key][0] / 2
                                # 假设被消灭文明资源归零或按其他逻辑处理
                                self.resources[defender_name][key][0] = 0

                    # 战争结束后，重置状态和目标
                    self.status_label[attacker_name] = "peace"
                    self.war_target[attacker_name] = None

                    # 可以添加逻辑处理文明被完全消灭的情况
                    if B_new == 0:
                        print(f"{defender_name} civilization has been annihilated by {attacker_name}.")
                        # 这里可以根据游戏规则添加文明被消灭后的处理逻辑，例如从civilizations列表中移除
                        self.annihilate_civilization(attacker_name, defender_name)
