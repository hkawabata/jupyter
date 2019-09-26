import numpy as np
import random


def get_unique_records(num):
    data = [[key, key*10] for key in random.sample(range(num), num)]
    return np.array(data)

