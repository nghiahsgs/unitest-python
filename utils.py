def tinhTong(x,y):
    if x<0 or y<0:
        raise ValueError("x and y must be larger than 0")
    if type(x) not in [int,float] or type(y) not in [int,float]:
        raise TypeError("x and y must be interger or float")
    return x+y