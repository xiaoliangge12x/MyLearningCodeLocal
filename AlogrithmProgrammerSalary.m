clc;
clear;
close all;

% sample x<-->programmer salary   y<-->alogrithm programmer salary
x = [1.3854; 1.2213; 1.1009; 1.0655; 0.09503];
y = [2.1332; 2.0162; 1.9138; 1.8621; 1.8016];

a = 0;
b = 0;
n = 5;
y_hat = a*x + b*ones(n,1);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function y_hat = oneElementRegressionModel(a, b, x)
    % y_hat=a*x+b   x(5,1)<->vector a,b<->scalar
    y_hat=a*x+b;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function J = costFunction(a, b, x, y)
    % 0.5*MSE(mean square error)
    n = 5;
    J = 0.5*sum((y-a*x-b*ones(n,1)).^2)/n;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [a_op, b_op] = optimizationMethod(a, b, x, y)
    %a_op = a - e*(?J/?a)   b_op = b - e*(?J/?b)
    n = 5;
    e = 0.01;
    y_hat = oneElementRegressionModel(a, b, x);
    delta_a = sum((y_hat - y).*x)/n;
    delta_b = sum(y_hat-y)/n;
    a_op = a - e*delta_a;
    b_op = b - e*delta_b;
end