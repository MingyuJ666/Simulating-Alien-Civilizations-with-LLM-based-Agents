# stick.py

# 用来记录每个文明在每个回合的状态
history = {}

def record_history(civilization, round_number, resources, political_system, interplanetary_knowledge, finding_time):
    if civilization not in history:
        history[civilization] = {}

    # 记录当前文明的资源和政治体制
    current_record = {
        "resources": resources,
        "political_system": political_system,
        "discovered_civilizations": {}
    }

    # 遍历发现的文明并记录它们的信息
    for discovered_civ, discovery_round in finding_time.items():
        if discovered_civ[0] == civilization and round_number >= discovery_round:
            discovered_info = interplanetary_knowledge[civilization].get(discovered_civ[1], {})
            current_record["discovered_civilizations"][discovered_civ[1]] = discovered_info

    history[civilization][round_number] = current_record

def print_record(history, finding_time):
    for civ, rounds in history.items():
        print(f"History for {civ}:")
        for round_number, info in sorted(rounds.items()):
            print(f"  Round {round_number}:")
            print(f"    Resources: {info['resources']}")
            print(f"    Political System: {info['political_system']}")
            if "discovered_civilizations" in info:
                for discovered_civ, _ in info["discovered_civilizations"].items():
                    if (civ, discovered_civ) in finding_time:
                        # 计算文明被发现的回合数
                        discovery_round = finding_time[(civ, discovered_civ)]
                        observed_rounds = round_number - discovery_round
                        print(f"    Discovered {discovered_civ} at round {discovery_round}, observed for {observed_rounds} rounds.")
                        # 尝试找到并打印发现文明的信息
                        if discovered_civ in history and observed_rounds in history[discovered_civ]:
                            discovered_info = history[discovered_civ][observed_rounds]
                            print(f"      Resources at observed round: {discovered_info['resources']}")
                            print(f"      Political System at observed round: {discovered_info['political_system']}")
                        else:
                            print(f"      No detailed information available for {discovered_civ} at observed round.")


