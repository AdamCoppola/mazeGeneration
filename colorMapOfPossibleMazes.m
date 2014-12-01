maxGridSize = 10;
numPosMazes = zeros(maxGridSize, maxGridSize)
for i = 2:maxGridSize
    for j = 2:maxGridSize
        numPosMazes(i, j) = log(numPossibleMazes(i, j));
    end
end
surf(numPosMazes)