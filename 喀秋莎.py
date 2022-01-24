from pynput.keyboard import Key, Controller
import time
t=0.6

#mu="3./1;/3./1;/4/4;./4]/3;/2;/3;/1;/7-./3-;/7-./3-;/2;/2]/2]/1;/7-;/6- "#3]/2]/1]/2]/3]/2]/3]/4]/
#mu2="3/6;./6]/5/6;/5;/4/3;/2;/3/6-/0;/4/2;/3./1;/7-;/3-]/3-]/1;/7-;/6- /6- /6- /6- "
#mu="3/6/5/6;/5;/4/3;/2;/3/6-/0;/4/2;/3./1;/7-;/3-;/1;/7-;/6- "#;/6-]/6-]/6-
mu="4/2;/3./1;/7-;/3-;/1;/7-;/6- "
mu3="6-./7-;/1./6-;/1/7-;/6-;/7-/3-;/0;/7-./1;/2./7-;/2;/2;/1;/7-;/6- "
mu4="3/6/5/6;/5;/4/3;/2;/3/6-/0;/4/2;/3./1;/7-;/3-;/1;/7-;/6- "
mu5_1="3/6/5/6;/5;/4;/4;/3;/2;/3/6-/0;/4/2;/3./1;"
mu5_2="3/4/3/4;/3;/2;/2;/1;/7-;/1/6-/0;/2/7-;/1./1;/7-;/3-;/1;/7-;/6- "
mu5_r="7-;/3-;/1;/7-;/6- "
#mu6="3/3;/3;/4;/5./6>/3/6/6>/5/6;./5]/6>/4/3;./2]/6>/3/6-/0;/4/2;/3./6-;/5]/4;./3;./2]/6-;/6-]/6-]/6-"
mu6="1;/1;/2;/3;/6 "
#mu6="7-;/7-;/1;/4;/6 "


mulst={"1-":"z","2-":"x","3-":"c","4-":"v","5-":"b","6-":"n","7-":"m","1":"a","2":"s","3":"d","4":"f","5":"g","6":"h","7":"j","1+":"q","2+":"w","3+":"e","4+":"r","5+":"t","6+":"y","7+":"u"}
def tw(ti):
    time.sleep(t*ti)
def cp(bu):
    Controller().press(bu)
    Controller().release(bu)
def dec(mus):
    global mulst
    music=mus.split("/")
    for i in music:
        num=i[0]
        if num!="0":
            if "-" in i:
                rem =i[2:len(i)]
                let=mulst[num+"-"]
                #print(num+"-",rem)
            elif "+" in i:
                rem = i[2:len(i)]
                let=mulst[num+"+"]
                #print(num + "+", rem)
            else:
                rem = i[1:len(i)]
                let=mulst[num]
                #print(num, rem)
        else:
            rem = i[1:len(i)]

        if rem==".":
            n=1.5
        elif rem==";":
            n=0.5
        elif rem=="]":
            n=0.25
        elif rem==";.":
            n=0.75
        elif rem==" ":
            n=2
        elif rem == "  ":
            n=3
        elif rem=="   ":
            n=4
        elif rem=="=":
            n=0.125
        elif rem==">":
            n=0
        else:
            n=1
            #print("a")
        if num!="0":
            cp(let)
        #print("cp(%s)"%let)
        if n!=0:
            tw(n)
        #print("tw(%s)"%n)


time.sleep(5)
dec(mu)
#dec(mu2)
for i in range(4):
    dec(mu3)
    dec(mu4)
    dec(mu5_1)
    dec(mu5_r)
dec(mu3)
dec(mu4)
dec(mu5_1)
dec(mu5_r)