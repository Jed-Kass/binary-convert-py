## Version 1.0
running = True # Prepare for the main loop
running1 = True
ip=[] # Prepare the list that will be used in the main loop.



def convert(octet): #Octet here refers to one of the 4 octets that make up a decimal IP address (e.g. octet.octet.octet.octet or 192.168.1.1)

    binary = []
    
        
    try:
        octet = int(octet)
    except ValueError, TypeError:
        return 2 # Tries to convert the octet to an integer, or at least fail gracefully.
    
    if octet == 0:
        full_string = "00000000"
        return full_string
    
    try:
        str(octet)
    except TypeError:
        return 3
    


    while octet > 0: # Math
                     # Here's how it works: if the given octet is lower than the value (e.g. 128, 64), then append a 0 to the binary list. If greater, subtract
                     # from that octet and append a 1 to the binary list. Search 'converting decimal to binary' to get a better sense of how this works.
                     
        if octet >= 128:
            binary.append(1)
            octet = octet - 128
        elif octet < 128:
            binary.append(0)

        if octet >= 64:
            binary.append(1)
            octet = octet - 64
        elif octet < 64:
            binary.append(0)

        if octet >= 32:
            binary.append(1)
            octet = octet - 32
        elif octet < 32:
            binary.append(0)

        if octet >= 16:
            binary.append(1)
            octet = octet - 16
        elif octet < 16:
            binary.append(0)

        if octet >= 8:
            binary.append(1)
            octet = octet - 8
        elif octet < 8:
            binary.append(0)

        if octet >= 4:
            binary.append(1)
            octet = octet - 4
        elif octet < 4:
            binary.append(0)

        if octet >= 2:
            binary.append(1)
            octet = octet - 2
        elif octet < 2:
            binary.append(0)

        if octet >= 1:
            binary.append(1)
            octet = octet - 1
        elif octet < 1 or octet == 0:
            binary.append(0)

    full_string = ""
    for numerals in binary:
        full_string = "".join((full_string, str(numerals)))

    return full_string # Return the list which will make up the resulting binary octet.



def error_checker(octet):

    if octet == 2:
        return 2
    elif octet == 3:
        return 3
    else:
        return 0
    

## ________________________________________________________________________________________________________
## Main Thread

while running1 == True: # For the sake of error handling, the main loop is held inside of another loop.
    while running == True:

        ip = str(raw_input("Please enter the IP address: "))
        ip_holdout = ip
        if ip.lower() == "quit":
            running = False
            running1 = False
            break
        

        if len(ip) > 15:
            print("One of the octets was too long. Please try again.")
            break
        error = 0

            


        
        digit_counter=0 ## Keep count of the number of digits we've progressed for the sake of removing unneeded portions of our IP address.
        octet_counter=0 ## Keeps track of the number of octets for the sake of placing said octet into octet_holder[].
        octet_holder=[] ## Holds the octets in a list.
         
        for octet in ip:
            if octet != ".":
                
                try:
                    int(octet)
                except ValueError:
                    error = 1
                    break
                
            if octet == ".": ## Checks whether we've reached the period after an octet, which helps parse the address.
                octet_holder.append(ip[:digit_counter]) ## Appends to octet_holder[] the octet up to (but not including) the period.
                ip = ip[digit_counter+1:len(ip)] ## Trashes the first octet and its period.
                

                try: ## Error checking
                    int(octet_holder[octet_counter]) ## Ensuring the currently handled octet is actually a number and ONLY a number.
                except ValueError:
                    error = 1
                    break
                try:
                    int(octet_holder[octet_counter])
                    str(octet_holder[octet_counter])
                except TypeError: # Checks for illegal characters
                    error = 4
                    break
                if int(octet_holder[octet_counter]) > 255: ## Ensure no numbers greater than 255 get through (which screws with the math).
                    error = 2
                    break ## End error checking
                    
                octet_counter = octet_counter + 1 ## Prepare for adding the next octet
                digit_counter = 0 ## Reset the digit counter.
                

            elif octet_counter == 3: ## Workaround for the fourth octet. Checks if we've dealt with the first 3 octets, then simply appends the rest to the final octet.
                octet_holder.append(ip) ## Doing it this way breaks error checking for the final octet.
            

                try: ## Error Checking for our fourth octet.
                    int(octet_holder[3])
                except ValueError:
                    error = 1
                    break
                try:
                    int(octet_holder[3])
                except TypeError:
                    error = 4

                if int(octet_holder[3]) > 255:
                    error = 2
                    break
                else:
                    break
            else: ## End Error Checking.
                digit_counter=digit_counter+1
2

        for items in octet_holder:
            if error_checker(items) == 2:
                error = 1
                break

            
        if error == 1: ## Remember that error checking from the for: loop?
            print("Only numbers and periods are allowed. Please try again.")
            break
        if error == 2: ## Here's where it pays off.
            print("One of the octets is too large. The max allowed is 255.")
            break
        if error == 4:
            print("Warning: Illegal character in octet. Please try again.")
            


            
        

        
        print("\n")
        print ip_holdout
        print("is...")
        try:
            print convert(octet_holder[0]) + '.' + convert(octet_holder[1]) + '.' + convert(octet_holder[2]) + '.' + convert(octet_holder[3])
        except IndexError:
            print("Warning: Illegal character[s]. Please try again.")
            break
        print("\n")




        
    ip=[]
