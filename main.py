from afd import AFD
from afnd import AFND

afd1 = AFD(Q={0, 1, 2},
           Sigma={"a", "b"},
           Delta={(0, "a"):  1,
                  (0, "b"): -1,
                  (1, "a"):  1,
                  (1, "b"):  2,
                  (2, "a"): -1,
                  (2, "b"):  2},
           q0=0,
           F={1, 2})

afnd1 = AFND(Q={0, 1},
             Sigma={"0", "1"},
             Delta={(0, "0"): {0, 1},
                    (0, "1"): {1},
                    (1, "0"): {1},
                    (1, "1"): {1}},
             q0=0,
             F={1})

while True:
       print("L = 0+ ?1 (0/1)*")
       print()

       p = input("Escreva uma palavra: ")

       if (afnd1.verificar(p)):
              print("Palavra válida.")
       else:
              print("Palavra inválida.")

       print()

       opcao = input("Deseja continuar (s/n)? ")

       if opcao.lower() == 'n':
              break