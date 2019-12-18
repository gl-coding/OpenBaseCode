#encoding=utf8
import json

def dict_to_list(data_dic, res):
    if not isinstance(data_dic, dict):
        return
    for k, v in data_dic.items():
        if isinstance(v, dict):
            dict_to_list(v, res)
        elif isinstance(v, list):
            res.append([k, v])
            for lv in v:
                dict_to_list(lv, res)
        else:
            res.append([k, v])

def pick_json(json_str, key_set, return_type="dict"):
    res = []
    json_dic = json.loads(json_str)
    dict_to_list(json_dic, res)

    #return key_set and val_set
    if return_type == "dict":
        res_dic = {}
        for k, v in res:
            if k in key_set:
                res_dic.update({k: v})
        return res_dic
    #return val_set
    elif return_type == "list":
        res_list = []
        for k, v in res:
            if k in key_set:
                res_list.append(v)
        return res_list
    else:
        return "error"
    
if __name__ == "__main__":
    json_dic = {"hl":{"age":27,"height":175},"lyh":{"age":28,"height":160},'wql':{"age":31,"height":172}}
    json_str = json.dumps(json_dic)

    key_set = set(["age", "height"])
    json_res = pick_json(json_str, key_set, "list")
    print json_res

    json_res = pick_json(json_str, key_set, "dict")
    print json_res
