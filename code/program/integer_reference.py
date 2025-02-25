import ctypes

a = ctypes.c_int(12)
a_ref_1 = a

def b(val):
    print(val.value)

def main():
    print(a.value)
    b(a)
    
if __name__ == "__main__":
    main()