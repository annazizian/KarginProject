import yaml


def read_yaml(path: str):
    with open(path) as rfile:
        return yaml.full_load(rfile)
