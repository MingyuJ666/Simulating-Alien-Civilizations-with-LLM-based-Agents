from civil_resources import resources

def transfer_function(civilization):
    if civilization not in ["Earth", "Three Body", "Borg"]:
        raise ValueError("Unknown civilization")

    # 定义一个 5x5 的矩阵，所有元素都是 1.2
    matrix = [[1.2 for _ in range(5)] for _ in range(5)]
    return matrix

def apply_function(civilization):
    transfer_matrix = transfer_function(civilization)
    resource_vector = resources[civilization]

    # 转换字典中的资源值为矩阵可操作的列表形式
    resource_list = [value[0] for key, value in resource_vector.items()]

    # 应用转移矩阵
    updated_resources = []
    for i in range(len(transfer_matrix)):
        updated_resource = sum(transfer_matrix[i][j] * resource_list[j] for j in range(len(resource_list)))
        updated_resources.append(updated_resource)

    # 更新资源字典
    for i, key in enumerate(resource_vector.keys()):
        resources[civilization][key] = [updated_resources[i]]


