class MyError(Exception):
    ...

def levantar():
    exception_ = MyError("Mensagem de erro", 'arg2', 'arg3')
    raise exception_


try:    
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(f"Erro: {error}")
    raise