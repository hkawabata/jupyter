# -*- coding: utf-8 -*-

def remove_module(module_name):
    u"""
    モジュール修正後の再読込がうまくいかないので一度消す
    """
    import sys
    try:
        del sys.modules[module_name]
    except Exception as e:
        pass