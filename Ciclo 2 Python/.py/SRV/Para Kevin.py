tranquilidad = False
estado_de_animo = input('¿Cómo te sientes?')
kevin = estado_de_animo

while not tranquilidad:
     if kevin == 'triste por el parcial':
          tranquilidad = False
     elif kevin == 'Parchado porque no se puede hacer nada más':
          tranquilidad = True

     if tranquilidad is True:
          print('Felicidades, a pesar de que te ha ido mal, aceptas que no se puede hacer nada más y elegiste el camino de la felicidad y el parche, por lo tanto estás tranquilo y te esforzarás para la próxima. :)')
          break
