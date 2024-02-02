from alien_agent import Alien
from secretary import Secretary

thoughts = "侵略扩张"
events = "侵略扩张"
initial_resources = 100

alien = Alien(thoughts, events, initial_resources)
prompt = "你是一个外星文明，你需要去侵略别的文明，探测到附近星系有弱小的国家，击败他"
decision = alien.decide(prompt)



secretary = Secretary()
text = decision
topic = "和平主义"


result = False
while not result:
    decision = alien.decide(prompt)
    result = secretary.evaluate_text(decision, topic)

    if result:
        print("决策符合和平主义。")
    else:
        print("决策不符合和平主义，重新决策。")

