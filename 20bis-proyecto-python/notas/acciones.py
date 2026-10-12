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