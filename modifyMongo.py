#!/usr/bin/python3
import sys
import pymongo
import json

if len(sys.argv) == 1:
    print("please input arg!")
    exit()

group = sys.argv[1]
print("group is " + group)

with open("/etc/ansible/hosts", 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

host_data = {}
cur_group = ""
for line in lines:
    if line == "" or line[0] == '#':
        continue
    if line[0] == '[' and line[-1] == ']':
        if ':' in line:
            cur_group = None
            continue
        host_data[line[1:-1]] = []
        cur_group = line[1:-1]
    else:
        if cur_group == None:
            continue
        host_data[cur_group].append(line)

if group not in host_data:
    print("group "+ group + " not exist")
    exit()
print(host_data[group])


okCounter = 0
ngCounter = 0
for host in host_data[group]:
    user = "Dts-JYlink"
    pw = "jY^*0]2019>"
    uri = f"mongodb://{user}:{pw}@{host}:21949/admin?authMechanism=SCRAM-SHA-1"
    client = pymongo.MongoClient(uri)

    db = client["MDB_Base"]
    collection = db["t_special_config"]

    try:
        result = collection.find_one({"key":"ss"})
    except:
        print(host + 'error')
        continue
    result['SS_mc_type_No42']
    if '0043' in result['SS_mc_type_No42']:
        print(host + ' ' + result['SS_mc_type_No42']['0043'])
        okCounter += 1
    else:
        print(host + ' ng')
        ngCounter += 1
        result['SS_mc_type_No42']['0043'] = 'M0113'
        collection.update_one({"key":"ss"},{"$set": result})
    client.close()

print('ok:'+ str(okCounter))
print('ng:'+ str(ngCounter))
