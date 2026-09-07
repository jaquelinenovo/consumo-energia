def calcular_consumo(potencia, horas_dia):
    return (potencia * horas_dia * 30) / 1000


print("=== CALCULADORA DE CONSUMO ELÉTRICO ===")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

consumo = calcular_consumo(potencia, horas_dia)

print("\n--- RESULTADO ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo:.2f} kWh/mês")

custo = consumo * 0.75
print(f"Custo estimado: R$ {custo:.2f}/mês")
