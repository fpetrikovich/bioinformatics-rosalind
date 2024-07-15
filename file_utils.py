import yaml
import json

def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()
    
def read_json_file(file):
    with open(file, 'r') as json_file:
        return json.load(json_file)
    
def write_file_content(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def convert_json_to_yaml(json_data):
    return yaml.dump(json_data, default_flow_style=False)