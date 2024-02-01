resources = {
    "Earth": {
        "military_capability": [1],
        "technology_development": [1],
        "production_capability": [1],
        "consumption": [1],
        "storage": [1]
    },
    "Three Body": {
        "military_capability": [1],
        "technology_development": [1],
        "production_capability": [1],
        "consumption": [1],
        "storage": [1]
    },
    "Borg": {
        "military_capability": [1],
        "technology_development": [1],
        "production_capability": [1],
        "consumption": [1],
        "storage": [1]
    }
}

def print_all_resources():
    for civilization, res in resources.items():
        print(f'"{civilization}": ')
        for key, value in res.items():
            print(f'        "{key}": {value},')

def print_civilization_resources(civilization):
    if civilization in resources:
        print(f'"{civilization}": ')
        for key, value in resources[civilization].items():
            print(f'        "{key}": {value},')
    else:
        print(f'No resources found for civilization: {civilization}')
