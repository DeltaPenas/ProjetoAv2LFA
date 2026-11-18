from automatos.automato_mercosul_convertido import validar
from automatos.identificador_placa import identificar_modelo

resultado = identificar_modelo("ABC1D23")

print(validar("ABC1D23"))
print(f"O modelo da placa é: {resultado}")