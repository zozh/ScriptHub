# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2023/09/25 17:18:52
@Author  :   zouzhao
@Version :   1.0
@Contact :   wszwc3721@163.com
@License :   Copyright (c) 2023 by zouzhao, All Rights Reserved.
@Description    :  反射
"""

from importlib import import_module
from typing import NoReturn


class ClassInfoError(ValueError):
    """类信息错误"""


class Reflect:
    """现在实现了对模块的反射，对类的反射未实现"""

    def __init__(self, module_name: str) -> NoReturn:
        self.module_obj = import_module(module_name)
        self._get_all_variable_name()
        self._get_all_function_name()

    def _get_all_variable_name(self) -> NoReturn:
        """获得所有公开名

        Returns:
            NoReturn
        """
        variables = dir(self.module_obj)
        constant_variables = []
        private_variables = []
        normal_variables = []

        for variable in variables:
            if variable.isupper():
                constant_variables.append(variable)
            elif variable.startswith("__") or variable.startswith("_"):
                private_variables.append(variable)
            else:
                normal_variables.append(variable)
        self._normal_variables = normal_variables + constant_variables

    def _get_all_function_name(self) -> NoReturn:
        """获得所有公开方法名

        Returns:
            NoReturn
        """
        module_obj = self.module_obj
        functions = dir(module_obj)
        private_functions = []
        normal_functions = []

        for function_name in functions:
            if function_name.startswith("__") or function_name.startswith("_"):
                private_functions.append(function_name)
            else:
                function = getattr(module_obj, function_name)
                if callable(function):
                    normal_functions.append(function_name)
        self._normal_functions = normal_functions

    def update_variable(self, variable_name: str, new_value: object) -> NoReturn:
        """根据名字更新模块对应变量值

        Args:
            variable_name (str): 变量名字
            new_value (object): 新的值

        Raises:
            ClassInfoError: 变量不存在或没有权限访问抛出

        Returns:
            NoReturn
        """
        if variable_name not in self._normal_variables:
            raise ClassInfoError(f"{variable_name} 变量不存在或没有权限访问")
        setattr(self.module_obj, variable_name, new_value)

    def calling_method(self, method_name: str, *args, **kwargs) -> NoReturn:
        """根据名字调用模块对应方法

        Args:
            method_name (str): 方法名字

        Raises:
            ClassInfoError: 方法不存在或没有权限访问

        Returns:
            NoReturn
        """
        if method_name not in self._normal_functions:
            raise ClassInfoError(f"{method_name} 方法不存在或没有权限访问")
        method = getattr(self.module_obj, method_name)
        method(*args, **kwargs)
