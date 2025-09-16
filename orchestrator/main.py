from .ross import Ross
from .rose import Rose
from .executor import Executor
import json 

#example actions
def action_a(ctx):
    return f"Action A executed with {ctx}"

def action_b(ctx):
    return f"Action B executed with {ctx}"

if __name__ == "__main__":
    with open("orchestrator/config.json") as f:
        config = json.load(f);

    #build ross units from config
    ross_units = [
        Ross(cfg, action_a if cfg["action"] == "A" else action_b)
        for cfg in config["tasks"]
    ]

    #Combining into Rose
    rose = Rose(ross_units);

#Run with executor
executor = Executor(rose);
results = executor.run({"request_id":42});
print("Results: ",results)