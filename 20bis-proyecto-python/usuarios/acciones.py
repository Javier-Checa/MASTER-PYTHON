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
                self.proximasAcciones(login)
                
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"\nLogin incorrecto!! Intentalo de nuevo!!")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
            - crear nota
            - mostrar notas
            - borrar nota
            - salir
        """)
        
        accion = input("¿Qué quieres hacer?: ")
        if accion == "crear":
            print("Ok!! Vamos a crear una nota")
        elif accion == "mostrar":
            print("Ok!! Vamos a mostrar tus notas")
        elif accion == "borrar":
            print("Ok!! Vamos a borrar una nota")
        elif accion == "salir":
            print(f"Ok {usuario[1]}!! Hasta pronto!!")