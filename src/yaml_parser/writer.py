import yaml


def write_yaml(obj, path: str):
    with open(path, 'w') as wfile:
        yaml.dump(obj, wfile, allow_unicode=True, indent=2)
