from math import log10, floor


def dict_remove(x, exclude=[]):
    """Remove items from a dict."""
    return dict((k, v) for k, v in x.items() if k not in exclude)


def dict_subset(x, include=[]):
    """Subset a dict."""
    return dict((k, v) for k, v in x.items() if k in include)


def rename(x, k, j):
    if k in x:
        x[j] = x[k]
        del x[k]


def unif_mean(a, b):
    return (a + b) * 0.5


def unif_var(a, b):
    """Uniform distribution variance."""
    return (a - b) ** 2 / 12


def rounded_var(x):
    """Variance implied by a rounded number."""
    k = trailing_zeros(x)
    return 10 ** (2 * k) / 12


def trailing_zeros(x):
    """ Number of trailing zeros in a number."""
    if x % 1 != 0 | x == 0:
        return 0
    magn = floor(log10(x))
    trailing = 0
    for i in range(1, magn + 1):
        if x % (10 ** i) == 0:
            trailing = i
        else:
            break
    return trailing
