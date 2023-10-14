#print ("Hello World")
#print ("This is the second line")
#print("Simple Interest")
#principal= float(input("provide Principal"))
#rate_of_interest=float(input("provide rate of interest in %"))
#time =int(input("provide the duration of the loan in years"))
#si=principal*rate_of_interest*time/100
#totalPayable = principal + si
#print(totalPayable)
#print(si)

# parking lot problem:
# car, bikes, every hour of bike needs to pay 10 Rs, and Car , 20 Rs
# Parking lot is open for 6 hours a day
# no of cars and no of bikes as an input and then calculate what is the total collection for the day
# 10000 it is a good day/Profitable day , bad day

#carPerHour =20
#bikePerHour=10
#parkingHoursPerDay=6




#noOfCars = int(input("Please enter no of cars:"))
#noPfBikes = int(input("Please enter no of bikes:"))
#
#totalPaymentCollection =0
#if noOfCars>0:
   #totalPaymentCollection += noOfCars*carPerHour*parkingHoursPerDay
#elif noPfBikes >0:
   #totalPaymentCollection += noPfBikes*carPerHour*parkingHoursPerDay

   #if totalPaymentCollection>10000:
      #print("It is good day, have some profit")
   #else:
      #print("It is a bad day, no profit earned")

'''number= int(input("Please enter a limit of odd numbers:"))
sum=0
for i in range(0,number,1):
    if (i %2 !=0):
      print(i)
      sum += i
      print("even number:", i)'''

'''print("!!! SIMPLE INTEREST !!!")
principal= float(input("Please provide Principal Amount "))
interestRate= float(input("Rate of Interest in % "))
Time=float(input("Please mention time duration of loan in years "))
SI=principal*interestRate*Time/100
PayableAmount=principal + SI
print("Toatal Payable amount ", PayableAmount)'''


carPerHour=50
bikePerHour=20
perkingHoursPerday=9
noOfCars= int(input("Please enter no of Cars "))
noOfBikes= int(input("Please enter no of Bikes"))
totalcollection= (noOfCars*carPerHour + noOfBikes*bikePerHour)*perkingHoursPerday
print(totalcollection)
print("Good Day" if totalcollection>5000 else "Bad Day")













                    

      

      




    

               
                 