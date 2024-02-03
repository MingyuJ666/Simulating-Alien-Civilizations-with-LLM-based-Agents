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

def update_knowledge(current_round):
    initializer = CivilizationInitializer()
    finding_time = calculate_finding_time()
    for civ_a in initializer.civilizations:
        for civ_b in initializer.civilizations:
            if civ_a == civ_b:
                continue
            if current_round >= finding_time[(civ_a, civ_b)]:
                # 获得文明B的资源信息作为文明A的了解
                civ_b_resources = initializer.resources[civ_b]
                # 保存文明B的资源信息，而不仅仅是知识的回合数
                initializer.interplanetary_knowledge[civ_a][civ_b] = {
                    "resources": civ_b_resources,
                    "knowledge_round": current_round - finding_time[(civ_a, civ_b)]
                }


def print_finding_time():
    initializer = CivilizationInitializer()
    finding_time = calculate_finding_time()
    print("Finding Time Between Civilizations:")
    for (civ_a, civ_b), time_a_to_b in finding_time.items():
        print(f"{civ_a} discovered {civ_b} at round {time_a_to_b}.")


