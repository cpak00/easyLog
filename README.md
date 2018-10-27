# EasyLog

<!-- TOC -->

- [EasyLog](#easylog)
    - [项目简介](#项目简介)
    - [启动说明](#启动说明)
    - [第三方库](#第三方库)

<!-- /TOC -->

## 项目简介

简单的在线日志检测系统

## 启动说明

在日志文件目录下
```bash
git clone https://github.com/cpak00/easyLog.git & cd easyLog & bash run.sh

```

用户名密码配置在config.py下
以列表形式存在, 可以配置多个用户名密码对

浏览器访问
```
http://ip:5000/
```

## 第三方库

第三方库       | 版本   | 说明
---------------|--------|------
Flask          | 0.12.2 | 网站主服务
Flask-HTTPAuth | 3.2.4  | 网页验证服务
