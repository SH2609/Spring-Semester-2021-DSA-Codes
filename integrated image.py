array = [[1,0,0,1,0],[0,0,0,1,0],[0,1,0,1,0],[1,1,0,1,0],[1,0,0,0,1]]
def integratedImage(array):
    X = []
    Y = []
    C = 0
    for i in range(len(array)):
        for j in range(len(array[0])):
            C = array[i][j]
            for n in range(1,len(array)):
                if i - n >= 0:
                    C += array[i-n][j]
                if j - n >= 0:
                    C += array[i][j-n]
            X.append(C)
            C = 0
        Y.append(X)
        X = []
    return Y

print(integratedImage(array))