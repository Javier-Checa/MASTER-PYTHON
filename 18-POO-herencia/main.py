import clases

persona = clases.Persona()
persona.setNombre("Javier")
persona.setApellidos("Checa Martínez")
persona.setAltura("165 cm")
persona.setEdad("53 años")


print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())