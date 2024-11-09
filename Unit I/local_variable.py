# Construct a function with a local variable.
# Show what happens when you try to use that variable outside the function. Explain the results.
#//////////////////

def functionLocal():
    localVariable = 'This is local' #We create the local variable
    print(localVariable)

show = functionLocal() #We call the function

print(localVariable) #We tried to use it, but since it's a local variable, outside the function is not defined.