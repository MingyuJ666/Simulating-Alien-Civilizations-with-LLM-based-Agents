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

def parse_chatgpt_response(response):
    # 解析政治体制
    political_system_match = re.search(r'\[Political System: \] (\w+)', response)
    political_system = political_system_match.group(1) if political_system_match else None
    
    # 解析转移矩阵
    transfer_matrix_match = re.search(r'\[Transfer Matrix: \] (.+?)\[', response, re.DOTALL)
    transfer_matrix_str = transfer_matrix_match.group(1).strip() if transfer_matrix_match else ""
    transfer_matrix = np.array([[float(num) for num in row.split()] for row in transfer_matrix_str.split('\n')])
    
    return political_system, transfer_matrix


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

