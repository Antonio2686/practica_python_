# Calcular el promedio de una lista de números usando args y un operador ternario

def test_var_args(*argv):
    sum = 0
    for arg in argv:
        sum += float(arg)
    print(sum / len(argv) if sum != 0 else "Lista vacía, no se puede calcular el promedio")

test_var_args('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20')
# test_var_args()


