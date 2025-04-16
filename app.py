from modelos.restaurantes import Restaurante
from modelos.avaliacao import Avaliacao


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.alternar_estado()

restaurante_praca.receber_avaliacao('paulo', 1)
restaurante_praca.receber_avaliacao('xaruco', 4)
restaurante_praca.receber_avaliacao('cesar', 5)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()