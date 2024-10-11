
def calcular_imc(peso, estatura):
    return peso / (estatura ** 2)


def clasificar_riesgo(imc):
    if imc < 18.5:
        return "Riesgo bajo (Bajo peso)"
    elif 18.5 <= imc < 24.9:
        return "Riesgo bajo (Peso normal)"
    elif 25 <= imc < 29.9:
        return "Riesgo medio (Sobrepeso)"
    elif 30 <= imc < 39.9:
        return "Riesgo alto (Obesidad)"
    else:
        return "Riesgo muy alto (Obesidad severa)"

cantidad_personas = int(input("¿Cuántas personas deseas registrar?: "))

for i in range(cantidad_personas):
    print(f"\n--- Registro de la persona {i+1} ---")
    
    nombre = input("Ingresa tu nombre: ")
    apellidos = input("Ingresa tus apellidos: ")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    estatura = input("Ingresa tu estatura en metros : ")
    
    estatura = float(estatura)

    imc = calcular_imc(peso, estatura)

    riesgo = clasificar_riesgo(imc)

    nombre_completo = f"{nombre} {apellidos}"
    print(f"{nombre_completo}: IMC = {imc:.2f}, {riesgo}")

