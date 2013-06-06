function [ m,b,muncer,buncer ] = weightedLSQFit(x, y,weight )
%Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w.
%perform a weighted linear least squares regression. Return the resulting slope and intercept
%parameters of the best fit line with their uncertainties.
%if the weights are all equal to one, the uncertainties on the parameters are calculated using the
%non-weighted least squares equations.
w = sum(weight);
wx = sum(weight.*x);
wxsq = sum(weight.*x.^2);
wy = sum(weight.*y);
wxy = sum(weight.*x.*y);
b = (wxsq.*wy-wx.*wxy)/(w.*wxsq-wx.^2);
m = (w.*wxy-wx.*wy)/(w.*wxsq-wx.^2);
muncer = (w/(w.*wxsq-wx.^2)).^0.5;
buncer = (wxsq/(w.*wxsq-wx.^2)).^0.5;
end

