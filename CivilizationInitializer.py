import random
import copy

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
            "Earth": [[1.1, 1.05, 1.0, 1.0, 1.03], [1.05, 1.1, 1.0, 1.0, 1.02], [1.05, 1.1, 1.0, 1.0, 1.02], [1.05, 1.1, 1.0, 1.0, 1.02], [1.05, 1.1, 1.0, 1.0, 1.02]],
            "Three Body": [[1.2, 1.1, 1.05, 1.05, 1.0], [1.2, 1.1, 1.05, 1.05, 1.0], [1.2, 1.1, 1.05, 1.05, 1.0], [1.2, 1.1, 1.05, 1.05, 1.0], [1.2, 1.1, 1.05, 1.05, 1.0]],
            "Borg": [[1.15, 1.05, 1.1, 1.1, 1.05], [1.15, 1.05, 1.1, 1.1, 1.05], [1.15, 1.05, 1.1, 1.1, 1.05], [1.15, 1.05, 1.1, 1.1, 1.05], [1.15, 1.05, 1.1, 1.1, 1.05]]
        }
        self.time_variables = {civ: random.randint(1, 4) for civ in self.civilizations}  # 示例：每个文明开始时的时间变量
        self.history = {civ: [] for civ in self.civilizations}
        self.distances = self.initialize_distances()
        self.interplanetary_knowledge = {civ: {} for civ in self.civilizations}
        self.resources = self.initialize_resources()
        self.apply_transfer_matrices_pre_game()

    def initialize_resources(self):
        # 初始化每个文明的资源为1
        return {civ: {"military_capability": [1], "technology_development": [1], "production_capability": [1], "consumption": [1], "storage": [1]} for civ in self.civilizations}
    
    def apply_transfer_matrices_pre_game(self):
        # 应用转移矩阵到游戏开始前的每个时间点
        for civ in self.civilizations:
            times_to_apply = self.time_variables[civ]
            self.apply_transfer_matrix(civ, times_to_apply)

    def apply_transfer_matrix(self, civ, times=1):
        for _ in range(times):
            updated_resources = {resource: [0] for resource in self.resources[civ]}
            resource_keys = list(self.resources[civ].keys())
            
            # 应用转移矩阵
            for i, resource_key in enumerate(resource_keys):
                for j, _ in enumerate(resource_keys):
                    updated_resources[resource_key][0] += sum(self.transfer_matrices[civ][i][k] * self.resources[civ][resource_keys[k]][0] for k in range(len(resource_keys)))
            
            self.resources[civ] = updated_resources

    def update_history(self, round_number):
        """
        更新所有文明在指定回合的资源历史记录
        """
        for civ in self.civilizations:
            self.apply_transfer_matrix(civ)
            self.history[civ].append({
                "round": round_number,
                "resources": self.resources[civ],
                "political_system": self.political_system[civ]
            })

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
                    base_distance = random.randint(1, 3)
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
