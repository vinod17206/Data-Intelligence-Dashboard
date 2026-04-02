import json
def save_data(d):
 f=open('data/datasets.json','r+');data=json.load(f);data.append(d);f.seek(0);json.dump(data,f,indent=4)
