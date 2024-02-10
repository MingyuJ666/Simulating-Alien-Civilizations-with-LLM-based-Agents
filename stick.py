from dependency import get_initializer
import copy

# Assuming CivilizationInitializer includes a history attribute now
initializer = get_initializer()

def get_historical_resources(civ, round_number):
    # 假设history的结构是 {civ: {round: resources}}
    # 如果指定回合的资源信息存在，则返回该信息
    if round_number in initializer.history[civ]:
        return initializer.history[civ][round_number]
    else:
        # 如果没有找到指定回合的信息，返回None或者一个默认值
        return None  # 或者是一个表示资源默认状态的字典

def record_history(civilization, round_number, resources, political_system, public_actions):
    initializer = get_initializer()

    round_label = "Before game start" if round_number < 0 else f"Round {round_number}"

    current_resources = copy.deepcopy(resources)

    current_record = {
        "round_number": round_number,
        "round_label": round_label,
        "resources": current_resources,
        "political_system": political_system,
        "discovered_civilizations": {},
        "public_actions": public_actions,  # 新增 - 对其他文明的公开行为
        # "private_feelings": private_feelings  # 新增 - 对其他文明的私密情感态度
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
    initializer = get_initializer()
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
            
# 在 stick.py 中
def get_historical_resources_until_last_round(civ, current_round):
    """
    获取指定文明直至上一回合的全部资源和政体信息。
    :param civ: 文明名称
    :param current_round: 当前回合数
    :return: 上一回合的资源和政体信息
    """
    initializer = get_initializer()
    # 假设历史记录是按回合顺序存储的，并且包含资源和政体信息
    if civ in initializer.history:
        history_records = initializer.history[civ]
        # 查找直至上一回合的记录
        for record in reversed(history_records):
            if record["round_number"] < current_round:
                return record  # 返回找到的上一回合信息
    return {}  # 如果没有找到信息，则返回空字典
