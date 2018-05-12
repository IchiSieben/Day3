class abc:

    def saludar(lang):
        def saludar_es():
            print ('Hola')

        def saludar_en():
            print ('Hi')

        def saludar_fr():
            print ('Salut')

        lang_func = {
            'es': saludar_es,
            'en': saludar_en,
            'fr': saludar_fr
        }
        return lang_func[lang]

    f = saludar('es')
    f()
    def frenar(self):
        print('*sonido de frenar')

    Carro = type ('Carro',(),{'arrancar':lambda self:'RUN RUN RUN'})
    bmw = Carro()
    print(bmw.arrancar())
    