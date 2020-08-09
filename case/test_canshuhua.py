# -*- coding: utf-8 -*-
# @author : 刘捷
# @time   : 2020-08-06 21:21

import pytest


def add(x, y):
    """定义函数，实现某个功能"""
    return x + y


@pytest.mark.parametrize("test_input, expected",
                         [
                             [{"a": 1, "b": 2}, 3],
                             [{"a": "1", "b": "2"}, "12"]
                         ])
def test_add(test_input, expected):
    result = add(test_input['a'], test_input["b"])  # 实际结果
    expected = expected  # 期望结果
    assert result == expected
