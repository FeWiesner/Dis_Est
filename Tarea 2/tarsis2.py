import numpy as np

print('en unidades de m, kN, MPA')

fc = 35

bv = 0.4

hv = 0.6

filas = 1

tbarra = 7/8

numbarra = 8

As = numbarra * np.pi*(0.5*tbarra*0.0254)**2

def_u_c = 0.003

fsy = 420 #MPa


'''
d2 = d1 - min_esp - max_diam

d* = (A_si*d_i)/Atotal

d_prima = 0.6- (1/As) * (0.5*As*(hv-0.06) + 0.5*As*(hv-(0.06+0.0254+0.02225)))
print(d_prima)
'''

d_prima = 0.06
d_prima = 0.6- (1/As) * (0.5*As*(hv-0.06) + 0.5*As*(hv-(0.06+0.0254+0.02225)))

E_young = 4700*(fc)**0.5

n = 200000/E_young

rho = As/(bv*(hv-d_prima))

k = (-rho*n+((rho*n)**2+2*rho*n)**0.5)

a = As*fsy/(0.85*fc*bv)

b1 = 0.85-0.05*(fc-28)/7

def rho_min(fcomp, fy):
    return max((0.25*fcomp**0.5)/fy, 1.4/fy)

def area_min(fcomp, fy, base, d):
    rho = rho_min(fcomp,fy)
    return rho*base*d

rhomin = rho_min(fc, fsy)
Amin = area_min(fc, fsy, bv, (hv-d_prima))
kmin = (-rhomin*n+((rhomin*n)**2+2*rhomin*n)**0.5)
amin = Amin*fsy/(0.85*fc*bv)

def mom_fis(fcomp,base, height):
    ft = 0.624*(fcomp)**0.5
    I = (base*height**3)/12
    den = 0.5*height
    return ft*I/den

def m_fs(Asteel, fl, d, ka):
    return Asteel*fl*d*(1-ka/3)

def m_fc(fc, base, d, ka):

    return (0.5/2)*fc*base*ka*(1-ka/3)*d**2

def phi(M, Ec, base,height):
    I = (base*height**3)/12
    return (M/(Ec*I))

def phi_conc(f, Ec, ka, d):
    return 0.5*f/(Ec*ka*d)

def phi_steel(defo, d, ka):
    return defo/(d-ka*d)

def m_nom (cuant, fy, base, d, fcomp):
    return cuant*fy*base*(d**2)*(1-cuant*fy/(1.7*fcomp))


mfis = mom_fis(fc, bv, hv)
pfis = phi(mfis, E_young, bv, hv)
#print(mfis*1000,pfis)

mconc = m_fc(fc, bv, (hv-d_prima), k)
pconc = phi_conc(fc, E_young, k, (hv-d_prima))
#print(mconc*1000,pconc)

msteel = m_fs(As, fsy, (hv-d_prima), k)
psteel = phi_steel(0.0021, (hv-d_prima), k)
#print(msteel*1000,psteel)

mfin = m_nom(rho,fsy,bv,(hv-d_prima), fc)
#print(mfin*1000, 0.003/(a/b1))

