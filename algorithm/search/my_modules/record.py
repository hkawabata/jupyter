import numpy as np
import random


def get_unique_records(num, sort=False):
    if not sort:
        data = [[key, key*10] for key in random.sample(range(num), num)]
    else:
        data = [[key, key*10] for key in range(num)]
    return np.array(data)

