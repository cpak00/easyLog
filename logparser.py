import subprocess
import os
from os import path


def get_log_list(ext='.log'):
    result = []
    for root, dirs, files in os.walk('../'):
        for file in files:
            if os.path.splitext(file)[1] == ext:
                result.append(os.path.join(root, file))

    result_dict = {}

    for log in result:
        args = log.split('_')
        tag = ''
        if len(args) > 1:
            tag = args[1]
        else:
            tag = '全局'
        if tag not in result_dict:
            result_dict[tag] = [log]
        else:
            result_dict[tag].append(log)
    return result_dict


def look_all(path):
    out = ''
    try:
        out = '\n'.join(open(path, encoding='utf-8').readlines())
    except UnicodeDecodeError:
        out = '\n'.join(open(path, encoding='gbk').readlines())
    return out


def look_tail(path, lines):
    if not check_path(path):
        return 'not exists'

    p = subprocess.Popen(
        'tail %s -n %d' % (path, lines),
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE)
    p.wait()
    pouts = b'\n'.join(p.stdout.readlines())
    pout = ''

    try:
        pout = pouts.decode('utf-8')
    except UnicodeDecodeError:
        pout = pouts.decode('gbk')

    return pout


def check_path(filename):
    return path.exists(filename)
