from rolepermissions.roles import AbstractUserRole

class Empresa(AbstractUserRole):
    available_permissions = {''}

class Funcionario(AbstractUserRole):
    available_permissions = {''}