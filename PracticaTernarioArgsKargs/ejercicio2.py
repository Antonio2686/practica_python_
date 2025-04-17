# Buscar una palabra en una lista ingresada por teclado usando args y un operador
# ternario 


#Solicitar la palabra al usuario


def test_var_args(f_arg,*argv):
    print("Nombre del primer argumento:", f_arg)
    print(argv)
    palabra = input("Ingresa la palabra a buscar (lenguaje de programacion): ")
    resul = False
    for arg in argv:
        if arg == palabra:
            resul = True
            break
        else:
            resul = False
            # Si no se encuentra la palabra, se asigna False a resul
    print("La palabra está en la lista." if resul else f"La palabra no está en la lista.")

test_var_args('Python','Java','C++','JavaScript','Ruby','PHP','Swift','Go','Kotlin','Rust','Dart','Perl','Scala','Haskell','Lua','C#','Objective-C','R','MATLAB','Groovy','Elixir','Clojure','F#','Visual Basic .NET','Assembly Language','COBOL','Fortran','Ada','Pascal','Smalltalk','Prolog','Erlang','OCaml','Scheme','Dylan','Nim','Crystal','Hack','Solidity','ActionScript','VBScript','Tcl','Xojo','PureBasic','REXX','Modula-2','ALGOL','Simula','Io','J#','OpenCL','VHDL','Verilog','ABAP','PL/SQL')
