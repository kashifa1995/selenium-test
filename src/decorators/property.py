import functools
import allure

from src.pages.base_element import BaseElement


def prop(func) -> BaseElement:
    @property
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res.prop_name = func.__name__
        return res

    return wrapper

def method(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> BaseElement:
        res = func(*args, **kwargs)
        if len(args)>1:
            res.par = args[1:]
        else:
            res.par = list(kwargs.values())
        res.method_name = func.__name__
        return res

    return wrapper


def allure_step(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name: str = func.__name__
        mod_func = func_name.replace("_", " ").capitalize()
        with allure.step(mod_func):
            return func(*args, **kwargs)

    return wrapper
