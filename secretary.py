import os
from openai import OpenAI
os.environ['OPENAI_API_KEY'] =  "sk-......"

class Secretary:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
        self.text1 = 'You are a good secretary, you can help me to judge whether the context is related to: '
        self.text2 = '. You must only say True or False, you should not say other thing.'
        self.text3 = 'This is the content: '

    def gpt4_evaluate(self, text, topic):

        response = self.client.chat.completions.create(
            model = self.model,
            messages= [
                {"role": "system", "content": self.text1 + topic + self.text2},
                {"role": "user", "content": self.text3 + text}
            ],
            temperature=0,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        answer = response.choices[0].message.content
        return answer
    def evaluate_text(self, text, topic):

        score = self.gpt4_evaluate(text, topic)
        print(score)

        if 'true' in score.lower():
            print('The text is relevant to the topic')
            return True
        if 'false' in score.lower():
            print('The text is not relevant to the topic')
            return False


secretary = Secretary()
text = "军备扩张：大幅增加国防预算，扩大军队规模，积极发展和购买先进武器系统和军事技术。"
topic = "军国主义"

result = secretary.evaluate_text(text, topic)
if result:
    print("文本与主题相关。")
else:
    print("文本与主题不相关。")