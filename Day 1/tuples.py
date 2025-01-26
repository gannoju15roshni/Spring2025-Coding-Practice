tuple1=("areoplane","banana","christmas")
print(type(tuple1))
print(len(tuple1))
print(tuple1)

tuple2=tuple(("dosa",15,7))
print(tuple2)
tuplecopy=list(tuple1)
tuplecopy.insert(2,2025)
tuple1=tuple(tuplecopy)
print(tuple1)

tuple3=tuple1+tuple2
print(tuple3)

#Note: Tuples are immutable