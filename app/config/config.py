from pathlib import Path
import yaml

print(__file__)

config_path = Path(__file__).parent / "config.yaml"
print(config_path)

def load_config():
    with open(config_path) as file:
        config = yaml.safe_load(file)
        return config
