import yaml


#用于读取yaml
def read_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value


if __name__ == '__main__':
    print(read_yaml('../testcases/test_api.yaml'))