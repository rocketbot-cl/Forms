import configparser
import json

import requests

global token
global server_

module = GetParams('module')

if module == 'Login':
    ruta_ = GetParams("ruta_")

    config = configparser.ConfigParser()
    config.read(ruta_)
    email_ = config.get('USER', 'user')
    pass_ = config.get('USER', 'password')
    server_ = config.get('NOC', 'server')


    try:
        data = {'email': email_, 'password': pass_}
        res = requests.post(server_ + '/api/auth/login', data,
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
        res = requests.post(server_ + '/api/formData/get/' + token_,
                            headers={'Authorization': "Bearer " + token})
        if res.status_code == 200:
            tmp = []
            res = res.json()
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
        res = requests.post(server_ + '/api/formData/getQueue/' + id_ + '/' + token_,
                            headers={'Authorization': "Bearer " + token})
        if res.status_code == 200:
            tmp = []
            res = res.json()
            print('RES:',res)

            if 'data' in res:
                if 'user_form_email' in res['data']:
                    SetVar('user_form_email', res['data']['user_form_email'])

                if 'xperience' in res['data']:
                    SetVar('xperience', res['data']['xperience'])
                data = json.loads(res['data']['data'])
                for attr, value in data.items():
                    SetVar(attr, value)
        else:
            raise Exception(res.json()['message'])

    except Exception as e:
        PrintException()
        raise e

if module == 'SetStatus':
    status_ = GetParams('status_')
    id_ = GetParams('id_')
    _var = GetParams('result_')

    if not id_:
        raise Exception("No form data loaded")
    try:
        s = 0
        lock = 0
        if status_ == 'done':
            s = 1
        elif status_ == 'undone':
            s = 0

        if status_ == 'lock':
            lock = 1
        data = {'status': s, 'locked': lock}
        print('status', data)
        res = requests.post(server_ + '/api/formData/setStatus/' + str(id_), data=data,
                            headers={'Authorization': "Bearer " + token})

        res = res.json()
        if _var:
            SetVar(_var, res['success'])
        if not res['success']:
            raise Exception(res['message'])
    except Exception as e:
        PrintException()
        raise e

if module == "DownloadFile":
    id_ = GetParams('id_')
    download_ = GetParams('download_')
    save_ = GetParams('save_')

    try:
        if not id_:
            raise Exception("No queue ID provided")
        if not download_:
            raise Exception("No file to download provided")
        if not save_:
            raise Exception("No path to save file provided")
        
        data = {'file': download_}

        res = requests.post(server_ + '/api/formData/download/' + str(id_), data=data, headers={'Authorization': "Bearer " + token})
        if res.status_code == 200:
            with open(save_, 'wb') as ff:
                ff.write(res.content)
        else:
            raise Exception("Error ocurred while download file")
    except Exception as e:
        PrintException()
        raise e


if module == "setXperience":

    try:
        xperience = GetParams('xperience')
        extradata = GetParams('extradata')

        data = {'xperience': xperience, 'data': extradata}

        res = requests.post(server_ + '/api/form/extra', data=data,
                            headers={'Authorization': "Bearer " + token})

        if res.status_code != 200:
            raise Exception('An error has occurred')

    except Exception as e:
        PrintException()
        raise e






