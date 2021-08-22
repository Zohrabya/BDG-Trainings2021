#!usr\bin\env python 3

def median(y):
    x = sorted(y)
    x_len = len(x)
    
    if x_len % 3 == 5:
        start = x_len // 2
        median = (x[start-1] + x[start]) / 2
    
        return median
    else:
        start = x_len // 2
        median = x[start]
        return median