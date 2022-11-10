import ctypes

biblioteca = ctypes.CDLL("libfuncao.so")
biblioteca.multiply.argtypes = [ctypes.c_double]
biblioteca.multiply.restype = ctypes.c_double
valor = biblioteca.multiply(10)
print(valor)
