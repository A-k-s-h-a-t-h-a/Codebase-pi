'''magicno= 26
for n in range(101):
    if n is magicno:
        print(n, "is the magic no")
        break
    else:
        print(n)'''


for n in range(100):
    if n%4==0:
        print(n)


'''def bitcoin_to_usd(btc):
    amount= btc*627
    print(amount)

bitcoin_to_usd(10)
bitcoin_to_usd(198)'''



'''def allowed_age(his_age):
    girls_age= his_age/2 +7
    return girls_age

limit= allowed_age(27)
print("He can go out with", limit, "year olds")'''



'''def allowed_age(his_age):
    girls_age= his_age/2 +7
    return girls_age

for his_age in range(15,61):
       print(his_age,"can go out with", allowed_age(his_age), "year olds")'''



'''def age(his):
    gigi= his/1.8 +10
    print(gigi)

age(27)
age(41)
age(66)'''


'''def give_gender(gen='Unknown'):
    if gen is 'm':
        gen='Male'
    elif gen is 'f':
        gen='Female'
    #else:
        #gen='Invalid'
    print(gen)

give_gender('m')
give_gender('f')
give_gender()
give_gender('s')'''


'''def std_price(dist):
    if dist<50:
        fare= dist*8
    else:
        fare= 15+ dist*6
    print(fare)

std_price(67)

def actual_price(age, weekend, distance):
    if age<12 | age>60:
        return std_price(distance)*0.7          #30 percent discount on the fare

    if weekend:                                 #boolean
        if age<12 | age>60:
            return std_price(distance)*0.65     #35 percent discount on the fare
        else:
            return std_price(distance)*0.6     #40 percent discount on the fare

actual_price(10, 1, 80)                         # ? What is to be passed for weekend ?'''


'''def addition(*argus):
    total=0
    for a in argus:
        total+= a
    print(total)

addition(90,78,11)
addition(20)'''