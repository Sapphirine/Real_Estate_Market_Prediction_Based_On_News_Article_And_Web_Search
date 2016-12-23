clear;
clc;
close all;
S = readtable('sentiment score.xlsx');
month = S.Month;
HPI = (S.HPI)';
sentiment1 = (S.Sentiment1)';
sentiment2 = (S.Sentiment2)';
month2 = zeros(1,117);

for i = 1:105
    month2(i)=2007+(i-1)*1/12 ;  
end

tdata = (1:117);
tfit = (1:0.01:117)';
tfit2 = zeros(1,length(tfit));
for i=1:length(tfit)
    tfit2(i) = 2007+(i-1)*1/12/100; 
end

p_coeffs1 = polyfit(tdata,HPI,5);
yfit1 = polyval(p_coeffs1,tfit);

p_coeffs2 = polyfit(tdata,sentiment1,5);
yfit2 = polyval(p_coeffs2,tfit);
yfit2_1 = yfit2+1.25;
yfit2_2 = yfit2-1.25;

p_coeffs3 = polyfit(tdata,sentiment2,5);
yfit3 = polyval(p_coeffs3,tfit);
yfit3_1 = yfit3+0.8;
yfit3_2 = yfit3-0.8;

figure;
scatter(month2,HPI);
xlim([2007 2016]);hold on;
plot(tfit2,yfit1,'r-','LineWidth',2);
legend('HPI','Polynomial Fit','Location','NW');



figure;
scatter(month2,sentiment1);
xlim([2007 2016]);hold on;
plot(tfit2,yfit2,'r-','LineWidth',2);hold on;
plot(tfit2,yfit2_1,'g--');hold on;
plot(tfit2,yfit2_2,'g--');hold on;
legend('Sentiment Score based on News','Polynomial Fit','Location','NW');


figure;
scatter(month2,sentiment2);
xlim([2007 2016]);hold on;
plot(tfit2,yfit3,'r-','LineWidth',2);hold on;
plot(tfit2,yfit3_1,'g--');hold on;
plot(tfit2,yfit3_2,'g--');hold on;
legend('Sentiment Score based on Searching query','Polynomial Fit','Location','NW');

