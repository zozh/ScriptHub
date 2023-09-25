# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2023/09/20 09:39:01
@Author  :   zouzhao
@Version :   1.0
@Contact :   wszwc3721@163.com
@License :   Copyright (c) 2023 by zouzhao, All Rights Reserved.
@Description    :   json 工具类
"""

import json


def read_json(path: str) -> dict:
    """读取 json 文件
    Args:
        path (str): 文件路径

    Raises:
        e: Exception

    Returns:
        dict: 解析后的字典
    """
    with open(path) as file_obj:
        content = file_obj.read()
        try:
            return json.loads(content)
        except Exception as e:
            raise RuntimeError(f"{path} 加载异常\n{e}")


def write_json(path: str, content: str):
    """写入 json

    Args:
        path (str): 文件路径
        content (str): 文本内容
    """
    with open(path, "a") as file_obj:
        json.dump(content, file_obj, indent=4, sort_keys=True)


if __name__ == "__main__":
    pass
