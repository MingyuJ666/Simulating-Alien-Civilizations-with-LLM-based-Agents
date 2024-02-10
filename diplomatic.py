class DiplomaticRelations:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DiplomaticRelations, cls).__new__(cls)
            # 初始化操作
            cls._instance.relations = {}  # 存储文明间的外交关系
        return cls._instance

    # def update_feeling(self, civ_name, other_civ_name, feeling):
    #     if civ_name not in self.relations:
    #         self.relations[civ_name] = {}
    #     if other_civ_name not in self.relations[civ_name]:
    #         self.relations[civ_name][other_civ_name] = {}
    #     self.relations[civ_name][other_civ_name]["feeling"] = feeling

    def update_public_stance(self, civ_name, other_civ_name, action):
        if civ_name not in self.relations:
            self.relations[civ_name] = {}
        if other_civ_name not in self.relations[civ_name]:
            self.relations[civ_name][other_civ_name] = {}
        self.relations[civ_name][other_civ_name]["public_stance"] = action

    def get_public_info(self, civ_name):
        public_info = {}
        for other_civ, details in self.relations.get(civ_name, {}).items():
            public_info[other_civ] = details.get("public_stance", "None")
        return public_info

    def get_private_info(self, civ_name):
        private_info = {}
        for other_civ, details in self.relations.get(civ_name, {}).items():
            private_info[other_civ] = details.get("feeling", "Indifferent")
        return private_info

# 使用示例
# 获取 DiplomaticRelations 的单例
# diplomatic_relations_instance = DiplomaticRelations()

