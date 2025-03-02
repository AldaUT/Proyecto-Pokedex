# Importamos las bibliotecas necesarias
import requests # Para hacer peticiones HTTP a la API "pokeap"
import os       # Para las operaciones del sistema de archivos "guardar en formato JSON"
import json     # Para manejar datos en formato JSON
import pygame   # Para crear la interfaz grafica "PokeDex"
import io       # Para trabajar con datos binarios en memoria "Impresion de imagenes con pygame"

# Funcion para obtener los datos pokemon desde la API
def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}" #U RL de la API especificiando el nombre del pokemon con minusculas
    respuesta = requests.get(url) # Hacemos peticion a la API

    # Verifica si la peticion fue exitosa (Codigo 200)
    if respuesta.status_code == 200:
        datos = respuesta.json() # Convierte la respuesta en formato JSON

        # Diccionario con la informacion relevante del Pokemon
        info_pokemon = {
            "nombre": datos["name"],  # Nombre
            "peso": datos["weight"],  # Peso en hectogramos (Por defecto en Pokemon)
            "altura": datos["height"],# Altura en decimetros (Por defecto en pokemon)
            "movimientos": [mov["move"]["name"] for mov in datos["moves"][:5]], # Primeros 5 movimientos 
            "habilidades": [hab["ability"]["name"] for hab in datos["abilities"]], # Habilidades
            "tipos": [tipo["type"]["name"] for tipo in datos["types"]], # Tipos del Pokemon
            "imagen": datos["sprites"]["front_default"] # Imagen (sprite) frontal por defecto
        }
        return info_pokemon
    # Manejo de errores
    else:
        # Si hay un error, retornamos None
        return None
# Funcion para guardar la informacion del Pokemon en un archivo JSON
def guardar_pokemon(info_pokemon):
    # Crea la carpeta "Pokedex" si no existe
    os.makedirs("pokedex", exist_ok=True)
    # Define la ruta del archivo
    ruta = os.path.join("pokedex", f"{info_pokemon['nombre']}.json")
    # Abre el archivo en modo escritura
    with open(ruta, "w", encoding="utf-8") as archivo:
        # Guarda la información del Pokemon en formao JSON con indentación
        json.dump(info_pokemon, archivo, indent=4, ensure_ascii=False)
    # Muestra mensaje de exito al guardar el Pokemon    
    print(f"Información guardada en {ruta}")

# Funcion para descargar la imagen (Sprite)
def descargar_imagen(url):
    # Realiza la peticion a la URL
    try:
        respuesta = requests.get(url)
        # Verifica si la peticion fue exitosa (codigo 200)
        if respuesta.status_code == 200:
            # Retorna el contenido binario de la imagen
            return respuesta.content
        # Manejo de errores
        return None
    except Exception as e:
        print(f"Error al descargar la imagen: {e}")
        return None
# Funcion para crear ventana grafica para mostrar la informacion del Pokemon (Pokedex)
def mostrar_pokemon(info_pokemon):
    # Inicializa pygame
    pygame.init()
    
    # Verificar si el archivo de música existe antes de intentar cargarlo
    try:
        # Cargar música si existe el archivo
        pygame.mixer.init()
        if os.path.exists("pokemon_theme.mp3"):
            pygame.mixer.music.load("pokemon_theme.mp3")
            pygame.mixer.music.play(-1)  # El -1 indica reproducciona infinita, en bucle
        # Manejo de errores    
        else:
            print("Archivo de música no encontrado. Continuando sin música.")
    except Exception as e:
        print(f"Error al cargar la música: {e}")

    # Define el tamaño de la ventanda
    ancho, alto = 600, 700
    # Crea la ventana 
    pantalla = pygame.display.set_mode((ancho, alto))
    # Titulo de la ventan
    pygame.display.set_caption("Pokédex")
    
    # Diseño de la ventana (Colores, fuentes, texto)
    fuente = pygame.font.Font(None, 30)
    rojo = (200, 0, 0)
    negro = (0, 0, 0)
    blanco = (255, 255, 255)
    azul = (50, 50, 200)
    
    # Carga la imagen desde la Funcion para la url
    imagen_pokemon = None
    try:
        if info_pokemon["imagen"]:
            # Descarga la imagen
            imagen_datos = descargar_imagen(info_pokemon["imagen"])
            if imagen_datos:
                # convierte lo sdatos binarios en una imagen de pygame
                imagen_pokemon = pygame.image.load(io.BytesIO(imagen_datos))
                # Redimensiona la imagen para la ventana de pygame
                imagen_pokemon = pygame.transform.scale(imagen_pokemon, (250, 250))

            # Manejo de errores
            else:
                print("No se pudo descargar la imagen del Pokémon")
    except Exception as e:
        print(f"Error al cargar la imagen del Pokémon: {e}")
    
    # Bucle princiapl de la ventana
    ventana = True
    while ventana:
        # Procesa el evento (Pokedex)
        for evento in pygame.event.get():
            # Si el usuario cierra la ventana sale del bucle
            if evento.type == pygame.QUIT:
                ventana = False
        # Diseño y colores del Pokedex
        pantalla.fill(rojo)
        pygame.draw.rect(pantalla, negro, (10, 10, ancho - 20, alto - 20), 5)
        pygame.draw.rect(pantalla, azul, (20, 20, ancho - 40, 250))
        
        # Muestra la imagen del Pokemon
        if imagen_pokemon:
            pantalla.blit(imagen_pokemon, (200, 30))
        
        # Muestra información del Pokémon
        texto_nombre = fuente.render(f"Nombre: {info_pokemon['nombre'].capitalize()}", True, blanco)
        texto_peso = fuente.render(f"Peso: {info_pokemon['peso']} hg", True, blanco)
        texto_altura = fuente.render(f"Altura: {info_pokemon['altura']} dm", True, blanco)
        
        # Formatea habilidades y tipos para que no sean demasiado largos
        habilidades_texto = ", ".join(info_pokemon['habilidades'])
        if len(habilidades_texto) > 30:
            habilidades_texto = habilidades_texto[:30] + "..."
        # Formatea los tipos de pokemon
        tipos_texto = ", ".join(info_pokemon['tipos'])
        
        # Muestra los textos, habilidades y tipos
        texto_habilidades = fuente.render(f"Habilidades: {habilidades_texto}", True, blanco)
        texto_tipos = fuente.render(f"Tipos: {tipos_texto}", True, blanco)
        
        # Muestra movimientos
        texto_movimientos = fuente.render("Movimientos:", True, blanco)
        pantalla.blit(texto_movimientos, (20, 480))

        # Muestra los primeros 5 movimientos
        for i, movimiento in enumerate(info_pokemon['movimientos'][:5]):
            texto_mov = fuente.render(f"- {movimiento}", True, blanco)
            pantalla.blit(texto_mov, (40, 520 + i * 30))
        
        # Muestra todo los textos en la pokedex
        pantalla.blit(texto_nombre, (20, 280))
        pantalla.blit(texto_peso, (20, 320))
        pantalla.blit(texto_altura, (20, 360))
        pantalla.blit(texto_habilidades, (20, 400))
        pantalla.blit(texto_tipos, (20, 440))
        
        # Actualiza la pantalla con todos los datos (muestra la pokedex)
        pygame.display.flip()
        
    
    # Detiene la musica cuando se cierra la pantalla
    try:
        pygame.mixer.music.stop()
    except:
        pass
    pygame.quit()

# Funcion principal del programa
def main():
    # Solicita en nombre del pokemon
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    # Obtiene los datos dede la API
    datos_pokemon = obtener_pokemon(nombre_pokemon)
    
    # Si se encontro el Pokemon, se muestra y se guarda la informacion
    if datos_pokemon:
        # Muestra la informacion en la consola
        print(f"\nNombre: {datos_pokemon['nombre'].capitalize()}")
        print(f"Peso: {datos_pokemon['peso']} hectogramos")
        print(f"Altura: {datos_pokemon['altura']} decímetros")
        print(f"Movimientos: {', '.join(datos_pokemon['movimientos'])}")
        print(f"Habilidades: {', '.join(datos_pokemon['habilidades'])}")
        print(f"Tipos: {', '.join(datos_pokemon['tipos'])}")
        print(f"Imagen: {datos_pokemon['imagen']}")
        
        # Guarda el archivo en formato JSON
        guardar_pokemon(datos_pokemon)
        # Muestra la informacion grafica
        mostrar_pokemon(datos_pokemon)
    # Manejo de errores    
    else:
        print("Error: Pokémon no encontrado.")
        
# Esta condicion verifica si el script se está ejectuando directamente
if __name__ == "__main__":
    main()


