from .rose import Rose 

class Executor:
    def __init__(self,rose:Rose):
        self.rose = Rose
    
    def run(self, context:dict):
        print("Executor starting...")
        return self.rose.run(context)