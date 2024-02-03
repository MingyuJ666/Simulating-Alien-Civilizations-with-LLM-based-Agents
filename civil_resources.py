from CivilizationInitializer import CivilizationInitializer

def print_all_resources():
    initializer = CivilizationInitializer()
    for civilization, res in initializer.resources.items():
        print(f'"{civilization}": ')
        for key, value in res.items():
            print(f'        "{key}": {value},')

def print_civilization_resources(civilization):
    initializer = CivilizationInitializer()
    if civilization in initializer.resources:
        print(f'"{civilization}": ')
        for key, value in initializer.resources[civilization].items():
            print(f'        "{key}": {value},')
    else:
        print(f'No resources found for civilization: {civilization}')

