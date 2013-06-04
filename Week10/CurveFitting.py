def LinearLeastSquaresFit(x,y):
    """Take in arrays representin (x,y) values for a set of linearly varying data and
    perform a linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties."""
    n  = len(x)
    xave = sum(x)/n
    yave = sum(y)/n
    xsqave = sum(x*x)/n
    xyave = sum(x*y)/n
    m = (xyave-xave*yave)/(xsqave-xave**2)
    b = (xsqave*yave-xave*xyave)/(xsqave-xave**2)
    uncer = y - (m * x + b)
    muncer = (sum(uncer*uncer)/(n*(n-2)*(xsqave-xave**2)))**.5
    buncer = (sum(uncer*uncer)*xsqave/(n*(n-2)*(xsqave-xave**2)))**.5
    
    return m,b,muncer,buncer

def WeightedLinearLeastSquaresFit(x,y,weight):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w.
    perform a weighted linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties.
    if the weights are all equal to one, the uncertainties on the parameters are calculated using the
    non-weighted least squares equations."""
    w = sum(weight)
    weightless=True
    for i in weight:
        if i!=1:
            weightless=False
    if weightless:
        return LinearLeastSquaresFit(x,y)
    wx = sum(weight*x)
    wxsq = sum(weight*x**2)
    wy = sum(weight*y)
    wxy = sum(weight*x*y)
    b = (wxsq*wy-wx*wxy)/(w*wxsq-wx**2)
    m = (w*wxy-wx*wy)/(w*wxsq-wx**2)
    muncer = (w/(w*wxsq-wx**2))**.5
    buncer = (wxsq/(w*wxsq-wx**2))**.5
    return m,b,muncer,buncer
