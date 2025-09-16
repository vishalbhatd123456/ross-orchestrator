from .ross import Ross

class Rose:
    def __init__(self,ross_list:list[Ross]):
        self.ross_list = ross_list

    def run(self, context:dict):
        results = []
        for ross in self.ross_list:
            results.append(ross.execute(context))
            return results