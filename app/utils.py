import yaml


def load_config():
    with open('../config.yml') as conf:
        return yaml.safe_load(conf)
