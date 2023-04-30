


cpdef clear_z_buffer(int[:, :, :,] nump_array, tuple color):
    
    cdef int i = 0 
    cdef int j = 0
    print(nump_array.shape)
    cdef int N = nump_array.shape[0]
    cdef int K = nump_array.shape[1]

    for i in range(N):
        for j in range(K):
            nump_array[i][j][0] = color[0]
            nump_array[i][j][1] = color[1]
            nump_array[i][j][2] = color[2]
