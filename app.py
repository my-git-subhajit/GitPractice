'''from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST', 'PUT'])
def helloWorld():
    return "Hello World!"

@app.route('/contactus')
def contactUS():
    return "Contact Subhajit"

@app.route('/pricing')
def pricing():
    return "1000"

if __name__=="__main__":
  app.run(debug=True)'''  # Correct code
  
import math

def rev(num):
    return int (num !=0) and ((num % 10) * \
                              (10**int(math.log(num, 10))) + \
                              rev (num // 10))
test_number = int(input("Please enter number to be checked: "))
#test_number=5244321187
print ("The Original No is: " + str(test_number))
res = test_number == rev(test_number)
print ("Is the No Pelindrome ? : " + str(res))







                             
    

       
                          
