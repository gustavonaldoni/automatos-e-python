from afd import AFD

afd1 = AFD()

afd1.inserir_estados('q0', 'q1')
afd1.inserir_simbolos('0', '1')

afd1.inserir_transicao('q0', '0', 'q0')
afd1.inserir_transicao('q0', '1', 'q1')
afd1.inserir_transicao('q1', '0', '')
afd1.inserir_transicao('q1', '1', 'q1')

afd1.definir_estado_inicial('q0')
afd1.definir_estado_final('q1')

afd1.mostrar()

print()
palavra = input()

while palavra != 'END':
       print(afd1.verificar(palavra))
       print()

       palavra = input()