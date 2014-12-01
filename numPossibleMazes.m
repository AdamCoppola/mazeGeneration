function res = numPossibleMazes(n, m)
    adj = zeros(n,n);
    for r = 1:n
        for c = 1:m
            i = ((r-1)*m)+c;
            if c > 1
                adj(i-1,i) = 1;
                adj(i, i-1) = 1;
            end
            if r > 1
                adj(i - m,i) = 1;
                adj(i, i-m) = 1;
            end
        end
    end
    
    degSeq = [2; repmat(3,m-2,1); 2; repmat([3; repmat(4, m-2,1); 3], n-2, 1); 2; repmat(3,m-2,1); 2];
    deg = diag(degSeq);

    lap = deg - adj;
    lap(1,:) = [];
    lap(:,1) = [];
    det(lap);
    res = det(lap);
end