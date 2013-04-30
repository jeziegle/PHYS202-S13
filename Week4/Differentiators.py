from numpy import zeros

def finiteDifference(x, y):
    """take a numerical derivative of y with respect to x, using a two point centered difference"""
    dydxCenter = zeros(y.shape,float)
    dydxCenter[1:-1] = (y[2:]-y[:-2])/(x[2:]-x[:-2])
    dydxCenter[0] = (y[1]-y[0])/(x[1]-x[0])
    dydxCenter[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydxCenter

def fourPtFiniteDiff(x, y):
    """Take a numerical derivative, using a four point centered difference to calculate each point on curve"""
    dydxFour = zeros(y.shape,float)
    for index in range(1,len(y)-3):
        dydxFour[index] = (y[index-2] - 8 * y[index-1] + 8 * y[index+1] - y[index+2])/ (12 * (x[index]-x[index-1]))
    dydxFour[0] = finiteDifference(x, y)[0]
    dydxFour[1] = finiteDifference(x, y)[1]
    dydxFour[-2] = finiteDifference(x, y)[-2]
    dydxFour[-1] = finiteDifference(x, y)[-1]
    return dydxFour
