import random

def initialize_distances():
    # 初始化文明间的距离
    distances = {
        ("Earth", "Three Body"): 1,  # 以回合数表示
        ("Earth", "Borg"): 2,
        ("Three Body", "Borg"): 1
    }
    return distances

def initialize_civilizations():
    # 初始化文明
    civilizations = ["Earth", "Three Body", "Borg"]
    political_system = {civ: "" for civ in civilizations}

    # 示例：手动为每个文明指定政治体制
    political_system["Earth"] = "friendly_cooperation"
    political_system["Three Body"] = "militarism"
    political_system["Borg"] = "concealment"

    # 为每个文明生成独立的资源、转移矩阵
    resources = {}
    transfer_matrices = {}
    resources['Earth']={
        "military_capability": [1],
            "technology_development": [1],
            "production_capability": [1],
            "consumption": [1],
            "storage": [1]
    }

    for civ in civilizations:
        resources[civ] = {
            "military_capability": [1],
            "technology_development": [1],
            "production_capability": [1],
            "consumption": [1],
            "storage": [1]
        }
        transfer_matrices[civ] = [[1.2 for _ in range(5)] for _ in range(5)]

    # 为每个文明随机分配一个 1-8 之间的时间变量，这个标志着文明的出生时间
    time_variables = {civ: random.randint(1, 8) for civ in civilizations}

    distances = initialize_distances()

    return civilizations, political_system, resources, transfer_matrices, time_variables, distances

def apply_transfer_matrix(transfer_matrix, resource_dict, times):
    if not isinstance(resource_dict, dict):
        raise ValueError("resource_dict must be a dict")

    for _ in range(times):
        updated_resources = []
        resource_vector = [value[0] for value in resource_dict.values()]
        for i in range(len(transfer_matrix)):
            updated_resource = sum(transfer_matrix[i][j] * resource_vector[j] for j in range(len(resource_vector)))
            updated_resources.append([updated_resource])

        # 将列表转换回字典形式
        keys = list(resource_dict.keys())
        resource_dict = {keys[i]: updated_resources[i] for i in range(len(keys))}

    return resource_dict

# 定义函数以显示所有文明及其资源
def display_all(civilizations, political_system, resources, time_variables):
    for civ in civilizations:
        print(f'{civ}:')
        print(f'  Resources: {resources[civ]}')
        print(f'  Political System: {political_system[civ]}')
        print(f'  Time Variable: {time_variables[civ]}\n')

# # 使用示例

civilizations, political_system, resources, transfer_matrices, time_variables, distances = initialize_civilizations()

# # 应用转移矩阵到资源向量，左乘时间变量次
for civ in civilizations:
    resources[civ] = apply_transfer_matrix(transfer_matrices[civ], resources[civ], time_variables[civ])

# # 输出所有文明及其资源
# display_all(civilizations, political_system, resources, time_variables)