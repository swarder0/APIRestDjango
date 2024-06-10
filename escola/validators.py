import re
from validate_docbr import CPF

def validate_cpf(client_cpf):
    cpf = CPF()
    return cpf.validate(client_cpf)
def validate_nome(client_name):
    return client_name.isalpha()
def validate_rg(client_rg):
    return len(client_rg) == 9
def validate_email(client_email):
    modelo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    resposta = re.findall(modelo, client_email)
    return resposta