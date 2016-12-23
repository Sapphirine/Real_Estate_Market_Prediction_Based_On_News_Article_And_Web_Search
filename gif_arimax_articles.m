
data = [257.530784,258.047361,259.173626,259.591458,259.971788,260.362292,260.490721,260.996530,261.449611,261.881582,262.264483,262.606734];

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
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('ARIMAX and Web Ariticles');
xlabel('Time');ylabel('HPI');


drawnow
frame = getframe(1);
im = frame2im(frame);
[A,map] = rgb2ind(im,256); 
imwrite(A,map,'ARIMAX and Web Ariticles.gif','WriteMode','append','DelayTime',0.5)    
  
end


