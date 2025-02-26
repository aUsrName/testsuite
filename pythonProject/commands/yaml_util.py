import yaml


#用于读取yaml
def read_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value

#用于写入yaml
def write_yaml(yaml_path):
    with open(yaml_path, encoding='utf-8', mode='w') as f:
        data = {'teacher':[{'name1': 'test1'},{'name2': 'test2'}]}
        yaml.safe_dump(data, f, allow_unicode=True)

#用于清空yaml
def clean_yaml(yaml_path):
    #一定要用 w ，表示替换
    with open(yaml_path, encoding='utf-8', mode='w') as f:
        pass

if __name__ == '__main__':
    print(read_yaml('../testcases/test_api.yaml'))
    # write_yaml('../testcases/test_api.yaml')
    # clean_yaml('../testcases/test_api.yaml')