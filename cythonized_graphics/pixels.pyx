
#When len(nump_array)>=422, clear_z_buffer starts to become more efficient than efficient_clear_z_buffer

cpdef clear_z_buffer(int[:, :, :,] nump_array, tuple color):
    
    cdef int i = 0 
    cdef int j = 0
    cdef int N = nump_array.shape[0]
    cdef int K = nump_array.shape[1]

    for i in range(N):
        for j in range(K):
            nump_array[i][j][0] = color[0]
            nump_array[i][j][1] = color[1]
            nump_array[i][j][2] = color[2]


cpdef efficient_clear_z_buffer(int[:, :, :,] nump_array, int[:, :] changed_pixels , tuple color):
    # int N = changed_pixels.shape[0]
    cdef int i = 0
    cdef int N = changed_pixels.shape[0]
    for i in range(N):
        nump_array[changed_pixels[i][0]][changed_pixels[i][1]][0] = color[0]
        nump_array[changed_pixels[i][0]][changed_pixels[i][1]][1] = color[1]
        nump_array[changed_pixels[i][0]][changed_pixels[i][1]][2] = color[2]
    

cpdef fill_screen(unsigned char [:, :, :,] nump_array, tuple color):
    
    cdef int i = 0 
    cdef int j = 0
    cdef int N = nump_array.shape[0]
    cdef int K = nump_array.shape[1]

    for i in range(N):
        for j in range(K):
            nump_array[i][j][0] = color[0]
            nump_array[i][j][1] = color[1]
            nump_array[i][j][2] = color[2]