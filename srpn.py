#This is the source file for the SRPN.

#An SRPN can call a random number from a list of organised numbers, this list stores the numbers in the correct order.
rlist=[1804289383,846930886,1681692777,1714636915,1957747793,
424238335,719885386,1649760492,596516649,
1189641421,1025202362,1350490027,783368690,
1102520059,2044897763,1967513926,1365180540,1540383426,
304089172,1303455736,35005211,521595368,1804289383]

#This counter stores how many times a random number has been called, and increments once per call. Everytime "r" is called, this number increases.
rcount=0

#This is a function that ensures saturation limits are kept. If the values in the calculator pass saturation limits, they are brought back to the max or min allowed values.
def sat(y):
  if int(y) >= 2147483647:
    y = int(2147483647)
  elif int(y) <= -2147483648:
    y = int(-2147483648)
  return int(y)

#The stack is initialized as an empty list, this list will be used when operators are being input, and stores all the operands of the calculator. Operands are pulled from this list when operators are called, and the resulting operands are pushed back into the list.
stack = []

#This function provides all the functionality of the SRPN. The input to the SRPN is defined as the command. 
def process_command(command):
    
    #Returnval is the value which will be pushed back into the stack. It is defined as a global variable, to prevent the program from trying to call it before it has been initialised.
    global returnval

    #If an "=" is fed to the calculator, I display the most recent value of "returnval", this should always be the last or most recent value in the stack.
    if command == "=":
      print (sat(returnval)) #The "sat" function is called everytime we store or return values, ensuring saturation is not exceeded.

    #If the "d" operator is called, I want to display everything currently stored in the stack. This piece iterates though and prints all the values stored in the stack.
    elif command == "d":
        for i in stack:
          print (sat(i))
    
    #If the "r" operator is called, this piece calls a value out of the random number list, when a value is called, it is stored to the stack and the r - counter iterates, ensuring the next call of "r" will return the next value in the random number list. If the r - count surpases the length of the random number list, a stack overflow error is displayed.
    elif command == "r":
      if rcount >= len(rlist):
        print ("Stack overflow.")
      else:
        stack.append(rlist[rcount])
        rcount == rcount + 1

    #If we havent recived a command of "=", "d" or "r", we enter into this section of the program.
    else:

      #Depending on the command, the program enters different processes, each process first checks if the stack is long enough to perform the operation, if it is, it calls the top 2 values in the stack, performs the operation, removes them from the stack, and then returns the result back to the top of the stack. This process is followed for all of the operators.

      #Addition
      if command == "+":
        if len(stack)==1:
          print("Stack underflow.")
        else:
          returnval = int(stack[-2])+int(stack[-1])
          stack.pop()
          stack.pop()
          stack.append(sat(returnval))

      #Subtraction
      elif command == "-":
        if len(stack)==1:
          print("Stack underflow.")
        else:
          returnval = int(stack[-2])-int(stack[-1])
          stack.pop()
          stack.pop()
          stack.append(sat(returnval))
      
      #Dividing
      elif command == "/":
        if len(stack)==1:
          print("Stack underflow.")
        #If the command is a "/", we must make sure that the operation is not dividing by 0. If it is, a Divide by 0 message is returned.
        elif int(stack[-1]) == 0:
          print("Divide by 0.")
        else:
          returnval = int(stack[-2])/int(stack[-1])
          stack.pop()
          stack.pop()
          stack.append(sat(returnval))

      #Multiplication
      elif command == "*":
        if len(stack)==1:
          print("Stack underflow.")
        else:
          returnval = int(stack[-2])*int(stack[-1])
          stack.pop()
          stack.pop()
          stack.append(sat(returnval))

      #Remainder
      elif command == "%":
        if len(stack)==1:
          print("Stack underflow.")
        else:
          returnval = int(stack[-2])%int(stack[-1])
          stack.pop()
          stack.pop()
          stack.append(sat(returnval))
      
      #Powers
      elif command == "^":
        if len(stack)==1:
          print("Stack underflow.")
        elif int(stack[-1]) >= 0:
          returnval = int(stack[-2])**int(stack[-1])
          stack.pop()
          stack.pop()
          stack.append(sat(returnval))
        #If the command is a "^", we must make sure that the operation is not taking a negative power. If it is, a negative power message is returned.
        else:
          print ("Negative power.")

      #If the command is not an operator, it is assumed to then be an operand, and is added to the stack.    
      else:
        stack.append(sat(command))
      
#This is the entry point for the program.
#Do not edit the below
if __name__ == "__main__": 
    while True:
        try:
            cmd = input()
            pc = process_command(cmd)
            if pc != None:
                print(str(pc))
        except:
            exit()
