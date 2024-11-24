import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Practica 09: Mover imágenes")

# Colores
white = (255, 255, 255)
gray = (200, 200, 200)

# Carga de imágenes
image1 = pygame.image.load("image1.png")  # Cambia por la ruta de tu imagen 1
image2 = pygame.image.load("image2.png")  # Cambia por la ruta de tu imagen 2

# Ajusta el tamaño de las imágenes si es necesario
image1 = pygame.transform.scale(image1, (100, 100))
image2 = pygame.transform.scale(image2, (100, 100))

# Coordenadas iniciales para las imágenes
x1, y1 = 0, height // 4 - image1.get_height() // 2  # Imagen 1 en la mitad superior
x2, y2 = width // 2 - image2.get_width() // 2, height // 2  # Imagen 2 en la mitad inferior

# Velocidades
speed_x1 = 5  # Velocidad de la imagen 1 (horizontal)
speed_y2 = 5  # Velocidad de la imagen 2 (vertical)

# Bucle principal
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover imagen 1 (izquierda a derecha dentro de la sección superior)
    x1 += speed_x1
    if x1 + image1.get_width() > width or x1 < 0:
        speed_x1 = -speed_x1

    # Mover imagen 2 (arriba hacia abajo dentro de la sección inferior)
    y2 += speed_y2
    if y2 + image2.get_height() > height or y2 < height // 2:
        speed_y2 = -speed_y2

    # Dibujar la pantalla
    screen.fill(white)  # Limpia la pantalla

    # Dibujar divisor para las secciones
    pygame.draw.line(screen, gray, (0, height // 2), (width, height // 2), 2)  # Línea horizontal

    # Dibujar imágenes en sus secciones respectivas
    screen.blit(image1, (x1, y1))  # Imagen 1 (mitad superior)
    screen.blit(image2, (x2, y2))  # Imagen 2 (mitad inferior)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar FPS
    clock.tick(60)

# Salir del programa
pygame.quit()
sys.exit()
