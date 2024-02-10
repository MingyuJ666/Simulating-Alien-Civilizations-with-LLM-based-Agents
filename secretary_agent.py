import os
from openai import OpenAI
import numpy as np
os.environ['OPENAI_API_KEY'] = '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'

class Secretary:
    def __init__(self):
        self.model = "gpt-3.5-turbo-0125"
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
        
    def evaluation(self, political_system, new_matrix):
        # Check political system
        valid_political_systems = ["friendly_cooperation", "militarism", "concealment"]
        is_valid_political_system = political_system in valid_political_systems
        
        # Check matrix
        # is_valid_matrix = self._is_valid_matrix(new_matrix)
        is_valid_matrix = True
        # Evaluate and return the result
        if is_valid_political_system and is_valid_matrix:
            return "true"
        else:
            return "false"
    
    import numpy as np

    def _is_valid_matrix(self, matrix):
        # 检查矩阵是否为5x5
        if matrix.shape != (5, 5):
            return False

        return True

    def evaluate_decision(self, political_system, action, proposed_matrix):
        prompt = f"""
        Given the political system '{political_system}' and the action '{action}', the alien civilization proposes the following state transition matrix adjustment: {proposed_matrix}. Based on the action descriptions and matrix impact:

        - Expressing friendliness has no direct impact on the state transition matrix for the current round.
        - Initiating cooperation increases the diagonal sum to 6.5, with the military capability coefficient required to be below 1.2.
        - War mobilization allows the military capability coefficient to exceed 1.5 up to 2.0, while keeping the total diagonal sum at 6.

        Evaluate whether the proposed state transition matrix adjustment is consistent with the conditions set forth by the action '{action}' and the current political system '{political_system}'.
        """
        # Assuming the use of a method `ask_model` to query the large language model
        response = self.ask_model(prompt)
        return response

    def ask_model(self, prompt):
        # This method should call the large language model with the prompt and return its evaluation
        # Placeholder for actual model calling code
        return "Placeholder response indicating whether the proposal is valid or not."


