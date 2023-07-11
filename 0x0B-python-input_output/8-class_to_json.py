#!/usr/bin/python3
""" function that returns the dictionary. """


def class_to_json(obj):
    """ Function retuns dictionary """
    dic = {}
    if hasattr(obj, "__dict__"):
        dic = obj.__dict__.copy()
    return dic
