#Añaden funcionalidades a otras funciones
def func_deco(func_param):
    def func_int():
        print("Inicio")
        func_param()
        print("fin")
    return func_int

@func_deco
def suma():
    print(1+2)

def resta():
    print(7-8)

suma()
resta()
