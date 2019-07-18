import yaml

def get_data_list(filename):
    with open("./data/"+filename, "r", encoding = "utf-8")as f:
        return yaml.load(f)


