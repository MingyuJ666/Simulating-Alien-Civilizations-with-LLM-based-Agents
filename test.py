from CivilizationInitializer import *
from stick import *
from interplanetary_relationship import *
# Assuming stick.py is adjusted as per the previous instructions

initializer = CivilizationInitializer()
initializer.display_all()
initializer.display_distances()
finding_time = calculate_finding_time()
print_finding_time()
# Assuming you have a function to simulate changes or apply transfers
def simulate_changes(civ, round_number):
    # Dummy implementation: Apply changes or transfer to resources
    initializer.apply_transfer_matrix(civ, round_number)

for round_number in range(1, 5):
    for civ in initializer.civilizations:
        # 模拟变化
        simulate_changes(civ, round_number)
        # 现在，使用更新的信息记录历史
        record_history(civ, round_number, initializer.resources[civ], initializer.political_system[civ], finding_time)

# After the simulation loop
print_record()

