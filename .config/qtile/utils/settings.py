import json

from utils.variables import CONFIG_DIR, DEFAULT_CONFIG


def _get_config() -> dict:
    try:
        with open(CONFIG_DIR, "r") as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print("Config file not found. Using default config")
        with open(CONFIG_DIR, "w") as default_config_file:
            default_config_file.write(json.dumps(DEFAULT_CONFIG, indent=2))
            config = DEFAULT_CONFIG.copy()

    return config


config = _get_config()
