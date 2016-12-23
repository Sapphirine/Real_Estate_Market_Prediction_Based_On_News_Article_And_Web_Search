
data = [252.385486  248.429516  238.388179  242.459128  237.403266  235.452895  221.323516  215.357509  213.355707  219.781255  209.203158  205.024185];

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
plot(month2,data1,'-*','LineWidth',2);
xlim([2014 2018]);ylim([200 275]);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('SVR and Web Ariticles');
xlabel('Time');ylabel('HPI');


drawnow
frame = getframe(1);
im = frame2im(frame);
[A,map] = rgb2ind(im,256); 
imwrite(A,map,'SVR and Web Ariticles.gif','WriteMode','append','DelayTime',0.5)    
  
end


