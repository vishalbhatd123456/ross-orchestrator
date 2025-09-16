class Ross:
    def __init__(self, config:dict, action):
        self.config = config
        self.action = action

    def execute(self, context:dict):
        if self.config.get("allowed",True):
            return self.action(context)
        else:
            print(f"skipping execution: {self.config}")
            return None