#code by top

import random
import pygame as pyg
import time
    
def generate_grid(mode="r"):
    global horizontal,vertical,vgrid,hgrid,hnumbr,vnumbr,gameDisplay

    if mode=="r":
    #generating random 0s and 1s
        hnumbr=int(input("Enter number of rows"))+1
        vnumbr=int(input("Enter number of columns"))+1
        horizontal=[random.choice([0,1]) for x in range(hnumbr)]
        vertical=[random.choice([0,1]) for x in range(vnumbr)]
    elif mode=="t":
        #text, vowels is 1, otherwise 0
        htext=input("Enter Horizontal text")
        vtext=input("Enter Vertical text")
        hnumbr=len(htext)+1
        vnumbr=len(vtext)+1
        horizontal=[0]+[0 if a.lower() in ["a","e","i","o","u"] else 1 for a in htext]
        vertical=[0]+[0 if a.lower() in ["a","e","i","o","u"] else 1 for a in vtext]
    elif mode=="n":
        #number, even is 1, otherwise 0
        hnum=input("Enter horizontal number")
        vnum=input("Enter vertical number")
        hnumbr=len(hnum)+1
        vnumbr=len(vnum)+1
        horizontal=[0]+[0 if int(a)%2==0 else 1 for a in hnum]
        vertical=[0]+[0 if int(a)%2==0 else 1 for a in vnum]

    #Generating Vertical grid
    vgrid=[]
    for x in vertical:
        if x==1:
            vgrid.append([1,0]*int(hnumbr/2))
        elif x==0:
            #odd even int issues
            if hnumbr%2==1:
                vgrid.append([0,1]*(int(hnumbr/2)-1) + [0,1])
            else:
                vgrid.append([0,1]*(int(hnumbr/2)-1) + [0,0])

    #generating Horizontal grid
    hgrid=[]
    for x in horizontal:
        if x==1:
            hgrid.append([1,0]*int(vnumbr/2))
        elif x==0:
            #odd even int issues
            if vnumbr%2==1:
                hgrid.append([0,1]*(int(vnumbr/2)-1) + [0,1])
            else:
                hgrid.append([0,1]*(int(vnumbr/2)-1) + [0,0])

    gameDisplay = pyg.display.set_mode(((vnumbr+5)*10,(hnumbr+5)*10))
    gameDisplay.fill((255,255,255))
    pyg.display.update()

def color(primary=(255,0,0),secondary=(0,255,255)):
    #Filling color between the lines of the pattern
    rstate=1
    for row in range(1,hnumbr):
        #swapping starting colour states for all rows except 1 which is coloured by default
        if row!=1:          
            if horizontal[row-1]==1:
                if scstate==0:
                    scstate=1
                else:
                    scstate=0
        else:
            scstate=1

        #Making the start colour state the actual state
        cstate=int(str(scstate))
        
        for col in range(1,vnumbr):
            #Alternating wall variable based on the row since it alternates
            wall=vertical[col]
            if rstate==0:
                if wall==1:
                    wall=0
                else:
                    wall=1
            #Painting it if the colour state permits (Note that cstate==0 was supposed to be no paint, but I made it a different colour to make it look better
            if cstate==1:
                    pyg.draw.rect(gameDisplay,primary,((col*10),(row*10),10,10),0)
                    pyg.display.update()
            else:
                    pyg.draw.rect(gameDisplay,secondary,((col*10),(row*10),10,10),0)
                    pyg.display.update()
            #Swapping colour states if there's a wall ahead
            if wall==1:
                if cstate==0:
                    cstate=1
                else:
                    cstate=0
        #This manages the row alternations
        if rstate==0:
                    rstate=1
        else:
                    rstate=0


def lines():
    #Draws the actual lines

    #Vertical lines
    rown=1
    for row in vgrid:
        linen=1
        for line in row:
            if line==1:
                pyg.draw.line(gameDisplay,(0,0,0),(rown*10,linen*10),(rown*10,(linen*10)+10))
                pyg.display.update()
            linen+=1
        rown+=1
    pyg.display.update()

    #Horizontal lines
    coln=1
    for col in hgrid:
        linen=1
        for line in col:
            if line==1:
                pyg.draw.line(gameDisplay,(0,0,0),(linen*10,coln*10),((linen*10)+10,coln*10))
                pyg.display.update()
            linen+=1
        coln+=1
    pyg.display.update()

def border():
    #Draws a border
    pyg.draw.rect(gameDisplay,(0,0,0),(10,10,(vnumbr-0.9)*10,(hnumbr-0.9)*10),1)
    pyg.display.update()


def main():
    pyg.init()

    mode=input("Enter desired mode, Options - r,t,n (r is random, t is text and n is number ")
    #You can manually add colours as you'd like here for more default options
    colors={"red":(255,0,0),"orange":(255,128,0),"yellow":(255,255,0),"lime":(128,255,0),"green":(0,255,0),"teal":(0,255,128),"cyan":(0,255,255),"lblue":(0,128,255),"blue":(0,0,255),"purple":(128,0,255),"pink":(255,0,255),"gray":(128,128,128),"black":(0,0,0),"white":(255,255,255)}
    print(f"""Possible colours are - {" ".join(colors.keys())}""")
    
    primary=input("Enter Primary color ")
    #custom primary colors
    if primary.lower() not in colors:
        print("You might have entered that colour incorrectly or we don't have that one, could you please input the rgb value? (It should look like R=255, G=0, B=0 for red, as an example)")
        pcolor=(int(input("Red-")),int(input("Green-")),int(input("Blue-")))
    else:
        pcolor=colors[primary.lower()]
        
    secondary=input("Enter secondary color ")
    #custom secondary colors
    if secondary.lower() not in colors:
        print("You might have entered that colour incorrectly or we don't have that one, could you please input the rgb value? (It should look like R=255, G=0, B=0 for red, as an example)")
        scolor=(int(input("Red-")),int(input("Green-")),int(input("Blue-")))
    else:
        scolor=colors[secondary.lower()]
    
    generate_grid(mode.lower()[0])
    lines()
    color(pcolor,scolor)
    lines()
    border()
    

if __name__=="__main__":
    main()
