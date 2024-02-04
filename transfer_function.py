from CivilizationInitializer import CivilizationInitializer

def transfer_function(civilization):
    initializer = CivilizationInitializer()
    if civilization not in initializer.civilizations:
        raise ValueError("Unknown civilization")
    return [[1.2 for _ in range(5)] for _ in range(5)]

def apply_function(civilization):
    initializer = CivilizationInitializer()
    transfer_matrix = transfer_function(civilization)
    resource_vector = initializer.resources[civilization]

    resource_list = [value[0] for key, value in resource_vector.items()]
    updated_resources = []
    for i in range(len(transfer_matrix)):
        updated_resource = sum(transfer_matrix[i][j] * resource_list[j] for j in range(len(resource_list)))
        updated_resources.append(updated_resource)

    for i, key in enumerate(resource_vector.keys()):
        initializer.resources[civilization][key] = [updated_resources[i]]