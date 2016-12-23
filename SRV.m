S = xlsread('sentiment score.xlsx');
Y = S(:,2);
X = S(:,4);
X = X(49:116);
Y = Y(49:116);
%time = [1:35]';
%testX = X(49:83);
%testY = Y(49:83);
time = [1:68]';
testX = X;
testY = Y;

T = table (time, testX, testY);
N = size(T,1);

rng(10); % For reproducibility
cvp = cvpartition(N,'Holdout',0.4);
idxTrn = training(cvp); % Training set indices
idxTest = test(cvp);    % Test set indices

Mdl = fitrsvm(T(idxTrn,:),'testY','Standardize',true);
YFit = predict(Mdl,T(idxTest,:));

table(T.testY(idxTest),YFit,'VariableNames',...
    {'Observed_HPI','Predicted_HPI'})

