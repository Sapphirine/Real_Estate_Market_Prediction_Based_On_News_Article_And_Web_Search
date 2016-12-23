
data = [266.514083  271.536460  259.472437  268.432764  271.466417  261.544300  253.423224  244.499854  232.437230  230.435620  234.598039  228.484523];

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
xlim([2014 2018]);ylim([200 275]);
set(gca,'xtick',[2014 2015 2016 2017]);
set(gca,'xticklabel',{'2014','2015','2016','2017'});
legend('original HPI','predicted HPI','Location','northwest');
title('SVR and Google Search');
xlabel('Time');ylabel('HPI');


drawnow
frame = getframe(1);
im = frame2im(frame);
[A,map] = rgb2ind(im,256); 
imwrite(A,map,'SVR and Google Search.gif','WriteMode','append','DelayTime',0.5)    
  
end



