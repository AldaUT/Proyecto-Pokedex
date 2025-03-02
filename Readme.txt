Proyecto Pokédex

Este proyecto es una aplicación que permite buscar información de Pokémon utilizando la PokeAPI y mostrarla de forma gráfica utilizando Pygame.

Descripción
La aplicación permite al usuario:

-Buscar un Pokémon por su nombre
-Ver información como peso, altura, tipos, habilidades y movimientos
-Visualizar la imagen del Pokémon
-Guardar la información en un archivo JSON

Requisitos
Para ejecutar este proyecto, necesitarás tener instalado:

Python 3.6 o superior
Las siguientes bibliotecas:

-requests: Para realizar peticiones HTTP a la API
-pygame: Para la interfaz gráfica
-json: Incluida en Python estándar
-os: Incluida en Python estándar
-io: Incluida en Python estándar


Instalación

Clona este repositorio: https://github.com/AldaUT/Proyecto-Pokedex.git

Instala las dependencias:

Copypip install requests pygame

Para una experiencia completa, puedes añadir un archivo de música "pokemon_theme.mp3" en la carpeta del proyecto (opcional).

Uso
Ejecuta el programa:
pokedex.py

Introduce el nombre de un Pokémon cuando se te solicite y disfruta de la información.

Ejemplos
Búsqueda de Pikachu

La aplicación muestra la imagen de Pikachu junto con toda su información.

Datos guardados
La información del Pokémon se guarda en archivos JSON en la carpeta "pokedex":
json{
    "nombre": "pikachu",
    "peso": 60,
    "altura": 4,
    "movimientos": [
        "mega-punch",
        "pay-day",
        "thunder-punch",
        "slam",
        "double-kick"
    ],
    "habilidades": [
        "static",
        "lightning-rod"
    ],
    "tipos": [
        "electric"
    ],
    "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
}

Lo que he aprendido
Durante este ejercicio he aprendido a:

-Llamar APIs externas utilizando la biblioteca requests
-Manejar datos en formato JSON
-Crear interfaces gráficas sencillas con Pygame
-Implementar operaciones de archivos para guardar datos
-Manejar errores y excepciones en Python
-Organizar el código en funciones para una mejor estructura
-Utilizar list comprehensions para un código más limpio
-Cargar y manipular imágenes en una aplicación
-Reproducir audio en aplicaciones Python
-Investigacion por cuenta propia para mejorar mis proyectos

Próximas mejoras

-Añadir más detalles como estadísticas base
-Añadr un mejor diseño al Pokedex
-Experimentoas con animaciones
-Añadir la posibilidad de comparar Pokémon

Recursos
Este proyecto utiliza:

PokeAPI para obtener los datos de los Pokémon
Pygame para la interfaz gráfica
