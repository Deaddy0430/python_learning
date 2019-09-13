#============1================
# v=100   #全局作用域
# def fun1():
#     v=200   #外部嵌套函数作用域
#     print('v in fun1 =', v)
#     def fun2():
#        v=300    #局部作用域
#        print('v in fun2=', v)
#     fun2()
# fun1()
# print("v =", v)

#=============2================    
v=100   #全局作用域
def fun1():
    print('v in fun1 =', v)
    def fun2():
       v=300    #局部作用域
       print('v in fun2=', v)
    fun2()
fun1()
print("v =", v)