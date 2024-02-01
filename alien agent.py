import numpy as np
import random
import os
from openai import OpenAI
os.environ['OPENAI_API_KEY'] =  "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"

class Alien:
    def __init__(self, thoughts, events, initial_resources):
        self.THOUGHTS = thoughts
        self.EVENTS = events
        self.resources = initial_resources
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), )
        self.text1 = 'You are a civilization and you need to think according to the following: '


    def decide(self, prompt):

        decision = f"Think about the: {self.THOUGHTS}, This is the currant event: {self.EVENTS}, This is the currant resources: {self.resources}. "
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.text1},
                {"role": "user", "content": prompt + decision}
            ],
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )


        return response.choices[0].message.content



# 使用示例
thoughts = "探索"
events = "资源发现"
initial_resources = 100

alien = Alien(thoughts, events, initial_resources)
prompt = "探测到附近星系有潜在危机"
decision = alien.decide(prompt)
print(decision)

