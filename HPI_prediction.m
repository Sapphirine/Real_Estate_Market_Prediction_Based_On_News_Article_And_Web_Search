clear;
clc;
close all;

data1 = [281.514083  286.536460  274.472437  283.432764  286.466417  276.544300  268.423224  259.499854  247.437230];
data2 = [273.548655  276.473248  277.476778  283.433496  286.566966  286.429597  288.543966  294.573611  297.575445];
data3 = [252.385486  248.429516  238.388179  242.459128  237.403266  235.452895  221.323516  215.357509  223.355707];
data4 = [264.414410  266.514266  257.460010  263.467568  278.434971  279.536475  285.515461  294.494626  307.539753];

S = readtable('sentiment score.xlsx');

HPI = (S.HPI)';
HPI = HPI(85:end);

month = zeros(1,42);
for i = 1:42
    month(i)=2014+(i-1)*1/12 ;  
end
month1 = month(1:33);
month2 = month(34:42);


figure;
plot(month1,HPI,'-*','LineWidth',2);hold on;
plot(month2,data1,'-*','LineWidth',2);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('SVR and searching query data');
xlabel('Time');ylabel('HPI');



figure;
plot(month1,HPI,'-*','LineWidth',2);hold on;
plot(month2,data2,'-*','LineWidth',2);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('ARIMAX and searching query data');
xlabel('Time');ylabel('HPI');

figure;
plot(month1,HPI,'-*','LineWidth',2);hold on;
plot(month2,data3,'-*','LineWidth',2);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('SVR and web news articles');
xlabel('Time');ylabel('HPI');

figure;
plot(month1,HPI,'-*','LineWidth',2);hold on;
plot(month2,data4,'-*','LineWidth',2);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('ARIMAX and web news articles');
xlabel('Time');ylabel('HPI');
