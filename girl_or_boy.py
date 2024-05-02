def girl_or_boy(nombre_usuario):
    caracteres_distintos = len(set(nombre_usuario))
    if caracteres_distintos % 2 == 0:
        return "¡ITS A GIRL!"
    else:
        return "¡ITS A BOY!"

# Ejemplo
nombre = "Maximiliano"
print(girl_or_boy(nombre))  