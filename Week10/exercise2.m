experiment = importdata('radioactivedecay.dat');
t = experiment.data(:,1);
N = experiment.data(:,2);
fun = @(A,b,x) A.*exp(b.*x);
fittedmodel = fit(t,N,fun,'StartPoint',[1 1]);
figure(42)
plot(t,N,'b*')
hold on
plot(fittedmodel,'r-')
legend('Data','Fitted Line')