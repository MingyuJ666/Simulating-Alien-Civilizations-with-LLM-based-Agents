from CivilizationInitializer import CivilizationInitializer

def calculate_finding_time():
    initializer = CivilizationInitializer()
    finding_time = {}
    for civ_a in initializer.civilizations:
        for civ_b in initializer.civilizations:
            if civ_a == civ_b:
                continue
            distance_rounds = initializer.distances.get((civ_a, civ_b), 0)
            finding_time_a_to_b = distance_rounds - initializer.time_variables[civ_b]
            finding_time_b_to_a = distance_rounds - initializer.time_variables[civ_a]
            finding_time[(civ_a, civ_b)] = max(0, finding_time_a_to_b)
            finding_time[(civ_b, civ_a)] = max(0, finding_time_b_to_a)
    return finding_time

# def update_knowledge(current_round):
#     initializer = CivilizationInitializer()
#     finding_time = calculate_finding_time()
#     for civ_a in initializer.civilizations:
#         for civ_b in initializer.civilizations:
#             if civ_a == civ_b:
#                 continue
#             if current_round >= finding_time[(civ_a, civ_b)]:
#                 # 获得文明B的资源信息作为文明A的了解
#                 civ_b_resources = initializer.resources[civ_b]
#                 # 保存文明B的资源信息，而不仅仅是知识的回合数
#                 initializer.interplanetary_knowledge[civ_a][civ_b] = {
#                     "resources": civ_b_resources,
#                     "knowledge_round": current_round - finding_time[(civ_a, civ_b)]
#                 }

def update_knowledge(current_round):
    initializer = CivilizationInitializer()
    finding_time = calculate_finding_time()
    for civ_a in initializer.civilizations:
        for civ_b in initializer.civilizations:
            if civ_a == civ_b:
                continue
            # 计算当文明A能够发现文明B的资源信息的回合
            # 确保信息是在发现时间之后，且考虑信息传播的延迟
            if current_round >= finding_time[(civ_a, civ_b)]:
                information_round = current_round - initializer.distances[(civ_a, civ_b)]
                if information_round == 0:
                    information_round = information_round + 1
                # 获取历史资源信息
                civ_b_resources = get_historical_resources(civ_b, information_round)
                # 保存文明B在发现回合的资源信息
                initializer.interplanetary_knowledge[civ_a][civ_b] = {
                    "resources": civ_b_resources,
                    "knowledge_round": information_round
                }
                

def get_historical_resources(civ, round_number):
    initializer = CivilizationInitializer()
    # 默认情况，如果没有找到特定回合的信息，则返回当前资源
    historical_resources = initializer.resources.get(civ, None)
    # 尝试从历史记录中获取特定回合的资源信息
    if initializer.history.get(civ):
        for record in reversed(initializer.history[civ]):
            if record["round_number"] <= round_number:
                historical_resources = record["resources"]
                break
    return historical_resources



def print_finding_time():
    initializer = CivilizationInitializer()
    finding_time = calculate_finding_time()
    print("Finding Time Between Civilizations:")
    for (civ_a, civ_b), time_a_to_b in finding_time.items():
        print(f"{civ_a} discovered {civ_b} at round {time_a_to_b}.")
