import os
from openai import OpenAI
import numpy as np
os.environ['OPENAI_API_KEY'] = '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'

class Secretary:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
        
    def evaluation(self, political_system, new_matrix):
        # Check political system
        valid_political_systems = ["friendly_cooperation", "militarism", "concealment"]
        is_valid_political_system = political_system in valid_political_systems
        
        # Check matrix
        is_valid_matrix = self._is_valid_matrix(new_matrix)
        
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
        
        # 检查矩阵所有元素之和是否为5
        if np.sum(matrix) != 5:
            return False
        
        return True


