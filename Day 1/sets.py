set1={"hp",5,"dell",1}
set1.add("lenovo")
set2={3,"mac",4}
set3={"msi",1,"alien ware",6}
set4={"legion",2,"asus",7}
set5=set3 | set4 | set2 | set1
print(set5)

seta={"apple","banana","cherry"}
setb={"banana","apple"}

setc=seta.symmetric_difference(setb)
print(setc)
# set1.update(set2)
# set1.discard("mac")
# print(set1)