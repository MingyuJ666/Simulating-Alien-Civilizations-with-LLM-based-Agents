from civil_resources import *
from transfer_function import *
from interplanetary_relationship import *
from initialize import *
from stick import *
# 初始化文明并获取相关数据
civilizations, political_system, resources, transfer_matrices, time_variables, distances = initialize_civilizations()
display_all(political_system, resources, transfer_matrices, time_variables)
print_finding_time()
# 更新资源并记录历史
for round_number in range(1, 11):  # 假设 max_rounds 是游戏的最大回合数
    for civ in civilizations:
        resources[civ] = apply_transfer_matrix(transfer_matrices[civ], resources[civ], time_variables[civ])
        record_history(civ, round_number, resources[civ], political_system[civ], interplanetary_knowledge, finding_time)

# 更新知识（假设当前回合数是5）
update_knowledge(5)
display_all(political_system, resources, transfer_matrices, time_variables)
# 打印知识
print_knowledge(5)
print_record(history,finding_time)
