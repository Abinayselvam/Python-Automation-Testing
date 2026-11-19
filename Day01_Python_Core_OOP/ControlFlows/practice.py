
#problem1
username = "Abinaya";
password = "abi@1234";

input_name = input("Enter username:");
input_password = input("Enter password:");

if(username == input_name and password == input_password):
   print("Logined Successfull");
elif username != input_name:
    print("Invalid username")

else:
    print("Invalid password")

#problem2
number = int(input("Enter the number:"));
if number>0:
    print("Positive");
elif number<0:
    print("Negative");
else:
    print("Zero");