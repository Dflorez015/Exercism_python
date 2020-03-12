def spiral_matrix(size):
    if size <= 0:
        return []
    
    matrix = [fila[:] for fila in [[0]*size]*size]
    com_fila=0
    fin_fila=size-1
    com_col=0
    fin_col=size-1
    cont=1    
    while (True):
        if cont>size*size:
            break
        for c in range (com_col, fin_col+1):
            matrix[com_fila][c]=cont
            cont+=1
        com_fila+=1
        for r in range (com_fila, fin_fila+1):
            matrix[r][fin_col]=cont
            cont+=1
        fin_col-=1
        for c in range (fin_col, com_col-1, -1):
            matrix[fin_fila][c]=cont
            cont+=1
        fin_fila-=1
        for r in range (fin_fila, com_fila-1, -1):
            matrix[r][com_col]=cont
            cont+=1
        com_col+=1
    return matrix