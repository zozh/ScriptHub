# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2023/09/25 17:19:11
@Author  :   zouzhao
@Version :   1.0
@Contact :   wszwc3721@163.com
@License :   Copyright (c) 2023 by zouzhao, All Rights Reserved.
@Description    : 日志类   

"""

import os
import logging
import concurrent.futures
from datetime import datetime
from pathlib import Path
from typing import NoReturn


class Logger:
    """日志类"""

    def __init__(
        self,
        log_path: str,
        is_cmd: bool = False,
        print_level: int = logging.DEBUG,
        file_level: int = logging.INFO,
        formatter: str = None,
    ):
        """初始化

        Args:
            file_path (str, optional): 日志文件路径. 默认 None.
            is_cmd (bool, optional): 是否开启控制台日志输出. 默认 False.
            print_level (str, optional): CMD 日志等级，默认 DEBUG.
            file_level (str, optional): 文件日志等级，默认 INFO.
            formatter (str, optional): 日志格式化字符串.为 None 使用默认.

        Raises:
            ValueError: 格式化字符错误抛出
            ValueError: 日志输出位置未指定抛出
        """
        self._logger = logging.getLogger(log_path)
        self._logger.setLevel(logging.INFO)
        self._is_cmd = False
        self._is_file = False
        if formatter:
            try:
                fmt = logging.Formatter(formatter)
            except BaseException:
                raise ValueError("格式化字符错误")
        else:
            fmt = logging.Formatter(
                "[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
            )
        if is_cmd:
            # 设置 CMD 日志
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(print_level)
            self._logger.addHandler(sh)
            self._is_cmd = True
        if log_path != "" and log_path != None:
            # 设置文件日志
            fh = logging.FileHandler(log_path, encoding="utf-8")
            fh.setFormatter(fmt)
            fh.setLevel(file_level)
            self._logger.addHandler(fh)
            self._is_file = True
        if not self._is_cmd and not self._is_file:
            raise ValueError("日志输出位置未指定")

        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    def debug(self, message: str, *args) -> NoReturn:
        """debug 等级日志

        Args:
            message (str): 消息

        Returns:
            NoReturn
        """
        self._logger.debug(message, *args)
        # self.executor.submit(self._logger.debug, message, *args)

    def info(self, message: str, *args) -> NoReturn:
        """info 等级日志

        Args:
            message (str): 消息

        Returns:
            NoReturn
        """
        self._logger.info(message, *args)
        # self.executor.submit(self._logger.info, message, *args)

    def warning(self, message: str, *args) -> NoReturn:
        """warning 等级日志

        Args:
            message (str): 消息

        Returns:
            NoReturn
        """
        self._logger.warn(message, *args)
        # self.executor.submit(self._logger.warn, message, *args)

    def error(self, message: str, *args) -> NoReturn:
        """error 等级日志

        Args:
            message (str): 消息

        Returns:
            NoReturn
        """
        self._logger.error(message, *args)
        # self.executor.submit(self._logger.error, message, *args)

    def critical(self, message: str, *args) -> NoReturn:
        """critical 等级日志

        Args:
            message (str): 消息

        Returns:
            NoReturn
        """
        self._logger.critical(message, *args)
        # self.executor.submit(self._logger.critical, message, *args)

    def set_cmd_log_level(self, level: int) -> NoReturn:
        """设置控制台输出日志等级

        Args:
            level (int): 输出等级,eg: logging.INFO

        Returns:
            NoReturn
        """
        if self._is_cmd:
            self._logger.handlers[0].setLevel(level)
        else:
            raise RuntimeError("没有设置控制台输出")

    def set_file_log_level(self, level: int) -> NoReturn:
        """设置文件输出日志等级

        Args:
            level (int): 输出等级

        Returns:
            NoReturn
        """
        if not self._is_file:
            raise RuntimeError("没有设置文件输出")
        if self._is_cmd:
            self._logger.handlers[1].setLevel(level)
        if not self._is_cmd:
            self._logger.handlers[0].setLevel(level)


def loggers(
    file_path: str = None,
    is_cmd: bool = False,
    print_level: str = logging.DEBUG,
    file_level: str = logging.INFO,
) -> Logger:
    """返回日志类

    Args:
        file_path (str, optional): 日志文件路径. 默认 None.
        is_cmd (bool, optional): 是否开启控制台日志输出. 默认 False.
        print_level (str, optional): CMD 日志等级，默认 DEBUG.
        file_level (str, optional): 文件日志等级，默认 INFO.


    Returns:
        Logger: 日志类
    """
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if file_path is not None:
        file_path = r"{}@{}.log".format(Path(file_path).stem, now)
    CMD_LOG_LEVEL = os.environ.get("CMD_LOG_LEVEL", print_level)
    FILE_LOG_LEVEL = os.environ.get("FILE_LOG_LEVEL", file_level)
    logger = Logger(file_path, is_cmd, CMD_LOG_LEVEL, FILE_LOG_LEVEL)
    return logger


if __name__ == "__main__":
    pass
