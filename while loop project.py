# while_loop_accoutn_sign_in

cemail = "dog.cat1234"
cphone_number = "9000000000"
cpassword = "ant123bat456"

print("\n\n")
print("sign in to account")
user = input("Are you ready to sign in with your account (Yes or NO): ").lower()

while user == "yes":
    uem_pn = input("Email or Phone: ")
    
    if uem_pn == cemail or uem_pn == cphone_number:
        passw = input("Password: ")
        
        while True:
            
            if passw == cpassword:
                        
                        print("." * 10)
                        print("Welcome")
                        print("." * 10)
                        break
                    
            else:
                again = input("Incorract Password.\nTry again (Yes or NO): ").lower()  

                if again != "yes":
                     user = "no"
                     break
        
        break
    
    else:
        user = input("Couldn't find this account.\nTry again (Yes or NO): ").lower()

else:
    print("OK")   
