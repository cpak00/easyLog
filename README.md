# EasyLog

<!-- TOC -->

- [EasyLog](#easylog)
    - [项目简介](#项目简介)
        - [功能介绍](#功能介绍)
    - [启动说明](#启动说明)
    - [第三方库](#第三方库)

<!-- /TOC -->

## 项目简介

简单的在线日志检测系统

### 功能介绍

匹配文件名为xxx_yyy.log的日志, 后缀可在server.py的ext变量修改

* 分类管理
    
    >默认按照yyy分类

* 多页面查看

    >可打开多个日志的预览窗口, 默认查看最新的20条日志

* 自动更新

    >点击auto按钮, 根据auto右边的数字间隔自动刷新预览窗口

* 查看完整日志

    >点击加号可以打开新页面查看完整日志

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
