# 导入初始化模块以获取文明的时间变量
from initialize import time_variables
from stick import *

civilizations = ["Earth", "Three Body", "Borg"]

# 计算文明之间的发现时间
finding_time = {}
for civ_a in civilizations:
    for civ_b in civilizations:
        if civ_a == civ_b:
            continue
        # 保证矩阵是对称的
        if (civ_b, civ_a) in finding_time:
            finding_time[(civ_a, civ_b)] = finding_time[(civ_b, civ_a)]
            continue
        # 计算发现时间
        distance = abs(time_variables[civ_a] - time_variables[civ_b])
        later_time = max(time_variables[civ_a], time_variables[civ_b])
        discovery_time = distance - later_time
        finding_time[(civ_a, civ_b)] = discovery_time

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

# 示例：假设当前是第10回合
current_round = 10
update_knowledge(current_round)

# 输出当前的星际知识
def print_knowledge(current_round):
    for observing_civ in interplanetary_knowledge:
        print(f"{observing_civ}'s knowledge at round {current_round}:")
        for observed_civ, knowledge_round in interplanetary_knowledge[observing_civ].items():
            if observed_civ in history and knowledge_round in history[observed_civ]:
                observed_info = history[observed_civ][knowledge_round]
                print(f"  About {observed_civ} (from round {knowledge_round}):")
                print(f"    Resources: {observed_info['resources']}")
                print(f"    Political System: {observed_info['political_system']}")

