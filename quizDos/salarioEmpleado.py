nom= input("Nombre: ")
dias =int(input("Ingrese el periodo de dias laborados"))
salario= int(input("Ingrese el salario "))





prima= salario*dias / 360
cesantias=salario*dias/ 360
interesesCesantías= (cesantias * 0.12)/ dias
Vacaciones=(salario * dias)/ 720


liquidacion = prima+cesantias+interesesCesantías+Vacaciones

print(f"\nSeñor {nom} para los {7} días laborados y salario ${salario:,.2f}, su liquidación se compone así:")
print(f"Prima: ${prima:,.2f}")
print(f"Cesantía: ${cesantias:,.2f}")
print(f"Intereses cesantías: ${interesesCesantías:,.2f}")
print(f"Vacaciones: ${Vacaciones:,.2f}")
print(f"Liquidación total: ${liquidacion:,.2f}")