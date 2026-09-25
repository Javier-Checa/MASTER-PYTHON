import clases

persona = clases.Persona()
persona.setNombre("Javier")
persona.setApellidos("Checa Martínez")
persona.setAltura("165 cm")
persona.setEdad("53 años")

print("\n------------------------------------------")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("\n------------------------------------------")
      
informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martín Requena")


print(f"El informático es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("\n------------------------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Manuel Pérez")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())