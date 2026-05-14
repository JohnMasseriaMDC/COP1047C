global_var1 = "global"

def fun1():
    global_var1 = "modified in fun1"
    print("Inside fun1:", global_var1)

print("Before calling fun1:", global_var1)
fun1()
print("After calling fun1:", global_var1)
