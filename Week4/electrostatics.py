
def pointPotential(x , y, q, posx, posy):
    """Finds potential at x and y due to a point charge of charge q at posx, and posy"""
    k = 8.987551787368176*10**9
    return (k*q/((x-posx)**2+(y-posy)**2)**.5)

def dipolePotential(x, y, q, d):
    """Finds potential at x and y due to a dipole a distance d separated"""
    v = pointPotential(x, y, q, 0, -d*.5) + pointPotential(x, y, -q, 0, d*.5)
    return v
