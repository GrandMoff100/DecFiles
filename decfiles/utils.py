import random


def random_string(length: int) -> str:
    def gen():
        for _ in range(length):
            yield '%02x' % random(0, 16)
    return ''.join(gen())
