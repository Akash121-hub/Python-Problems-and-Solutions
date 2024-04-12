'''import time
def deco_func(func):
    def wrapper(*args,**kwargs):
        start_time = time.now()
        result  = func(*args,**kwargs)
        end_time = time.now() 
        return [result, (start_time-end_time)*1000]
    return wrapper

@deco_func
def add(a,b):
    return a + b'''

    # water
	# rwate
	# erwat
	# terwa
	# aterw
	# water


def slicing_words(word):
    for i in range(len(word)):
        print(word[i:] + word[:i]) 

s = slicing_words("water")



dict1 = {'a':1,'b':2}

re = dict1.pop('a')
# print(re)
# print(dict1)