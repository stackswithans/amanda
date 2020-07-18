from amanda.types import Bool,Indef
import amanda.symbols as symbols
from amanda.symbols import Type
from amanda.error import AmandaError,throw_error

#Symbols for builtin functions
#used during sem analysis
bltin_symbols = {}
#builtin objects used during 
#code execution
bltin_objs={}

#Runtime errors
DIVISION_BY_ZERO = "não pode dividir um número por zero"
INVALID_CONVERSION = "impossível realizar a conversão entre os tipos especificados"


def add_bltin_func(name,obj,rtn_type,*params):
    ''' Helper that creates a function_symbol and adds it
    to the dict of bltin symbols'''
    rtn_type = rtn_type if rtn_type else Type.VAZIO
    formal_params = {}
    for pname,ptype in params:
        formal_params[pname] = symbols.VariableSymbol(pname,ptype)
    bltin_symbols[name] = symbols.FunctionSymbol(
        name,rtn_type,
        formal_params
    )
    bltin_objs[name] = obj
    

    
def print_wrapper(obj,**kwargs):
    if str(obj) == "True":
        print(Bool.VERDADEIRO,**kwargs)
    elif str(obj) == "False":
        print(Bool.FALSO,**kwargs)
    else:
        print(obj,**kwargs)

def converte(value,ama_type):
    if isinstance(value,Indef):
        value = value.value
    if ama_type == "int" or ama_type == "real":
        try:
            return int(value) if ama_type == "int" else float(value)
        except ValueError as e:
           raise AmandaError(INVALID_CONVERSION,-1)
        except TypeError as e:
           raise AmandaError(INVALID_CONVERSION,-1)
    elif ama_type == "bool":
        return bool(value)
    elif ama_type == "texto":
        return str(value)
    elif ama_type == "indef":
        return Indef(value)
    else:
        NotImplementedError("have not considered other types")

def tipo(indef_obj):
    ''' Returns the type of a 
    value. Useful for 'unwrapping' 
    indef type values'''
    value = indef_obj.value # unwrap value
    types = {
        int : "int",
        float : "real",
        bool : "bool",
        Bool : "bool",
        str : "texto",
    }
    return types.get(type(value))

bltin_objs["verdadeiro"] = Bool.VERDADEIRO
bltin_objs["falso"] = Bool.FALSO
bltin_objs["printc"] = print_wrapper
bltin_objs["Indef"] = Indef
bltin_objs["converte"] = converte
add_bltin_func("tipo",tipo,Type.TEXTO,("valor",Type.INDEF))