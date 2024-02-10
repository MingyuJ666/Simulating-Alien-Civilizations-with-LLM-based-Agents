import re
import numpy as np
from CivilizationInitializer import CivilizationInitializer

def update_civilization_transfer_matrix(civ_name, new_matrix):
    # 获取CivilizationInitializer的实例
    initializer = CivilizationInitializer()
    
    # 调用方法更新资源转移矩阵
    initializer.update_transfer_matrix(civ_name, new_matrix)

# 示例用法
# new_matrix = [[新的矩阵值]]
# update_civilization_transfer_matrix("Earth", new_matrix)

# 假设在 CivilizationInitializer 类中有一个方法来获取历史记录，
# 这里添加一个函数来格式化这些记录为字符串

def get_civilization_history_as_string(civ_name):
    """
    获取指定文明的历史记录，并将其转换成字符串格式。
    """
    initializer = CivilizationInitializer()  # 获取CivilizationInitializer的实例
    history_records = initializer.history.get(civ_name, [])  # 获取指定文明的历史记录

    # 将历史记录转换为字符串
    history_str = ""
    for record in history_records:
        round_label = record.get('round_label', 'Unknown round')
        resources = record.get('resources', {})
        political_system = record.get('political_system', 'Unknown')
        
        # 格式化资源信息
        resources_str = ", ".join([f"{key}: {value}" for key, value in resources.items()])
        
        # 将当前记录添加到历史字符串中
        history_str += f"Round: {round_label}, Resources: {resources_str}, Political System: {political_system}\n"

    return history_str

import re
import numpy as np

def parse_chatgpt_response(response):
    # 解析政治体制
    political_system_match = re.search(r'\[Political System: \] (.*?)\n', response)
    political_system = political_system_match.group(1) if political_system_match else None
    
    # 解析转移矩阵
    matrix_str_match = re.search(r'\[Transfer Matrix: \](.+?)(?=\[Transfer Matrix Reason: \])', response, re.DOTALL)
    if matrix_str_match:
        matrix_str = matrix_str_match.group(1)
        # 移除非数字字符，除了数字、逗号、分号和换行符
        clean_matrix_str = re.sub(r'[^\d.,;\n]', '', matrix_str)
        # 按分号分割行
        rows = clean_matrix_str.strip().split(';')
        # 解析每一行为浮点数列表，跳过空字符串
        matrix = []
        for row in rows:
            if not row:  # 跳过空行（可能由最后一个分号导致）
                continue
            # 分割行中的元素，并移除空字符串
            nums = [num.strip() for num in row.split(',') if num.strip()]
            # 转换为浮点数
            row_nums = list(map(float, nums))
            matrix.append(row_nums)
        # 转换成NumPy数组
        transfer_matrix = np.array(matrix)

    # 解析私人行动
    private_action_match = re.search(r'\[Private Action: \] (.*)', response)
    private_action = private_action_match.group(1) if private_action_match else None

    # 解析行动原因
    action_reason_match = re.search(r'\[Action Reason: \] (.*)', response)
    action_reason = action_reason_match.group(1) if action_reason_match else None

    return political_system, transfer_matrix, private_action, action_reason

def parse_public_actions(response):
    # 查找公共行动的部分
    public_action_match = re.search(r'\[Public Action: \] (.+)', response)
    actions_with_targets = []

    if public_action_match:
        # 获取匹配到的行动字符串，按照 "/" 分割不同的行动
        actions_text = public_action_match.group(1).split(' / ')
        
        for action_text in actions_text:
            # 分离行动和目标文明，注意处理 "Do Nothing" 的情况
            if " towards civilization " in action_text:
                action, targets_str = action_text.split(' towards civilization ')
                targets = targets_str.split(' | ')
            elif " from civilization " in action_text:
                action, targets_str = action_text.split(' from civilization ')
                targets = targets_str.split(' | ')
            else:
                action = action_text
                targets = []

            actions_with_targets.append((action, targets))

    return actions_with_targets

# 示例使用
response = "[Public Action: ] express_friendliness towards civilization civ1 | civ2 / initiate_cooperation towards civilization civ3 / Do Nothing"
actions_with_targets = parse_public_actions(response)

for action, targets in actions_with_targets:
    print(f"Action: {action}, Targets: {targets}")


def string_to_matrix(matrix_string):
    # 假设matrix_string是一个以换行符分隔的字符串，每行有5个由空格分隔的数字
    matrix_lines = matrix_string.strip().split('\n')
    matrix = np.zeros((5, 5))  # 创建一个5x5的零矩阵
    for i, line in enumerate(matrix_lines):
        row_values = line.split()
        if len(row_values) != 5:
            raise ValueError("每行需要有5个数字")
        matrix[i, :] = [float(value) for value in row_values]
    return matrix


