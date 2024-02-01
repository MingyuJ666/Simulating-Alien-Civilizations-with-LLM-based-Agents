# stick.py

# 用来记录每个文明在每个回合的状态
history = {}

def record_history(civilization, round_number, resources, political_system):
    if civilization not in history:
        history[civilization] = {}
    history[civilization][round_number] = {"resources": resources, "political_system": political_system}
