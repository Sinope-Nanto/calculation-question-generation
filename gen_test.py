from evaluation import *
from prime_number import *

def dict_add(dict_1:dict, dict_2:dict) -> dict:
    common_key = dict_1.keys() & dict_2.keys()
    re_dict = {}
    for key in common_key:
        re_dict[key] = dict_1[key] + dict_2[key]
    for key in dict_1.keys() - common_key:
        re_dict[key] = dict_1[key]
    for key in dict_2.keys() - common_key:
        re_dict[key] = dict_2[key]
    return re_dict


def prime_factor(n:int) -> dict:
    if n > (1 << 32):
        raise Exception('Too Large')
    prime_factor = {}
    if n < (1 << 13):
        for p in PRIME_NUMBER_LIST_100:
            if n % p == 0:
                return  dict_add({p : 1}, prime_factor(n//p))
    elif n < (1 << 19):
        for p in PRIME_NUMBER_LIST_1000:
            if n % p == 0:
                return  dict_add({p : 1}, prime_factor(n//p))
    elif n < (1 << 26):
        for p in PRIME_NUMBER_LIST_10000:
            if n % p == 0:
                return  dict_add({p : 1}, prime_factor(n//p))
    else:
        for p in PRIME_NUMBER_LIST_100000:
            if n % p == 0:
                return  dict_add({p : 1}, prime_factor(n//p))
    return {n : 1}

