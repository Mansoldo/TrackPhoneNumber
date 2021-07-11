# Working with phone number and discovering his location

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier


# Ajuste o formato do telefone
telefone = '+5511959459690'

telefone_ajustado = phonenumbers.parse(telefone, 'pt-br')
print(telefone_ajustado)

# Descobrir a localização do telefone
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)

# Formatando o número
telefone_formulario = '+5511959459690'
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, 'pt-br')
telefone_formato = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefone_formato)

# Operadora do telefone
operadora = carrier.name_for_number(telefone_ajustado, 'pt-br')
print(operadora)

# Retirar telefone do texto
corpo_email = '' \
              'Prezados, ' \
              'Quando tiverem uma resposta da proposta, favor entrar em contato. ' \
              'Abraços, ' \
              'Mansoldo ' \
              '(11)95945-9690'

for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, "BR"):
    print(telefone)