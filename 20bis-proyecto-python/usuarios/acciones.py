import usuarios.usuario as modelo

class Acciones:
    
    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema...")
        
        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
        
        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
        
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("\nNo te has registrado correctamente!!")    

    def login(self):
        print("\nVale!! Identifícate en el sistema...")
        
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            
            usuario = modelo.Usuario('', '', email, password)       
            login = usuario.identificar()
            
            if email == login[3]:
                print(f"\nBienvenido {login[1]} te has registrado en el sistema el dia {login[5]}")

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"\nLogin incorrecto!! Intentalo de nuevo!!")
