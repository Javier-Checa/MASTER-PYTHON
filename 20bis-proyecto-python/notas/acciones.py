import notas.nota as modelo

class Acciones:
   
    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Introduce la descripcion de tu nota: ")
        
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardado = nota.guardar()
        
        if guardado[0] >= 1:
            print(f"\nPerfecto {usuario[1]}!! Has creado la nota: {nota.titulo}")
        else:
            print(f"\n{usuario[1]}, no se ha podido crear la nota.")
    
            
    def mostrar(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a mostrar tus notas...")
        
        nota = modelo.Nota(usuario[0], '', '')
        notas = nota.listar()
        
       
        if len(notas) >= 1:
            print(f"\n{usuario[1]}!! Tienes {len(notas)} notas: ")
            for n in notas:
                print("\n********************************")
                print(n[2])
                print(n[3])
                print("********************************")
        else:
            print(f"\n{usuario[1]}!! No tienes notas para mostrar.")
        