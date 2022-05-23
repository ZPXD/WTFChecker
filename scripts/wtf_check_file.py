import sys


'''
Check file or filder from wherever you are.

ZPXD, Łukasz Pintal.
'''


def wtf_check_file(what):
    '''
    Copy this function to your program.

    Use this code in whatever program you need.
    '''
    
    #if what is folder:
    #    what = zip(what)

    import requests
    import os
    url = 'http://lukasz-pintal.pl/wtf'
    headers = {
        "user" : "",
        "key" : "",
        "msg" : "hi",
    }
    if 'www' in what[:10]:
        headers['what'] = what
    elif len(what) < 200 and os.path.exists(what):
        file = {'file': open(what,'rb')}
    else:
        headers['what'] = what
    
    r = requests.post(url, files=file, headers=headers)
    info = r.json()

    result = info['result']
    results = info['results']
    return result, results

if __name__ == "__main__":
    what = sys.argv[1]
    wtf_check_file(what)