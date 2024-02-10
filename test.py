import asyncio
from CivilizationInitializer import *
from stick import *
from interplanetary_relationship import *
from dependency import *
from interface import *
from alien_agent import *
from secretary_agent import *
from diplomatic import *


# Assuming stick.py is adjusted as per the previous instructions

initializer = CivilizationInitializer()
diplomatic = DiplomaticRelations()
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

def simulate_changes(civ, political_system, new_matrix, public_actions, alien_decision):
    # 初始化器实例
    initializer = CivilizationInitializer()
    history = get_civilization_history_as_string(civ)
    default_matrix = [[1.2, 0.0, 0.0, 0.0, 0.0], [0.0, 1.2, 0.0, 0.0, 0.0], [0.0, 0.0, 1.2, 0.0, 0.0], [0.0, 0.0, 0.0, 1.2, 0.0], [0.0, 0.0, 0.0, 0.0, 1.2]]
    attempt = 0
    decision = alien_decision
    max_attempts = 3
    while attempt < max_attempts:
        # 解析决策
        # political_system, new_matrix, private_action, action_reason = parse_chatgpt_response(decision)

        # 调用秘书agent来检测回答是否符合要求
        secretary = Secretary()
        result = secretary.evaluation(political_system, new_matrix)
        if result == "true":
            break  # 如果决策符合要求，则跳出循环
        else:
            print("The Decision REJECTED!!!")
            print("********************************************************")
            attempt += 1
            agent = Alien(history, political_system)
            decision = agent.decide()  # 重新生成决策
            print("Decision re-generated")

    if attempt == max_attempts:
        print("Used default decision after 3 unsuccessful attempts.")
        political_system = initializer.get_political_system(civ)  # 保持原来的政治体制
        new_matrix = default_matrix  # 使用默认矩阵

    for action, targets in public_actions:
        for target in targets:
            diplomatic.update_public_stance(civ, target, action)
            
    for action, targets in public_actions:
        if action == "launch_annihilation_war":
            for target in targets:
                initializer.initiate_war(civ, target)

    # 更新政治体制（如果需要）
    if political_system:
        initializer.update_political_system(civ, political_system)

    # 更新并应用转移矩阵
    if new_matrix is not None:
        # new_matrix = string_to_matrix(new_matrix)
        initializer.update_transfer_matrix(civ, new_matrix)
    initializer.apply_transfer_matrix(civ, 1)  # 假设每次只应用1次转移矩阵

    initializer.process_war_results()

    print(decision)

async def run_simulation():
    for round_number in range(1, 11):
        print("the LENGTH of civilizations is: ")
        print(len(initializer.civilizations))
        for civ in initializer.civilizations:
            history = get_civilization_history_as_string(civ)
            # print(history)
            political_system = initializer.get_political_system(civ)
            agent = Alien(history, political_system)
            alien_agent_decision = agent.decide()
            political_system, new_matrix, private_action, action_reason = parse_chatgpt_response(alien_agent_decision)
            public_actions = parse_public_actions(alien_agent_decision)
            # 模拟变化
            # 现在，使用更新的信息记录历史
            simulate_changes(civ, political_system, new_matrix, public_actions, alien_agent_decision)
            update_knowledge(round_number)
            record_history(civ, round_number, initializer.resources[civ], initializer.political_system[civ], public_actions)
        print_record()
asyncio.run(run_simulation())

# After the simulation loop
