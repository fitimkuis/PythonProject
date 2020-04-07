import json
from collections import defaultdict
from pprint import pprint


s = """
 {
    "http":{
       "http://":"64.90.50.38:45876/",
       "http://":"89.250.220.40:54687/",
       "http://":"89.207.92.146:37766/",
       "http://":"89.23.194.174:8080/",
       "http://":"82.208.111.100:52480/"
    }
 }
 """

def custom_hook(obj):
    # Identify dictionary with duplicate keys
    # If found create a separate dict with single key and val and as list.
    if len(obj) > 1 and len(set(i for i, j in obj)) == 1:
        data_dict = defaultdict(list)
        for i, j in obj:
            data_dict[i].append(j)
        return dict(data_dict)
    return dict(obj)