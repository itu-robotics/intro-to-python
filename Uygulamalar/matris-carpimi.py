def satir_sutun_carpma(r, c):
    return r[0]*c[0] + r[1]*c[1] + r[2]*c[2]

def matris_carpma(m1,m2):
    m1r1 = m1[0]
    m1r2 = m1[1]
    m1r3 = m1[2]
    m2c1 = [m2[0][0],m2[1][0],m2[2][0]]
    m2c2 = [m2[0][1],m2[1][1],m2[2][1]]
    m2c3 = [m2[0][2],m2[1][2],m2[2][2]]
    
    i11 = satir_sutun_carpma(m1r1,m2c1)
    i12 = satir_sutun_carpma(m1r1,m2c2)
    i13 = satir_sutun_carpma(m1r1,m2c3)
    i21 = satir_sutun_carpma(m1r2,m2c1)
    i22 = satir_sutun_carpma(m1r2,m2c2)
    i23 = satir_sutun_carpma(m1r2,m2c3)
    i31 = satir_sutun_carpma(m1r3,m2c1)
    i32 = satir_sutun_carpma(m1r3,m2c2)
    i33 = satir_sutun_carpma(m1r3,m2c3)
    
    result = [[i11,i12,i13],[i21,i22,i23],[i31,i32,i33]]
    return result
    
matrix1 = [[1,2,3],[2,2,2],[0,-1,5]]
matrix2 = [[10,0,3],[1,2,-2],[2,-1,1]]

sonuc_matrisi = matris_carpma(matrix1, matrix2)

print(sonuc_matrisi[0])
print(sonuc_matrisi[1])
print(sonuc_matrisi[2])