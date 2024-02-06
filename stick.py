from CivilizationInitializer import CivilizationInitializer
import copy
import asyncio

# Assuming CivilizationInitializer includes a history attribute now
initializer = CivilizationInitializer()

def get_historical_resources(civ, round_number):
    # 假设history的结构是 {civ: {round: resources}}
    # 如果指定回合的资源信息存在，则返回该信息
    if round_number in initializer.history[civ]:
        return initializer.history[civ][round_number]
    else:
        # 如果没有找到指定回合的信息，返回None或者一个默认值
        return None  # 或者是一个表示资源默认状态的字典


def record_history(civilization, round_number, resources, political_system):
    initializer = CivilizationInitializer()

    round_label = "Before game start" if round_number < 0 else f"Round {round_number}"

    current_resources = copy.deepcopy(resources)

    current_record = {
        "round_number": round_number,
        "round_label": round_label,
        "resources": current_resources,
        "political_system": political_system,
        "discovered_civilizations": {}
    }

    # 遍历发现的文明信息
    for discovered_civ in initializer.civilizations:
        if discovered_civ != civilization:  # 确保不是自己
            discovery_info = initializer.interplanetary_knowledge[civilization].get(discovered_civ)
            if discovery_info:  # 如果有发现信息
                current_record["discovered_civilizations"][discovered_civ] = discovery_info

    # 将当前记录添加到该回合的记录列表中
    initializer.history[civilization].append(current_record)


def print_record():
    initializer = CivilizationInitializer()
    for civ, records in initializer.history.items():
        print(f"History for {civ}:")
        for record in records:
            if 'round_label' in record:
                # 打印当前回合标签、资源和政治体制
                print(f"  {record['round_label']}:")
                print(f"    Resources:")
                for resource, value in record['resources'].items():
                    print(f"      {resource}: {value}")
                print(f"    Political System: {record['political_system']}")
                if 'discovered_civilizations' in record:
                    print("    Discovered Civilizations:")
                    for discovered_civ, civ_info in record['discovered_civilizations'].items():
                        print(f"      {discovered_civ}:")
                        if 'resources' in civ_info:
                            print("        Resources:")
                            for resource, value in civ_info['resources'].items():
                                print(f"          {resource}: {value}")
                        else:
                            print("        Resources: Information not available")
            else:
                # 如果记录中没有 'round_label'，可能需要处理或打印一条错误信息
                print("Error: 'round_label' missing in record.")
            