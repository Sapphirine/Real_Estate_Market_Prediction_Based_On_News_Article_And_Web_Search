
data = [257.074281,257.544815,257.921280,258.278807,258.614458,258.884034,259.090551,259.266145,259.435645,259.737281,260.018171,260.290103];

S = readtable('sentiment score.xlsx');

HPI = (S.HPI)';
HPI = HPI(85:end);

month = zeros(1,45);
for i = 1:45
    month(i)=2014+(i-1)*1/12 ;  
end


for i=1:12
month1 = month(1:33);
month2 = month(34:33+i);
    
figure;
plot(month1,HPI,'-*','LineWidth',2);hold on;
plot(month2,data,'-*','LineWidth',2);
xlim([2014 2018]);ylim([210 270]);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('ARIMAX and Google Search');
xlabel('Time');ylabel('HPI');


drawnow
frame = getframe(1);
im = frame2im(frame);
[A,map] = rgb2ind(im,256); 
imwrite(A,map,'ARIMAX and Google Search.gif','WriteMode','append','DelayTime',0.5)    
  
end



