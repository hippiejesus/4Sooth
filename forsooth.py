import re
import os
import random as rand
v = {}
o = {}
o_num = 0
class object:
    def __init__(self,inn):
        global o_num
        self.v = {}
        self.ID = o_num
        o_num += 1
        self.desc = inn
        
        
def interpret(command):
    global v
    clist = command.split()
    if command[0] == 'p':
        interpret('4 n p -> '+ command[2:])
    
    elif command[0] == '£':
        r = rand.randint(int(clist[2]),int(clist[3]))
        interpret('4 n d '+ clist[1]+' '+str(r))
    
    elif command[0] == 'd':
        interpret('4 n d '+ command[2:])
        
    elif command[0] == 'D':
        interpret('4 n D '+ command[2:])
        
    elif command[0] == 'i':
        interpret('4 n d '+command[2]+' 0')
    
    elif command[0] in ['+','-','*','/']:
        interpret('4 n '+command)
        
    elif command[0] == '@':
        exec(command[1:])
    
    elif command[0]=='4':
        
        if clist[1] == 'n':
            if clist[2] == 'p':
                if clist[3] == '->':
                    #eg(4 n p -> hi
                    rawString = ''
                    newString = "print('"
                    for letter in command[9:].split():
                        if letter[0]=='|':
                            try:
                                te = eval(v[letter[1]])
                            except:
                                te = v[letter[1]]
                            newString += str(te)+' '
                            rawString += str(te)+' '
                        else: 
                            rawString += str(letter)+' '
                            newString += str(letter)+' '
                    newString += "')"
                    if rawString[0]=='!':
                        interpret(rawString[2:])
                    else:
                        try:
                            exec(newString)
                        except:
                            exec(rawString)
            elif clist[2] == 'D':
                t = command[8:]
                v.update({clist[3]:eval(clist[4])})
            elif clist[2] == 'd':
                t = command[8:]
                v.update({clist[3]:t})
            elif clist[2] == '~':
                t = input(str(clist[3]))
                v.update({clist[4]:t})
            elif clist[2] == '°':
                t = object(clist[4])
                o.update({t.ID:t})
                v.update({clist[3]:t.ID})
            elif clist[2] in ['+','-','/','*']:
                var = str(v[clist[3]])
                op = clist[2]
                try:
                    answer = eval(var+op+clist[4])
                except:
                    answer = var + clist[4]
                v[clist[3]] = answer
        elif clist[1] == 'm':
            commands = command[4:].split()
            for com in commands:
                com = re.sub('_',' ',com)
                interpret(com)
        elif clist[1] == 'c':
            if clist[2] == '^':
                expression = clist[3]
                clist.pop(0)
                clist.pop(0)
                clist.pop(0)
                clist.pop(0)
                expression = re.sub('_',' ',expression)
                newExp = ''
                for item in clist:
                    newExp += item+' '
                while(eval(expression)):
                    interpret(newExp)
    elif command[0] == 'r':
        clist.pop(0)
        ranget = clist[0]
        clist.pop(0)
        newExp = ''
        for i in clist:
            newExp += i+' '
        for x in range(int(ranget)):
            interpret(newExp)

if __name__=='__main__':
    os.system('clear')
    print('FORSOOTH - v.1 - Enjoy!')
    inn = input('run --> ')
    
    f = open('/storage/emulated/0/qpython/'+inn,'r')
    for line in f.readlines():
        #try:
        interpret(line)
        #except:
            #print('forsooth')
    
    """while True:
        command = input('$: ')
        #try:
        interpret(command)
        #except:
            #print('forsooth')"""

