def porcentaje_impuestos(sueldo, impuestos):
    return (impuestos / sueldo) * 100

def porcentaje_comida(sueldo, comida):
    return (comida / sueldo) * 100

def porcentaje_colegio(sueldo, colegio):
    return (colegio / sueldo) * 100

sueldo_evelyn = 22500
impuestos_evelyn = 6750
comida_evelyn = 11250
colegio_evelyn = 4500

porcentaje_impuestos_evelyn = porcentaje_impuestos(sueldo_evelyn, impuestos_evelyn)
porcentaje_comida_evelyn = porcentaje_comida(sueldo_evelyn, comida_evelyn)
porcentaje_colegio_evelyn = porcentaje_colegio(sueldo_evelyn, colegio_evelyn)

print(f"Porcentaje de sueldo destinado a impuestos: {porcentaje_impuestos_evelyn}%")
print(f"Porcentaje de sueldo destinado a comida: {porcentaje_comida_evelyn}%")
print(f"Porcentaje de sueldo destinado al colegio de su hija: {porcentaje_colegio_evelyn}%")
