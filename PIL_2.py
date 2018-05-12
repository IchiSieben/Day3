from PIL import Image, ImageDraw

imagen = Image.open('rias2.jpeg')



# se peude cear diccionarios por comprension
#{x: 'a' for x in range (3)}

#red = { key:'value' for key in range(256) }
#green = { key:'value' for key in range(256) }
#blue = { key:'value' for key in range(256) }

rojos = [0 for _ in range (256)]
verdes = [0 for _ in range (256)]
azules = [0 for _ in range (256)]

for r, g ,b in imagen.getdata():
    rojos[r] += 1
    verdes[g] += 1
    azules[b] += 1


def generar_histograma(conteos, nombre_archivo):

    lienzo = Image.new ('RGB',(256,256))
    lapicero = ImageDraw.Draw(lienzo)

    maximo_conteo = max(conteos)
    for color, conteo in enumerate(conteos):
        factor = conteo/ maximo_conteo
        lapicero.line([(color,255),(color,255-(factor*256))])

    lienzo.save(nombre_archivo)

generar_histograma(rojos,'histogramaR.jpg')
generar_histograma(verdes,'histogramaV.jpg')
generar_histograma(azules,'histogramaA.jpg')

"""
for c in range (256):

    lapicero.line([(c, 0), (c, rojos[c])])

lienzo.save('histograma.jpg')

lienzo = Image.new ('RGB',(256,256))
lapicero = ImageDraw.Draw(lienzo)
lapicero.line([(0,0),(256,256)])
"""
