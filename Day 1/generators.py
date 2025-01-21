# In Python, to create iterators, we can use both regular functions and generators. 
# Generators are written just like a normal function but we use yield() instead of return() for returning a result. 
# It is more powerful as a tool to implement iterators.
# It is easy and more convenient to implement because it offers the evaluation of elements on demand. 
# Unlike regular functions which on encountering a return statement terminates entirely,
# generators use a yield statement in which the state of the function is saved from the last call and can be picked up or resumed the next time we call a generator function. 
# Another great advantage of the generator over a list is that it takes much less memory. 





# Python code to illustrate generator, yield() and next(). 
def generator(): 
    t = 1
    print ('First result is ',t) 
    yield t 
 
    t += 1
    print ('Second result is ',t) 
    yield t 
 
    t += 1
    print('Third result is ',t) 
    yield t 
 
call = generator() 
next(call) 
next(call) 
next(call)