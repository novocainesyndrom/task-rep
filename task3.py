from copy import deepcopy 

def task_2():
	a = 1
	s = "2"

	print(type(a) == type(s)) 
	s = int(s)
	print(type(a) == type(s)) 

	L = [1,2,3,4,5]
	print(L)
	L.append(6)
	print(L)
	L.insert(3,10)
	print(L) 
	L.remove(L[0]) # L = L[1:]
	print(L)
	del L[2] # L = L[0:2] + L[3:]; L.pop(2)
	print(L)
	L.reverse() # L = L[::-1]
	print(L, "List len %s" % len(L), sep='\n')
	L2 = deepcopy(L) # L2 = L[:]
	"""L = quick_sort(L)
				print("L", L)"""
	L2.sort() # sorted() - function that returns a new, changed object, 
			  #  unlike the sort() method, which modifies an existing list
	print("L2", L2)
	s = "This is a test string for Internship Onix for python"
	print(s)
	s = sorted(s.lower().split(' '))
	print(s)
	D = {'b':3, 'c':1, 'a':2 }
	print(D)
	D['e'] = 4
	print(D)
	del D['a'] # D.pop(‘a’)
	keys, values = list(D.keys()), list(D.values())
	print(keys, values, sep='\n')
	D = {key: D[key] for key in sorted(D)}
	print(D)
	D = {key: value for value in sorted(D.values()) for key in D.keys() if D[key] == value }
	print(D)



glb_var = 9


def var_mult(var):
	values = list(map(lambda num: num * glb_var, range(1,var)))
	return  values, len(values)

def var_mult_easy(numeric_variable, returning_list=[]):
	returning_list.append(numeric_variable * glb_var) 
	return returning_list, len(returning_list)

def arguments(*args, **kwargs):
	print( "*" * 80 + '\n' + f"args={args}\nkwargs={kwargs}")

def is_divisible_by(num, divisor):
	return True if num%divisor==0 else False

def fib(fib_num):
    return 1 if fib_num <= 2 else fib(fib_num - 1) + fib(fib_num - 2)
 
if __name__ == '__main__':
	num, divisor = 15, 3
	fib_num = 9
	sep='\n' + "*" * 80 + '\n'
	task_2()
	print(sep + "List: {0}\nLength: {1}".format(*var_mult(7)),
	      	   "List: {0}\nLength: {1}".format(*var_mult_easy(8)),
		   f'{num} is divisible by {divisor}' if is_divisible_by(num, divisor) else f'{num} isn\'t divisible by {divisor}' , 
		   f'{fib_num} Fibonacci number is {fib(fib_num)}',
		   sep=sep)
	arguments(6,7,8, val1=10, val2=57)
