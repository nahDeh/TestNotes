import yaml


# 返回值是Dict
def readConfig(file_path):
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)
    return config_data


