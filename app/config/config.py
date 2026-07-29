from pathlib import Path
import yaml

config_path = Path(__file__).parent / "config.yaml"

def load_config():
    with open(config_path) as file:
        config = yaml.safe_load(file)
        return config
