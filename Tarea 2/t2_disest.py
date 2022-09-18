#-------------------------------------------------------------------#

#TAREA 2
import numpy as np

def beta(fcomp):
    if fcomp < 28:
        return 0.85
    else:
        b1 = 0.85 - 0.05*(fcomp-28)/7
        if b1 <0.65:
            return 0.65
        else:
            return b1

#print(beta(21))

def rho_min(fcomp, fy):
    return max((0.25*fcomp**0.5)/fy, 1.4/fy)

rhomin = rho_min(21, 420)
#print(rhomin)

def rho_max(fcomp, fy, ec):
    b1 = beta(fcomp)
    return (ec/(ec+0.005))*(b1*0.85*fcomp/fy)

rhomax = rho_max(21, 420, 0.003)
#print(rhomax)

def asmin(base, d, fcomp, fy):
    rho = rho_min(fcomp, fy)
    area  = base*d*rho
    area_norma = (base*d*0.25*(fcomp)**0.5)/fy
    return max(area, area_norma)

Asmin = asmin(0.25, 0.44, 21, 420)
#print(Asmin)

def a_barra(num):
    area = np.pi*(0.5*(num/7)*0.0254)**2
    return area

def barras(amin):
    for i in range(4,7):
        if amin/a_barra(i) < 2:
            return i

#print(barras(Asmin))

def momento(W, l, factor):
    return (W*l**2)/factor


def rho_req(fcomp, fy, M, base, d):
    a = 0.85*fcomp/(fy)
    b = 1- 2*M/(0.9*0.85*base*fcomp*1000*(d**2))
    print(b)
    return a*(1-b**0.5)

#print(rho_req(28, 420, 147.121, 0.3, 0.39))

def a_req(rho, base, d, amin):
    if (rho*base*d - amin)*10000 > 0:
        return round((rho*base*d - amin)*10000,2)
    else: 
        return 0

with open('T2.txt', 'a', encoding = 'UTF-8') as file:
    file.write('Beta 1 = ' + str(beta(21)))
    file.write('\n')
    file.write('Rho_min = ' + str(rhomin))
    file.write('\n')
    file.write('Rho_max = ' + str(rhomax))
    file.write('\n')
    file.write('As_min = ' + str(Asmin*10000))
    file.write('\n')
    file.write('2 Barras No  ' + str(barras(Asmin)))
    file.write('\n')
    file.write('Rho_real = ' + str(2*a_barra(barras(Asmin))/(0.25*0.44)))
    file.write('\n')
    file.write('\n')

    file.write('Áreas de barras')
    
    for i in range (4,7):
        for j in range (1,4):
            file.write (str(j) + 'No '+ str(i) + ' = ' + str(j*round(a_barra(i)*10000, 2)))
            file.write('\n')



    file.write('Vigas entrepiso')
    file.write('\n')

    file.write('Viga AB')
    file.write('\n')

    ma = (momento(25.572, 6.5, 24))
    ra = (rho_req(21, 420, ma, 0.25, 0.44))
    areaa = (a_req(ra, 0.25, 0.44, Asmin))

    mab = (momento(25.572, 6.5, 14))
    rab = (rho_req(21, 420, mab, 0.25, 0.44))
    areaab = (a_req(rab, 0.25, 0.44, Asmin))

    mb1 = (momento(25.572, 6.5+7, 40))
    rb1 = (rho_req(21, 420, mb1, 0.25, 0.44))
    areab1 = (a_req(rb1, 0.25, 0.44, Asmin))

    file.write('M(A) = ' + str(ma))
    file.write('\n')
    file.write('Cuantía = ' + str(ra))
    file.write('\n')
    file.write('Área Adicional = ' + str(areaa))
    file.write('\n')
    file.write('\n')

    file.write('M(AB) = ' + str(mab))
    file.write('\n')
    file.write('Cuantía = ' + str(rab))
    file.write('\n')
    file.write('Área Adicional = ' + str(areaab))
    file.write('\n')
    file.write('\n')


    file.write('M(B) = ' + str(mb1))
    file.write('\n')
    file.write('Cuantía = ' + str(rb1))
    file.write('\n')
    file.write('Área Adicional = ' + str(areab1))
    file.write('\n')
    file.write('\n')

    file.write('Viga BC \n')

    mb2 = (momento(29.052, 7+6.5, 44))
    rb2 = (rho_req(21, 420, mb2, 0.25, 0.44))
    areab2 = (a_req(rb2, 0.25, 0.44, Asmin))

    mbc = (momento(29.052, 7, 16))
    rbc = (rho_req(21, 420, mbc, 0.25, 0.44))
    areabc = (a_req(rbc, 0.25, 0.44, Asmin))

    mc1 = (momento(29.052, 7+6, 44))
    rc1 = (rho_req(21, 420, mc1, 0.25, 0.44))
    areac1 = (a_req(rc1, 0.25, 0.44, Asmin))

    file.write('M(B) = ' + str(mb2))
    file.write('\n')
    file.write('Cuantía = ' + str(rb2))
    file.write('\n')
    file.write('Área Adicional = ' + str(areab2))
    file.write('\n')
    file.write('\n')

    file.write('M(BC) = ' + str(mbc))
    file.write('\n')
    file.write('Cuantía = ' + str(rbc))
    file.write('\n')
    file.write('Área Adicional = ' + str(areabc))
    file.write('\n')
    file.write('\n')

    file.write('M(C) = ' + str(mc1))
    file.write('\n')
    file.write('Cuantía = ' + str(rc1))
    file.write('\n')
    file.write('Área Adicional = ' + str(areac1))
    file.write('\n')
    file.write('\n')

    file.write('Viga CD')
    file.write('\n')
    mc2 = (momento(25.572, 6+7, 44))
    rc2 = (rho_req(21, 420, mc2, 0.25, 0.44))
    areac2 = (a_req(rc2, 0.25, 0.44, Asmin))

    mcd = (momento(25.572, 6, 16))
    rcd = (rho_req(21, 420, mcd, 0.25, 0.44))
    areacd = (a_req(rcd, 0.25, 0.44, Asmin))

    md1 = (momento(25.572, 6+6.5, 44))
    rd1 = (rho_req(21, 420, md1, 0.25, 0.44))
    aread1 = (a_req(rd1, 0.25, 0.44, Asmin))

    file.write('M(C) = ' + str(mc2))
    file.write('\n')
    file.write('Cuantía = ' + str(rc2))
    file.write('\n')
    file.write('Área Adicional = ' + str(areac2))
    file.write('\n')

    file.write('M(CD) = ' + str(mcd))
    file.write('\n')
    file.write('Cuantía = ' + str(rcd))
    file.write('\n')
    file.write('Área Adicional = ' + str(areacd))
    file.write('\n')
    file.write('\n')

    file.write('M(D) = ' + str(md1))
    file.write('\n')
    file.write('Cuantía = ' + str(rd1))
    file.write('\n')
    file.write('Área Adicional = ' + str(aread1))
    file.write('\n')
    file.write('\n')

    file.write('Viga DE')
    file.write('\n')
    md2 = (momento(25.572, 6.5+6, 40))
    rd2 = (rho_req(21, 420, md2, 0.25, 0.44))
    aread2 = (a_req(rd2, 0.25, 0.44, Asmin))

    mde = (momento(25.572, 6.5, 14))
    rde = (rho_req(21, 420, mde, 0.25, 0.44))
    areade = (a_req(rde, 0.25, 0.44, Asmin))

    me = (momento(25.572, 6.5, 24))
    re = (rho_req(21, 420, me, 0.25, 0.44))
    areae = (a_req(re, 0.25, 0.44, Asmin))

    file.write('M(D) = ' + str(md2))
    file.write('\n')
    file.write('Cuantía = ' + str(rd2))
    file.write('\n')
    file.write('Área Adicional = ' + str(aread2))
    file.write('\n')
    file.write('\n')
    
    file.write('M(DE) = ' + str(mde))
    file.write('\n')
    file.write('Cuantía = ' + str(rde))
    file.write('\n')
    file.write('Área Adicional = ' + str(areade))
    file.write('\n')
    file.write('\n')

    file.write('M(E) = ' + str(me))
    file.write('\n')
    file.write('Cuantía = ' + str(re))
    file.write('\n')
    file.write('Área Adicional = ' + str(areae))
    file.write('\n')

    file.write('Vigas Cubierta')
    file.write('\n')

    file.write('Viga AB')
    file.write('\n')

    ma = (momento(33.652, 6.5, 24))
    ra = (rho_req(21, 420, ma, 0.25, 0.44))
    areaa = (a_req(ra, 0.25, 0.44, Asmin))

    mab = (momento(33.652, 6.5, 14))
    rab = (rho_req(21, 420, mab, 0.25, 0.44))
    areaab = (a_req(rab, 0.25, 0.44, Asmin))

    mb1 = (momento(33.652, 6.5+7, 40))
    rb1 = (rho_req(21, 420, mb1, 0.25, 0.44))
    areab1 = (a_req(rb1, 0.25, 0.44, Asmin))

    file.write('M(A) = ' + str(ma))
    file.write('\n')
    file.write('Cuantía = ' + str(ra))
    file.write('\n')
    file.write('Área Adicional = ' + str(areaa))
    file.write('\n')
    file.write('\n')

    file.write('M(AB) = ' + str(mab))
    file.write('\n')
    file.write('Cuantía = ' + str(rab))
    file.write('\n')
    file.write('Área Adicional = ' + str(areaab))
    file.write('\n')
    file.write('\n')


    file.write('M(B) = ' + str(mb1))
    file.write('\n')
    file.write('Cuantía = ' + str(rb1))
    file.write('\n')
    file.write('Área Adicional = ' + str(areab1))
    file.write('\n')
    file.write('\n')

    file.write('Viga BC \n')

    mb2 = (momento(33.652, 7+6.5, 44))
    rb2 = (rho_req(21, 420, mb2, 0.25, 0.44))
    areab2 = (a_req(rb2, 0.25, 0.44, Asmin))

    mbc = (momento(33.652, 7, 16))
    rbc = (rho_req(21, 420, mbc, 0.25, 0.44))
    areabc = (a_req(rbc, 0.25, 0.44, Asmin))

    mc1 = (momento(33.652, 7+6, 44))
    rc1 = (rho_req(21, 420, mc1, 0.25, 0.44))
    areac1 = (a_req(rc1, 0.25, 0.44, Asmin))

    file.write('M(B) = ' + str(mb2))
    file.write('\n')
    file.write('Cuantía = ' + str(rb2))
    file.write('\n')
    file.write('Área Adicional = ' + str(areab2))
    file.write('\n')
    file.write('\n')

    file.write('M(BC) = ' + str(mbc))
    file.write('\n')
    file.write('Cuantía = ' + str(rbc))
    file.write('\n')
    file.write('Área Adicional = ' + str(areabc))
    file.write('\n')
    file.write('\n')

    file.write('M(C) = ' + str(mc1))
    file.write('\n')
    file.write('Cuantía = ' + str(rc1))
    file.write('\n')
    file.write('Área Adicional = ' + str(areac1))
    file.write('\n')
    file.write('\n')

    file.write('Viga CD')
    file.write('\n')
    mc2 = (momento(33.652, 6+7, 44))
    rc2 = (rho_req(21, 420, mc2, 0.25, 0.44))
    areac2 = (a_req(rc2, 0.25, 0.44, Asmin))

    mcd = (momento(33.652, 6, 16))
    rcd = (rho_req(21, 420, mcd, 0.25, 0.44))
    areacd = (a_req(rcd, 0.25, 0.44, Asmin))

    md1 = (momento(33.652, 6+6.5, 44))
    rd1 = (rho_req(21, 420, md1, 0.25, 0.44))
    aread1 = (a_req(rd1, 0.25, 0.44, Asmin))

    file.write('M(C) = ' + str(mc2))
    file.write('\n')
    file.write('Cuantía = ' + str(rc2))
    file.write('\n')
    file.write('Área Adicional = ' + str(areac2))
    file.write('\n')

    file.write('M(CD) = ' + str(mcd))
    file.write('\n')
    file.write('Cuantía = ' + str(rcd))
    file.write('\n')
    file.write('Área Adicional = ' + str(areacd))
    file.write('\n')
    file.write('\n')

    file.write('M(D) = ' + str(md1))
    file.write('\n')
    file.write('Cuantía = ' + str(rd1))
    file.write('\n')
    file.write('Área Adicional = ' + str(aread1))
    file.write('\n')
    file.write('\n')

    file.write('Viga DE')
    file.write('\n')
    md2 = (momento(33.652, 6.5+6, 40))
    rd2 = (rho_req(21, 420, md2, 0.25, 0.44))
    aread2 = (a_req(rd2, 0.25, 0.44, Asmin))

    mde = (momento(33.652, 6.5, 14))
    rde = (rho_req(21, 420, mde, 0.25, 0.44))
    areade = (a_req(rde, 0.25, 0.44, Asmin))

    me = (momento(33.652, 6.5, 24))
    re = (rho_req(21, 420, me, 0.25, 0.44))
    areae = (a_req(re, 0.25, 0.44, Asmin))

    file.write('M(D) = ' + str(md2))
    file.write('\n')
    file.write('Cuantía = ' + str(rd2))
    file.write('\n')
    file.write('Área Adicional = ' + str(aread2))
    file.write('\n')
    file.write('\n')
    
    file.write('M(DE) = ' + str(mde))
    file.write('\n')
    file.write('Cuantía = ' + str(rde))
    file.write('\n')
    file.write('Área Adicional = ' + str(areade))
    file.write('\n')
    file.write('\n')

    file.write('M(E) = ' + str(me))
    file.write('\n')
    file.write('Cuantía = ' + str(re))
    file.write('\n')
    file.write('Área Adicional = ' + str(areae))
    file.write('\n')

def comprobacion():
    a = int(input('cantidad N4'))
    b = int(input('cantidad N5'))
    c = int(input('cantidad N6'))
            