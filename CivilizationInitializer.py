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

    def apply_transfer_matrix(self, civ, times=1):
        for _ in range(times):
            updated_resources = {resource: [0] for resource in self.resources[civ]}
            resource_keys = list(self.resources[civ].keys())
            
            # 应用转移矩阵
            for i, resource_key in enumerate(resource_keys):
                updated_resources[resource_key][0] = sum(self.transfer_matrices[civ][i][k] * self.resources[civ][resource_keys[k]][0] for k in range(len(resource_keys)))
            
            self.resources[civ] = updated_resources

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
