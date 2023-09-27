# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2023/09/26 18:45:08
@Author  :   zouzhao
@Version :   1.0
@Contact :   wszwc3721@163.com
@License :   Copyright (c) 2023 by zouzhao, All Rights Reserved.
@Description    :   
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
