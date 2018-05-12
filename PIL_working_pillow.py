from PIL import Image

imagen=Image.open('rias2.jpeg')
imagen.thumbnail((100,100))

imagen_convertida = ''

colores = [
    '@',
    '#',
    'H',
    '*',
    '.',
    ' '
]
ancho,alto = imagen.size
for nro_pixel,pixel in enumerate(imagen.getdata()):

    r, g, b = pixel
    color = (r + g + b)/3
    factor = color / 255
    posicion = int(factor*(len(colores)-1))
    imagen_convertida += colores[posicion]
    if nro_pixel % ancho ==0:
        imagen_convertida += '\n'

archivo = open('rias2.txt','w')
archivo.write(imagen_convertida)
archivo.close()