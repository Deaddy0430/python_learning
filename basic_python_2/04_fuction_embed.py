def fn_outer():
    print("fn_out called !")
    def fn_inner():
        print("fn_inner called !")
    
    fn_inner()
    fn_inner()
    print("fn_outter invoke end")
    return fn_inner

fn_outer()
print('----------------------------------')
fx=fn_outer()
fx()