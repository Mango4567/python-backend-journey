#type-casting , variables,built-in functions
#int to float
int_num=10
print('int_num',int_num)  #10
num_float=float(int_num)
print("num_float:",num_float) #10.0
#float to int
float_weight= 74.55
int_weight=int(float_weight)
print("intweight:",int_weight) #74
#str to float or int
num_str="10.6"             #imp- str to float to int always
num_float=float(num_str)   #int(num_str)not allowed directly because int()accepts int values, truncates float numbers and valid integer strings. 
num_int=int(num_float)   #meaning int(10.6),int("10")iare allowed butint("10.6") not allowed directly.
print("integernumberis:",num_int) #that is why we use int(float())
print("floatnumberis:",num_float)
print("the string to integer converted is:",int(float(num_str)))