"""
Solución del laboratorio
"""

from custom_functions import temperature_methods

import statistics as stats
print("//////////////////////Digite las temperaturas de Nariño/////////////////////////////////////")
am=nariño=temperature_methods.base1()

print("//////////////////////Digite las temperaturas de santander//////////////////////////////////")
lo=santander=temperature_methods.base2()

print("//////////////////////Digite las temperaturas de la guajira/////////////////////////////////")
pre=guajira=temperature_methods.base3()
print("////////////////////////////////////////////////////////////////////////////////////////////")
promedio_guajira=temperature_methods.prom3(guajira)
promedio_nariño=temperature_methods.prom1(nariño)
promedio_santander=temperature_methods.prom2(santander)
print("a) El promedio de temperatura en Nariño fue",promedio_nariño,"°")
a=temperature_methods.mes_caliente(nariño)
print("//////////////////////////////////////////////////////////")
print("a) El promedio de temperatura en Santander fue",promedio_santander,"°")
b=temperature_methods.mes_caliente(santander)
print("//////////////////////////////////////////////////////////")
print("a)El promedio de temperatura en La Guajira fue",promedio_guajira,"°")
c=temperature_methods.mes_caliente(guajira)
print("//////////////////////////////////////////////////////////")
list1 = nariño.values()
max1 = max(list1)
list2 = santander.values()
max2 = max(list2)
list3 =guajira.values()
max3= max(list3)
promedio_meses=max1+max2+max3
mas=promedio_meses/3
print("d) El promedio de los meses más calientes fue", mas)
print("//////////////////////////////////////////////////////////")
if promedio_guajira==promedio_santander==promedio_nariño:
    print("e) Los tres departamentos tuvieron la misma temperatura")
if promedio_nariño<promedio_guajira>promedio_santander:
    print("e) En promedio la Guajira fue el departamento más caliente")
elif promedio_guajira<promedio_nariño>promedio_santander:
    print("e) En promedio Nariño fue el departamento más caliente")
elif promedio_guajira<promedio_santander>promedio_nariño:
    print("e) En promedio Santander fue el departamento más caliente")

print("//////////////////////////////////////////////////////////")


if a==b==c:
    print("f) Las tres temperaturas son iguales")

elif b<a>c:
    print("f) La mayor temperatura fue",a,"se dio en el departamento de Nariño")
    temperature_methods.mes_caliente(nariño)
elif a<b>c:
    print("f) la mayor temperatura fue",b,"se dio en el departamento de Santander")
    temperature_methods.mes_caliente(santander)
elif a<c>b:
    print("f)la mayor temperatura fue",c,"se dio en el departamento de la Guajira")
    temperature_methods.mes_caliente(guajira)
print("//////////////////////////////////////////////////////////")
mu=promedio_santander
ma=promedio_guajira
me=promedio_nariño
tempe=(mu + me + ma)

xyz=tempe/3

print("b) El promedio de la temperatura a nivel nacional es de", xyz,"°")

print("////////////////////////////////////////////////////////////////////////////////////////////")

desv1=am.values()
desv2=lo.values()
desv3=pre.values()
desv_san=(stats.pstdev(desv2))
desv_nari=(stats.pstdev(desv1))
desv_gua=(stats.pstdev(desv3))
print("g) La desviación estándar de Nariño es:",desv_nari)
print("g) La desviación estándar de Santander es:",desv_san)
print("g) La desviación estándar de la Guajira es:",desv_gua)