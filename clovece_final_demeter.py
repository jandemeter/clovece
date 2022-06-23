import random


def kocka(): #hodi sa kocka, ak padne 6 program sa zavola este raz a cisla sa scitaju
    a = random.randint(1,6)
    if a==6:
        return a + kocka()
    else:
        return a

        
def gensachovnicu(n):   #generuje a vrati sachovnicu  
    global stred 
    s = n
    r = n
    sachovnica = []
    stred = int((n-1)/2)
    stred += 1 
    
   
    #vytvori prazdny 2d list
    for i in range(r+1):
        l = []
        for j in range(s+1):
            l.append(" ")
        sachovnica.append(l)
    
    #prideli cisla riadkov a stplcov, osetrene aby stale od 1-9
    for i in range(n):
        if i>=10:
            p = i//10
            sachovnica[0][i+1] = i-10*p
        else:
            sachovnica[0][i+1] = i
    
    for j in range(n):
        if j >=10:
            p = j//10
            sachovnica[j+1][0] = j-10*p
        else:    
            sachovnica[j+1][0] = j
    

    #prideli policka na pohyb
    sachovnica[stred][1] = "*"
    sachovnica[stred][n] = "*"
    sachovnica[1][stred] = "*"
    sachovnica[n][stred] = "*"

    for i in range(n):
        sachovnica[stred-1][1+i] = "*"
        sachovnica[stred+1][1+i] = "*"

        sachovnica[1+i][stred-1] = "*"
        sachovnica[1+i][stred+1] = "*"


    #prideli domceky
    for i in range(stred-2):
        sachovnica[stred][i+2] = "D"
        sachovnica[stred][stred+1+i] = "D"
        
        sachovnica[i+2][stred] = "D"
        sachovnica[stred+1+i][stred] = "D"    

    #prideli domceky x do stredu plochy     
    sachovnica[stred][stred] = "X"   

    #panacik A a B
    sachovnica[1][stred+1] = "A"
    sachovnica[(2*stred)-1][stred - 1] = "B"

    return sachovnica

def tlacsachovnicu(sachovnica):  #vykresli sachovnicu 

    for i in sachovnica:
        for j in i:
            print(j,end=" ")
        print()

def dom_a():      #da mi domcek pre A do listu aby som potom mohol zistovat ci ma este volne policka     
    domcek_a=[]
    for i in range(stred-2):
        c = sachovnica[i+2][stred]
        domcek_a.append(c)
    return domcek_a 

def dom_b():     #da mi domcek pre B do listu aby som potom mohol zistovat ci ma este volne policka  
    domcek_b= []
    for i in range(stred-2):
        c = sachovnica[stred+1+i][stred]
        domcek_b.append(c)
    return domcek_b


def pohyb_hraca():

    #pozicia A na zaciatku
    x = 1
    y = stred + 1
    
    #pozicia B na zaciatku 
    x1 = (2*stred)-1
    y1 = stred - 1
   
   

    
    while True:
        

        #hodi sa kocka pre hraca A
        pohyb_a = kocka()
        print("hrac A hodil " + str(pohyb_a) ) 
      

        
        
        for i in range(pohyb_a): #pohyb hraca a
           
            #pohyb pre pravu stranu hracej plochy          
            if (y > stred):
                if x == (stred*2)-1 and sachovnica[x][y-1] == "*":
                    sachovnica[x][y] = "*"
                    y = y - 1
                    sachovnica[x][y] = "A"
                    
                elif sachovnica[x+1][y] == "*":
                    sachovnica[x][y] = "*"
                    x += 1
                    sachovnica[x][y] = "A"
                    

                elif x == stred-1 and sachovnica[x][y+1] == "*":
                    sachovnica[x][y] = "*"
                    y += 1
                    sachovnica[x][y] = "A"
                   


                elif x == stred+1 and sachovnica[x][y-1] == "*":
                    sachovnica[x][y] = "*"
                    y = y - 1
                    sachovnica[x][y] = "A"
                   
            
            #pohyb pre lavu stranu hracej plochy 
            elif y < stred:
                if sachovnica[x-1][y] == "*":
                    sachovnica[x][y] = "*"
                    x -= 1
                    sachovnica[x][y] = "A"
                    

                elif x == stred-1 and sachovnica[x][y+1] == "*":
                    sachovnica[x][y] = "*"
                    y += 1
                    sachovnica[x][y] = "A"
                    


                elif x == stred+1 and sachovnica[x][y-1] == "*":
                    sachovnica[x][y] = "*"
                    y = y - 1
                    sachovnica[x][y] = "A"
                   

                elif x == 1 and sachovnica[x][y+1] == "*":
                    sachovnica[x][y] = "*"
                    y += 1
                    sachovnica[x][y] = "A"
                    
            #pohyb stred dole
            elif y==stred and x == (2*stred)-1:
                if sachovnica[x][y-1] == "*":
                    sachovnica[x][y] = "*"
                    y -= 1
                    sachovnica[x][y] = "A"
                   
            
            #pohyb do domceka
            elif y==stred and x == 1:
                if sachovnica[x+1][y] == "D" :
                    sachovnica[x][y] = "*"
                    x +=  1
                    sachovnica[x][y] = "A"
                   
            #pohyb v domceku 
            elif (y == stred) and (x>1):
                if (sachovnica[x+1][y] == "D" ):
                    sachovnica[x][y] = "D"
                    x +=  1
                    sachovnica[x][y] = "A"
                elif sachovnica[x+1][y] == "X" or sachovnica[x+1][y] == "A":
                    x = 1
                    y = stred + 1
                    if "D" in dom_a():
                        sachovnica[1][stred+1] = "A"
                        break
                    else:
                        break 

        tlacsachovnicu(sachovnica)          #ukaze sachonicu po pohybe A  a skontroluje ci uz nema plny domcek ak ano hra skonci 
        if 'D' not in dom_a():
            print('Hrac A vyhral')
            break


        
        pohyb_b = kocka()  #kocka pre hraca B
        print("hrac B hodil " + str(pohyb_b))    

        for i in range(pohyb_b): #pohyb hraca b
           
            #pohyb pre pravu stranu hracej plochy          
            if (y1 > stred):
                if (x1 == (stred*2)-1) and (sachovnica[x1][y1-1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 = y1 - 1
                    sachovnica[x1][y1] = "B"
                    
                elif sachovnica[x1+1][y1] == "*":
                    sachovnica[x1][y1] = "*"
                    x1 += 1
                    sachovnica[x1][y1] = "B"
                    

                elif (x1 == stred-1) and (sachovnica[x1][y1+1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 += 1
                    sachovnica[x1][y1] = "B"
                   


                elif (x1 == stred+1) and (sachovnica[x1][y1-1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 = y1 - 1
                    sachovnica[x1][y1] = "B"
                   
            
            #pohyb pre lavu stranu hracej plochy 
            elif (y1 < stred):
                if sachovnica[x1-1][y1] == "*":
                    sachovnica[x1][y1] = "*"
                    x1 -= 1
                    sachovnica[x1][y1] = "B"
                    

                elif (x1 == stred-1) and (sachovnica[x1][y1+1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 += 1
                    sachovnica[x1][y1] = "B"
                    


                elif (x1 == stred+1) and (sachovnica[x1][y1-1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 = y1 - 1
                    sachovnica[x1][y1] = "B"
                   

                elif (x1 == 1) and (sachovnica[x1][y1+1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 += 1
                    sachovnica[x1][y1] = "B"
                    
            #pohyb stred hore
            elif (x1==1) and (y1 == stred):
                if (sachovnica[x1][y1+1] == "*"):
                    sachovnica[x1][y1] = "*"
                    y1 += 1
                    sachovnica[x1][y1] = "B"
                   
            
            #pohyb do domceka

            elif (y1==stred) and (x1 == (2*stred)-1):
                if (sachovnica[x1-1][y1] == "D" ):
                    sachovnica[x1][y1] = "*"
                    x1 -=  1
                    sachovnica[x1][y1] = "B"
                   
            #pohyb v domceku 
            elif (y1 == stred) and (x1<(2*stred)-1):
                if (sachovnica[x1-1][y1] == "D" ):
                    sachovnica[x1][y1] = "D"
                    x1 -=  1
                    sachovnica[x1][y1] = "B"

                elif sachovnica[x1-1][y1] == "X" or sachovnica[x1-1][y1] == "B":
                    x1 = (2*stred)-1
                    y1 = stred - 1
                    if "D" in dom_b():
                        sachovnica[(2*stred)-1][stred - 1] = "B"
                        break 
                    else:
                        break

        tlacsachovnicu(sachovnica)
        if 'D' not in dom_b():
            print('Hrac B vyhral')
            break
 

        
                    


           
n = int(input("velkost sachovnice:"))
sachovnica = gensachovnicu(n)
tlacsachovnicu(sachovnica)
pohyb_hraca()










        



