#programa que realiza un descuento en una panadería 

precio2=27
descuento=(float)
total=(float)
barras2=float(input("cuántas barras vendiste, que no son del día? "))
barras1=float(input("cuántas barras vendiste del día de hoy: "))
print("precio del pan del día es: ", precio2)
if barras2!=0:
    descuento=(27*barras2)*.60
    total=(27*barras2)-descuento
    print("total a pagar con descuento es: ",total)
total=barras1*precio2
print("El total a pagar sin descuento es: ", total)
