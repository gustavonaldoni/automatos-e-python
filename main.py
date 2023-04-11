from afd import AFD
from afnd import AFND

afd1 = AFD()

afd1.inserir_estados('q0', 'q1')
afd1.inserir_simbolos('0', '1')

afd1.inserir_transicao('q0', '0', 'q0')
afd1.inserir_transicao('q0', '1', 'q1')
afd1.inserir_transicao('q1', '0', '')
afd1.inserir_transicao('q1', '1', 'q1')

afd1.definir_estado_inicial('q0')
afd1.definir_estado_final('q1')

# afd1.mostrar()
# print()

afnd1 = AFND()

afnd1.inserir_estados('q0', 'q1')
afnd1.inserir_simbolos('0', '1')

afnd1.inserir_transicao('q0', '0', {'q0', 'q1'})
afnd1.inserir_transicao('q0', '1', {'q1'})
afnd1.inserir_transicao('q1', '0', {'q1'})
afnd1.inserir_transicao('q1', '1', {'q1'})

afnd1.definir_estado_inicial('q0')
afnd1.definir_estados_finais('q1')

print("========== Mostrando AFND ==========")
afnd1.mostrar()
print()

afd2 = afnd1.converter_para_afd()

print("========== Achando o AFD equivalente ==========")
afd2.mostrar()
print()
