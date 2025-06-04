import yaml

#带测试用例编号key一起读取！
def yaml_data_with_file(file_name, key):#List[Dict]
    with open(file_name, "r") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)[key]
        ret = list()
        for k in data.keys():
            v=data[k]
            v["key"]=k
            ret.append(v)
        return ret
