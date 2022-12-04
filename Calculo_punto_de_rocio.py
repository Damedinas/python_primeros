
import math as mt

T=float(input("Ingrese la temperatura ambiente en °C = "))
h=float(input("Ingrese la altitud en MSNM "))
H1=float(input("Ingrese la Humedad relativa (%)"))
T1=273.15+T
R = 8.31432 #constante gases
P0 = 101325 #Pa
MasaMolarAire = 0.0289644
G= 9.81
P=(P0*mt.exp((-MasaMolarAire*G*h)/(R*T1))/1000)
print('la presión atmosférica de la zona es: ', P, 'kPa')
Psat=(mt.exp((16.461*T-114.86)/(T+231.67)))
print('La presión de saturación es:', Psat,'kPa')
Pv = (H1/100)*Psat
print('la presión de vapor es: ', Pv, 'kPa')
Habsoluta=0.622*(Pv/(P-Pv))
print('la Humedad Absoluta es: ', Habsoluta,'Kilogramos de vapor/Kilogramos de aire seco')
v=((1/29)+(Habsoluta/18))*((R*T1)/(P))
print('el volumen específico es: ', v,' m3/kg de aire seco ')
Densidad=((1+Habsoluta)/v)
print('La densidad del aire humedo es : ', Densidad, 'kg/m3')
TR=((-231.67)-((3928.5)/(mt.log((Pv/100)/140974)))) # logbase 10
print(' la temperatura de rocio es :', TR,'°C')


