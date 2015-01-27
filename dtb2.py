running = True # Prepare for the main loop
ip=[] # Prepare the list that will be used in the main loop.

def convert(octet): #Octet here refers to one of the 4 octets that make up a decimal IP address (e.g. octet.octet.octet.octet or 192.168.1.1)

    bin = [] # bin = Binary, as in the Binary octet
    
    if len(octet) > 3:
        return 1 # Checks that the octet in question is not more than 3 digits long.


    try:
        octet = int(octet)
    except ValueError:
        return 2 # Tries to convert the octet to an integer, or at least fail gracefully.

    if octet > 255:
        return 3 # Checks that the octet isn't beyond the maximum of 255.
    


    while octet > 0: # Math
        
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

    return bin # Return the list which will make up the resulting binary octet.



def ArrangeBinary(octet0, octet1, octet2, octet3):


    if octet0 == 1:
        print "Octet is too long, try again."
        return 0
    elif octet0 == 2:
        print "Octet contains an ASCII character or is blank. Try again."
        return 1


    if octet1 == 1:
        print "Octet is too long, try again."
        return 0
    elif octet1 == 2:
        print "Octet contains an ASCII character or is blank. Try again."
        return 1


    if octet2 == 1:
        print "Octet is too long, try again."
        return 0
    elif octet2 == 2:
        print "Octet contains an ASCII character or is blank. Try again."
        return 1
    

    if octet3 == 1:
        print "Octet is too long, try again."
        return 0
    elif octet3 == 2:
        print "Octet contains an ASCII character or is blank. Try again."
        return 1

    else:
        x = ''.join(map(str, octet0 + octet1 + octet2 + octet3))
        FULL_IP = x[0:7] + '.' + x[8:15] + '.' + x[16:24] + '.' + x[25:]
        return FULL_IP
    




## ________________________________________________________________________________________________________
## Main Thread

while running == True:

    ip.append(raw_input("Please enter the first octet: ")) # Collect the octets one by one, because lol regex.
    ip.append(raw_input("Please enter the first octet: ")) 
    ip.append(raw_input("Please enter the first octet: "))
    ip.append(raw_input("Please enter the first octet: "))

    print ip[0] + "." + ip[1] + "." + ip[2] + "." + ip[3] # Print the IP given as a form of debugging.

    x = raw_input("Would you like to convert to binary? [Y/n]: ") # If answer Y or just press enter, will convert.
    if x == "" or x.lower == "y":
             

        print ArrangeBinary(convert(ip[0]), convert(ip[1]), convert(ip[2]), convert(ip[3])) # Print the result of ArrangeBinary() called with the 4 results of convert()
        # on our IP octets
        

    else: # Any other input stops the program.
        print "Okay, have a good day!"
        break


        
    ip=[]
