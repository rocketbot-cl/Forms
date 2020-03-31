import configparser
import json

import requests

global token

module = GetParams('module')

if module == 'Login':
    ruta_ = GetParams("ruta_")

    config = configparser.ConfigParser()
    config.read(ruta_)
    email_ = config.get('USER', 'user')
    pass_ = config.get('USER', 'password')

    try:
        data = {'email': email_, 'password': pass_}
        res = requests.post('https://noc.myrb.io/api/auth/login', data,
                            headers={'content-type': 'application/x-www-form-urlencoded'})

        if res.status_code == 200:
            res = res.json()
            if res['success']:
                token = res['data']
            else:
                raise Exception(res['message'])
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'GetForm':
    token_ = GetParams('token')
    var_ = GetParams('result')

    try:
        res = requests.post('https://noc.myrb.io/api/formData/get/' + token_,
                            headers={'Authorization': "Bearer " + token})
        if res.status_code == 200:
            tmp = []
            res = res.json()
            print('rrr', res)
            if 'data' in res:
                for data in res['data']:
                    aa = {'id': data['id']}
                    tmp.append(aa)
            
            SetVar(var_, tmp)
        else:
            raise Exception(res.json())

    except Exception as e:
        PrintException()
        raise e

if module == 'GetFormData':
    id_ = GetParams('id_')
    token_ = GetParams('token_')

    try:
        res = requests.post('https://noc.myrb.io/api/formData/getQueue/' + id_ + '/' + token_,
                            headers={'Authorization': "Bearer " + token})
        if res.status_code == 200:
            tmp = []
            res = res.json()
            if 'data' in res:
                data = json.loads(res['data']['data'])
                for attr, value in data.items():
                    print('*' * 15, 'var', attr, '*' * 15)
                    SetVar(attr, value)
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SetStatus':
    status_ = GetParams('status_')
    id_ = GetParams('id_')

    if not id_:
        raise Exception("No form data loaded")
    try:
        s = 0
        if status_ == 'done':
            s = 1
        else:
            s = 0
        data = {'status': s}
        res = requests.post('https://noc.myrb.io/api/formData/setStatus/' + str(id_), data=data,
                            headers={'Authorization': "Bearer " + token})

        res = res.json()
        if not res['success']:
            raise Exception(res['message'])
    except Exception as e:
        PrintException()
        raise e
