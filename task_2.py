from copy import deepcopy

def quick_sort(arr):
	if len(arr) < 2:
		return arr
	else:
		piv = arr[0]
		less = [i for i in arr[1 : ] if i < piv] 
		great = [ i for i in arr[1 : ] if i > piv]
	return quick_sort(less) + [piv] + quick_sort(great)

a = 1
s = "2"

print(type(a) == type(s)) 
s = int(s)
print(type(a) == type(s)) 

L = [1,2,3,4,5]
print(L)
L.append(6)
print(L) 
L.remove(L[0]) # или L = L[1:]
print(L)
del L[2] # или L = L[0:2] + L[3:]; L.pop(2)
print(L)
L.reverse() # или L = L[::-1]
print(L, "List len %s" % len(L), sep='\n')
L2 = deepcopy(L) # или L2 = L[:]
L = quick_sort(L)
print("L", L)
L2.sort() # sorted() - функция, которая возвращяет новий, измененный объект, 
		  # в отличии от метода sort(), изменяющего уже существующий список  
print("L2", L2)
s = "This is a test string for Internship Onix for python"
print(s)
s = "".join(sorted(s))
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