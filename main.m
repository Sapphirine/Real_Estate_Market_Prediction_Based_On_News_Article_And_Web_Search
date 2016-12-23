clear;
clc;
close all;
S = readtable('sentiment score.xlsx');
month = S.Month;
HPI = (S.HPI)';
sentiment1 = (S.Sentiment1)';
sentiment2 = (S.Sentiment2)';
month2 = zeros(1,84);

for i = 1:84
    month2(i)=2007+(i-1)*1/12 ;  
end

figure;
plot(month2,HPI,'-o','LineWidth',2,...
    'MarkerSize',3,'MarkerEdgeColor','r');
xlim([2007 2014]);

figure;
plot(month2,sentiment1,'-o','LineWidth',2,...
    'MarkerSize',3,'MarkerEdgeColor','r');
xlim([2007 2014]);


figure;
plot(month2,sentiment2,'-o','LineWidth',2,...
    'MarkerSize',3,'MarkerEdgeColor','r');
xlim([2007 2014]);