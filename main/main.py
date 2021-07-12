# Working with phone number and discovering his location

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

telefone = '+5511959459690'

# Adjusting the phone number according to the region
telefone_ajustado = phonenumbers.parse(telefone, 'pt-br')
print(telefone_ajustado)

# Discovering the number location
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)

# Formating the number
telefone_formulario = '+5511959459690'
telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, 'pt-br')
telefone_formato = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefone_formato)

# Telephone provider
operadora = carrier.name_for_number(telefone_ajustado, 'pt-br')
print(operadora)

# Removing a phone number from a text
corpo_email = '' \
              'Prezados, ' \
              'Quando tiverem uma resposta da proposta, favor entrar em contato. ' \
              'Abraços, ' \
              'Mansoldo ' \
              '(11)95945-9690'

for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, "BR"):
    print(telefone)