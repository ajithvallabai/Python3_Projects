# iterators 

sample="water"
rt=iter(sample)
print(next(rt))




# Generator Expressions
# zip()

x=sum(i*i for i in range(10))
print(x)

x_array=[1,2,3]
y_array=[6,7,8]

w=sum(i*j for i,j in zip(x_array,y_array))
print(w)