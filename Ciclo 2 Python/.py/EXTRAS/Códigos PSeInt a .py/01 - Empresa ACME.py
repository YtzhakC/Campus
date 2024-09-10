nick = input("Ingrese su nombre: \n")
v_hora = int(20_000)

horas_t = int(input("Ingrese la cantidad de horas trabajadas: \n"))
s_neto = v_hora * horas_t
EPS = s_neto*0.04
pension = s_neto*0.04
nomina = (s_neto - EPS - pension)

print("-----------------------------------------------------------")
print("Nombre: ", nick)
print(f"Sueldo neto: {s_neto:,.0f}")
print(f"Costo EPS: {EPS:,.0f}")
print(f"Costo Pensión: {pension:,.0f}")
print(f"Sueldo nómina: {nomina:,.0f}")
print("-----------------------------------------------------------")
