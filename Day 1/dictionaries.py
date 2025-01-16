dict1={
    "white":"Jasmine",
    "red":"Rose",
    "yellow":"sunflower"
}

print(dict1.get("yellow"))

#  adding a new item using key() method
x=dict1.keys()

print(x)

dict1["pink"]="lotus"

print(x)

#  replacing the exsiting item using values() method
y=dict1.values()

print(y)

dict1["white"]="tulip"

print(y)

# updating existing dictionary using update() method

dict1.update({"white":"lily"})

print(dict1)

# you can remove an item using -> [dictionaryname.pop("key")]
# -> [dictionaryname.popitem()] would remove the last inserted item

# you can use -> [del dictionaryname.["key"]] to delete specified key from the dictionary
# remember if ->[ del dictinaryname ] is used and then printed you'll get an error since the dictionary is deleted before print command

# you can clear the whole dictionary using -> [dictionaryname.clear()]

# copy the exsisting dictionary assigning the -> [dictionaryname.copy()] to a variable and printing it
# you can also copy using dict() method -> [dict(dictionaryname)]

#blank comment

#blank comment