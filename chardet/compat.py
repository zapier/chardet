import sys

PY2 = sys.version_info < (3, 0)


def wrap_ord(value):
    if PY2 or not isinstance(value, int):
        return ord(value)
    return value
