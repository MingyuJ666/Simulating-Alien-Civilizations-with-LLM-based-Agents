import asyncio
from CivilizationInitializer import *
from stick import *
from interplanetary_relationship import *
from dependency import *
from interface import *
from alien_agent import *

# Assuming stick.py is adjusted as per the previous instructions

initializer = CivilizationInitializer()
initializer.display_all()
initializer.display_distances()
finding_time = calculate_finding_time()
print_finding_time()
# Assuming you have a function to simulate changes or apply transfers
# def simulate_changes(civ, round_number):
#     # Dummy implementation: Apply changes or transfer to resources
#     new_matrix = create_matrix_with_diagonal(round_number)
#     initializer.update_transfer_matrix(civ, new_matrix)
#     initializer.apply_transfer_matrix(civ, 1)
#     update_knowledge(round_number)

def simulate_changes(civ, round_number, decision):
    # 初始化器实例
    initializer = CivilizationInitializer.instance

    # 解析决策（假设decision已经包含了解析后的信息）
    political_system, new_matrix = parse_chatgpt_response(decision)
    
    # 更新政治体制（如果需要）
    if political_system:
        initializer.update_political_system(civ, political_system)
    
    # 更新并应用转移矩阵
    if new_matrix is not None:
        initializer.update_transfer_matrix(civ, new_matrix)
    initializer.apply_transfer_matrix(civ, 1)  # 假设每次只应用1次转移矩阵


async def run_simulation():
    for round_number in range(1, 5):
        for civ in initializer.civilizations:
            history = get_civilization_history_as_string(civ)
            political_system = initializer.get_political_system(civ)
            agent = Alien(history, political_system)
            alien_agent_decision = agent.decide()
            print(alien_agent_decision)
            # 模拟变化
            # simulate_changes(civ, round_number)
            # 现在，使用更新的信息记录历史
            simulate_changes(civ, round_number, alien_agent_decision)
            record_history(civ, round_number, initializer.resources[civ], initializer.political_system[civ])
        print_record()
asyncio.run(run_simulation())

# After the simulation loop
