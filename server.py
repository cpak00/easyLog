import flask as F
from flask_httpauth import HTTPBasicAuth
import logparser
import config

app = F.Flask(__name__)
auth = HTTPBasicAuth()


# 认证
@auth.get_password
def get_password(username):
    for user in config.users:
        if user['username'] == username:
            return user['userpass']
    return None


@app.route('/', methods=['GET'])
@auth.login_required
def index_get():
    # 后缀名为log
    ext = '.log'
    log_list = logparser.get_log_list(ext)
    day_list = list(log_list.keys())
    day_list.sort(reverse=True)
    return F.render_template(
        'index.html', log_list=log_list, day_list=day_list)


@app.route('/log/<path>', methods=['GET'])
@auth.login_required
def log_get(path):
    lines = int(F.request.args.get('lines', '20'))

    if lines <= 0:
        content = logparser.look_all('../' + path)
    else:
        content = logparser.look_tail('../' + path, lines)

    return content


@app.route('/look/log/<path>', methods=['GET'])
@auth.login_required
def logall_get(path):
    content = logparser.look_all('../' + path)

    return F.render_template('log.html', logname=path, content=content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
