import json
import copy
import basics
import shared_info

serversList = shared_info.serversList

def server_check(id, name):
    # Ensure 'default' exists, create with basic settings if not
    if 'default' not in serversList:
        serversList['default'] = {
            'prefix': '-',
            'draftStatus': {'draftRunning': False},
            'fachannel': 0,
            'tradechannel': 0,
            'draftchannel': 0,
            'releasechannel': 0,
            'aimedia': 0,
            'maxroster': 15,
            'hardcap': 100,
            'softcap': 60,
            'holdout': 50,
            'tuodloh': 150,
            'options': 'on',
            'rookieoptions': 0.0,
            'birdrights': 'on',
            'tradeback': 'on',
            'tradefa': 0,
            'tradeapproval': 'off',
            'poschanges': 'on',
        }
    
    default = serversList['default']
    id = str(id)
    if id in serversList:
        for d, v in default.items():
            if d in serversList[id]:
                continue
            else:
                serversList[id][d] = v
    else:
        serversList[id] = copy.deepcopy(default)
    serversList[id]['name'] = name
    return(serversList)
