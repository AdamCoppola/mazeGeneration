function plotTimeGrowth(topBound)
    timeGrowth = zeros(topBound, 1);
    for n = 1: topBound
        tic;
        numPossibleMazes(n,n);
        timeGrowth(n) = toc;
    end
    plot(timeGrowth)
end