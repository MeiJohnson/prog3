v = 900 #global
# wrap_wrap_foo()
def wrapper_foo():
    enc_v = 'string'
    def foo(x):
        # x local
        y = 100500 #local
        print(enc_v)
        return x+y+1
    foo(1)
    return 'This is wrapper'

f = wrapper_foo()
