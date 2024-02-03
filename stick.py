from CivilizationInitializer import CivilizationInitializer
import copy

# Assuming CivilizationInitializer includes a history attribute now
initializer = CivilizationInitializer()

def record_history(civilization, round_number, resources, political_system, finding_time):
    initializer = CivilizationInitializer()

    # 如果是负回合数，意味着游戏开始前的历史记录
    round_label = f"Before game start ({-round_number} round(s) before)" if round_number < 0 else f"Round {round_number}"
    
    # 使用copy.deepcopy确保对resources进行深拷贝
    current_resources = copy.deepcopy(resources)

    # 构建当前文明的历史记录，包括政治体制和发现的文明信息
    current_record = {
        "round_number": round_number,
        "round_label": round_label,
        "resources": current_resources,
        "political_system": political_system,
        "discovered_civilizations": {}
    }

    # 遍历发现的文明，根据finding_time和interplanetary_knowledge更新发现的文明信息
    for discovered_civ, civ_info in initializer.interplanetary_knowledge.get(civilization, {}).items():
        if round_number >= finding_time.get((civilization, discovered_civ), float('inf')):
            # 这里采用深拷贝是为了保留记录时刻的资源状态
            discovered_resources = copy.deepcopy(civ_info.get("resources", "Information not available"))
            # 更新current_record以包含发现的文明及其资源信息
            current_record["discovered_civilizations"][discovered_civ] = {
                "resources": discovered_resources
            }

    # 将当前记录添加到历史中，不需要再次添加，避免重复
    initializer.history[civilization].append(current_record)

def print_record():
    initializer = CivilizationInitializer()
    for civ, records in initializer.history.items():
        print(f"History for {civ}:")
        for record in records:
            # 打印当前回合标签、资源和政治体制
            print(f"  {record['round_label']}:")
            print(f"    Resources:")
            for resource, value in record['resources'].items():
                print(f"      {resource}: {value}")
            print(f"    Political System: {record['political_system']}")

            # 打印发现的文明及其资源信息
            if record["discovered_civilizations"]:  # 确保发现的文明列表不为空
                print("    Discovered Civilizations:")
                for discovered_civ, civ_info in record["discovered_civilizations"].items():
                    print(f"      {discovered_civ}:")
                    if "resources" in civ_info:  # 确保资源信息不为空
                        print(f"        Resources:")
                        for resource, value in civ_info["resources"].items():
                            print(f"          {resource}: {value}")
                    else:
                        print("        Resources: Information not available")
