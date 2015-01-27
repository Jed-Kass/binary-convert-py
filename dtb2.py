## Version 0.6
running = True # Prepare for the main loop
running1 = True
ip=[] # Prepare the list that will be used in the main loop.

def convert(octet): #Octet here refers to one of the 4 octets that make up a decimal IP address (e.g. octet.octet.octet.octet or 192.168.1.1)

    bin = [] # bin = Binary, as in the Binary octet
    
    if len(octet) > 3:
        print octet
        return 1 # Checks that the octet in question is not more than 3 digits long.


    try:
        octet = int(octet)
    except ValueError:
        return 2 # Tries to convert the octet to an integer, or at least fail gracefully.

    if octet > 255:
        return 3 # Checks that the octet isn't beyond the maximum of 255.
    


    while octet > 0: # Math
                     # Here's how it works: if the given octet is lower than the value (e.g. 128, 64), then append a 0 to the binary list. If greater, subtract
                     # from that octet and append a 1 to the binary list. Search 'converting decimal to binary' to get a better sense of how this works.
                     
        if octet >= 128:
            bin.append(1)
            octet = octet - 128
        elif octet < 128:
            bin.append(0)

        if octet >= 64:
            bin.append(1)
            octet = octet - 64
        elif octet < 64:
            bin.append(0)

        if octet >= 32:
            bin.append(1)
            octet = octet - 32
        elif octet < 32:
            bin.append(0)

        if octet >= 16:
            bin.append(1)
            octet = octet - 16
        elif octet < 16:
            bin.append(0)

        if octet >= 8:
            bin.append(1)
            octet = octet - 8
        elif octet < 8:
            bin.append(0)

        if octet >= 4:
            bin.append(1)
            octet = octet - 4
        elif octet < 4:
            bin.append(0)

        if octet >= 2:
            bin.append(1)
            octet = octet - 2
        elif octet < 2:
            bin.append(0)

        if octet >= 1:
            bin.append(1)
            octet = octet - 1
        elif octet < 1:
            bin.append(0)

    full_string = ""
    full_string = full_string + str(bin[0]) + str(bin[1]) + str(bin[2]) + str(bin[3]) + str(bin[4]) + str(bin[5]) + str(bin[6]) + str(bin[7])

    return full_string # Return the list which will make up the resulting binary octet.



## ________________________________________________________________________________________________________
## Main Thread

while running1 == True: # For the sake of error handling, the main loop is held inside of another loop.
    while running == True:

        ip = str(raw_input("Please enter the IP address: "))
        ip_holdout = ip



        if len(ip) > 14:
            print "One of the octets was too long. Please try again."
            break


            


        
        digit_counter=0
        octet_counter=0
        octet_holder=[]
         
        for octet in ip:
            if octet == ".":
                octet_holder.append(ip[:digit_counter])
                ip = ip[digit_counter+1:len(ip)]
                

                try:
                    int(octet_holder[octet_counter])
                except ValueError:
                    print "Only numbers and periods are allowed. Please try again."
                    break
                if int(octet_holder[octet_counter]) > 255:
                    print "One of the octets is too large. The max allowed is 255."
                    break
                    
                octet_counter = octet_counter + 1
                digit_counter = 0
                

                
            elif octet_counter == 3:
                octet_holder.append(ip)
                break
            
            else:
                digit_counter=digit_counter+1
            

        
        
        print "\n"
        print ip_holdout
        print "is..."
        print convert(octet_holder[0]) + '.' + convert(octet_holder[1]) + '.' + convert(octet_holder[2]) + '.' + convert(octet_holder[3])
        print "\n"




        
    ip=[]
