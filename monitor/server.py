import flask as F
import logparser

app = F.Flask(__name__)


@app.route('/', methods=['GET'])
def index_get():
    # 后缀名为log
    ext = '.log'
    log_list = logparser.get_log_list(ext)
    day_list = list(log_list.keys())
    day_list.sort(reverse=True)
    return F.render_template(
        'index.html', log_list=log_list, day_list=day_list)


@app.route('/log/<path>', methods=['GET'])
def log_get(path):
    lines = int(F.request.args.get('lines', '20'))

    if lines <= 0:
        content = logparser.look_all('../' + path)
    else:
        content = logparser.look_tail('../' + path, lines)

    return content
    '''
    return F.render_template(
        'log.html',
        logname=path,
        content=content)
    '''

@app.route('/look/log/<path>', methods=['GET'])
def logall_get(path):
    content = logparser.look_all('../' + path)

    return F.render_template(
        'log.html',
        logname=path,
        content=content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
