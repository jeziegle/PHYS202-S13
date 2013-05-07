
def pointPotential(x , y, q, posx, posy):
    """Finds potential at x and y due to a point charge of charge q at posx, and posy"""
    k = 8.987551787368176*10**9
    return (k*q/((x-posx)**2+(y-posy)**2)**.5)

def dipolePotential(x, y, q, d):
    """Finds potential at x and y due to a dipole a distance d separated"""
    v = pointPotential(x, y, q, 0, -d*.5) + pointPotential(x, y, -q, 0, d*.5)
    return v

def pointField(x,y,q,Xq,Yq):
    """Takes arrays (x,y) charge q and position Xq, Yq and returns a tuple of the electric field components (Ex,Ey)"""
    k = 8.987551787368176*10.**9.
    Ex = k*q*(x-Xq)/((x-Xq)**2+(y-Yq)**2)**.5
    Ey = k*q*(y-Yq)/((x-Xq)**2+(y-Yq)**2)**.5
    return Ex,Ey
