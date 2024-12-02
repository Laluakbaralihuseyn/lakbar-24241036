#operasi yang dapat dilalkukan dengan meringkas

a = 5 # dalam assigment
print("nilai a = " ,a)

a += 1 #artinya a = a + 1
print("nilai a += 1, nilai a menjadi", a)


a -= 2  #artinya a = a - 2
print("nilai a -= 2, nilai a menjadi",a)

a *=5 #artinya adalah a= a * 5
print("nilai a *= 5 ,nilai a menjadi", a )

a/= 2 #artinya adalah a = a / 2
print("nilai a/= 2,nilai a menjadi",a)

b =10
print("\nnilai b =",b)

#modulus dan floor division
b%= 3
print("nilai b %= 3,nilai b menjadi ",b)

b =10
print("\nnilai b=",b)

b//= 3
print("nilai b//= 3,nilai b menjadi",b)

#pangkat atau exponen
a =5
print("\nnilai =",a)
a**=3
print("nilai a**=3,nilai a menjadi",a)

#operasi logika
#or
c =True
print("\nnilai c=",c)
c |= False
print("nilai c |= false,nilai c menjadi",c)
c = False
print("nilai c =",c)
c|= False
print("nilai c |= false, nilai c menjadi",c)

#and
c =True
print("\nnilai c =" ,c)
c&= False
print("nilai c &= false,nilai c menjadi",c)
c=True
print("nilai c =",c)
c &= True
print("nilai c &= true,nilai c menjadi",c)
c = False
print("\nnilai c =",c)
c &= False
print("nilai c &= false,nilai c menjadi",c)

#xor
c =True
print("\nnilai c =",c)
c ^= False
print("nilai c^= true,nilai c menjadi",c)

#shift
d=0b0100
print("\nnilai d =",format(d,"04b"))
d>>= 2
print("nilai d>> 2,nilai d menjadi",format(d,"04b"))
d<<=1
print("nilai d<<= 1,nilai d menjadi",format(d,"04b"))
      