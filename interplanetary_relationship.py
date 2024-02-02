# 导入初始化模块以获取文明的时间变量
from initialize import time_variables
from stick import *

civilizations = ["Earth", "Three Body", "Borg"]

# 导入距离数据
from initialize import initialize_civilizations, initialize_distances

# 获取初始化的数据
civilizations, political_system, resources, transfer_matrices, time_variables, distances = initialize_civilizations()

# 使用距离来计算发现时间
def calculate_finding_time():
    finding_time = {}
    for civ_a in civilizations:
        for civ_b in civilizations:
            if civ_a == civ_b:
                continue
            # 使用距离来计算发现时间
            if (civ_a, civ_b) in distances:
                distance_rounds = distances[(civ_a, civ_b)]
            elif (civ_b, civ_a) in distances:
                distance_rounds = distances[(civ_b, civ_a)]
            else:
                continue  # 如果没有定义距离，则跳过

            # 确保矩阵是对称的
            finding_time[(civ_a, civ_b)] = distance_rounds
            finding_time[(civ_b, civ_a)] = distance_rounds

    return finding_time

# 计算文明之间的发现时间
finding_time = calculate_finding_time()

# 初始化星际知识
interplanetary_knowledge = {civ: {} for civ in civilizations}

# 更新星际知识的函数
def update_knowledge(current_round):
    for civ_a in civilizations:
        for civ_b in civilizations:
            if civ_a == civ_b:
                continue
            # 确定文明之间是否已经发现彼此
            if current_round >= finding_time[(civ_a, civ_b)]:
                # 更新文明 A 对文明 B 的了解
                knowledge_round = current_round - finding_time[(civ_a, civ_b)]
                interplanetary_knowledge[civ_a][civ_b] = f"Information of {civ_b} from round {knowledge_round}"

def print_finding_time():
    print("Finding Time Between Civilizations:")
    for pair, round in finding_time.items():
        print(f"  {pair[0]} and {pair[1]} discovered each other at round {round}")

# 输出当前的星际知识
def print_knowledge(current_round):
    print(f"Knowledge at round {current_round}:")
    for civ_a in civilizations:
        for civ_b in civilizations:
            if civ_a != civ_b:
                # 检查是否已经发现了这个文明
                if current_round >= finding_time.get((civ_a, civ_b), float('inf')):
                    # 打印发现时间和相关信息
                    discovery_time = finding_time[(civ_a, civ_b)]
                    knowledge_info = interplanetary_knowledge[civ_a].get(civ_b, "No information available")
                    print(f"{civ_a} discovered {civ_b} at round {discovery_time}: {knowledge_info}")
                else:
                    print(f"{civ_a} has not discovered {civ_b} yet.")
