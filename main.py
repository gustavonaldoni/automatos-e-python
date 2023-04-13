from afd import AFD
from afnd import AFND
from afnde import AFNDe

afnde1 = AFNDe()

afnde1.inserir_estados('q0', 'q1', 'q2', 'q3')
afnde1.inserir_simbolos('0', '1')

afnde1.inserir_transicao('q0', '0', {'q0', 'q1'})
afnde1.inserir_transicao('q0', '1', set())
afnde1.inserir_transicao('q0', '', {'q1', 'q2'})

afnde1.inserir_transicao('q1', '0', {'q3'})
afnde1.inserir_transicao('q1', '1', {'q3'})
afnde1.inserir_transicao('q1', '', set())

afnde1.inserir_transicao('q2', '0', {'q3'})
afnde1.inserir_transicao('q2', '1', {'q2'})
afnde1.inserir_transicao('q2', '', set())

afnde1.inserir_transicao('q3', '0', set())
afnde1.inserir_transicao('q3', '1', set())
afnde1.inserir_transicao('q3', '', {'q0'})

afnde1.definir_estado_inicial('q0')
afnde1.definir_estados_finais('q2', 'q3')

print("========== Mostrando AFND-e ==========")
afnde1.mostrar()
print()

afnd_equivalente = afnde1.converter_para_afnd()
print("========== Mostrando AFND equivalente ==========")
afnd_equivalente.mostrar()
print()

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
