class MyError(Exception):
    ...
class OutroError(Exception):
    ...

def levantar():
    exception_ = MyError("Mensagem de erro", 'arg2', 'arg3')
    exception_.add_note('Nota 1 - teste')
    raise exception_


try:    
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(f"Erro: {error}")
    exception_ = OutroError("Erro tratado de novo")
    exception_.__notes__ = error.__notes__.copy()
    raise exception_ from error