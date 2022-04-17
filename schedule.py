tableHeader = "+---------------+----------+----------+----------+----------+----------+----------+\n|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |\n+---------------+----------+----------+----------+----------+----------+----------+"
tableRow =    "+---------------+----------+----------+----------+----------+----------+----------+"
hours = ['08:00 - 08:55', '08:55 - 09:50', '10:00 - 10:55', '10:55 - 11:50', '12:00 - 12:55',
         '12:55 - 13:50', '14:00 - 14:55', '14:55 - 15:50', '16:00 - 16:55', '16:55 - 17:50',
         '18:00 - 18:55', '19:00 - 19:50', '19:50 - 20:40', '20:50 - 21:40', '21:40 - 22:30'] #[0, 14]

#Treatment and sorting of possible inputs
def Input():
    global args, action, code, time
    args = input()
    if(args == "Hasta la vista, beibe!"):
        action = False
        return action
    elif(len(args)>1):
        action, code, *time = args.split()
        return action, code, *time
    else:
        action = args
        return action

#Function that prints errors, if any, and the current state
def printIt():
    if(len(conflict)>0):
        for i in range(len(conflict)):
            print("!("+conflict[i]+")")
        conflict.clear()  #Conflict is flushed after displayed
    
    print(tableHeader)
    
    thereIs = [False]*15
    for i in range(15):
        for j in range(6):
            if (schedule[j][i] != None):               
                thereIs[i] = True

    for i in range(15):
        for j in range(6):
            if (thereIs[i]):              
                print("| "+hours[i]+" |", end="")
                for x in range(6):
                    if (schedule[x][i]):
                        var = (schedule[x][i]).center(10)
                        print(var, end="|")
                    else:
                        print("          ", end="|")
                print()
                print(tableRow)
            break
    
def timeTreatment():
    for i in range(len(time)):
        day, shift, hour = [], None, []
        temp = list(time)
        switch = False

        for char in (temp[i]):
            if (ord(char)>=48 and ord(char)<=57 and switch==False): #0-9
                day.append(char)
            elif (ord(char)>=65 and ord(char)<=90): #A-Z
                shift = char
                switch = True
            elif (ord(char)>=48 and ord(char)<=57 and switch==True): #0-9
                hour.append(char)
        
        offset = None
        if (shift == "M"):
            offset = 0
        elif (shift == "T"):
            offset = 5
        elif (shift == "N"):
            offset = 11

        exitLoop = False
        if (action == "+"):
            for i in range(len(day)):
                for j in range(len(hour)):
                    if(exitLoop):
                        break
                    if (schedule[int(day[i])-2][int(hour[j])-1+offset] != None): 
                        errorCode = args                    
                        conflict.append(errorCode)
                        exitLoop = True          
                    else:  
                        schedule[int(day[i])-2][int(hour[j])-1+offset] = code 

        elif (action == "-"):
            for i in range(len(day)):
                for j in range(len(hour)):
                    if(exitLoop):
                        break
                    if (schedule[int(day[i])-2][int(hour[j])-1+offset] == None or schedule[int(day[i])-2][int(hour[j])-1+offset] != code ): 
                        errorCode = args
                        conflict.append(errorCode)   
                        exitLoop = True             
                    else:
                        schedule[int(day[i])-2][int(hour[j])-1+offset] = None

#Building schedule array
skltn = [None]*15
schedule = []
for i in range(6): #Monday to Saturday
    schedule.append(list(skltn))

conflict = []
Input()
while(action):
    if(action == "?"):
        printIt()
    elif(action == "+" or action == "-"): 
        timeTreatment()
    else:
        quit()
    Input()