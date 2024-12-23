print( )
red = '\033[31m'
white = '\033[0m'
blue= '\033[34m'
yellow= '\033[33m'
green= '\033[32m'
purple= '\033[35m'

statement = "{}={}={}= {}Music App{}={}={}= ".format(red,white,blue,yellow,blue,white,red)
first ="{}PREV". format(white)
second = "{}NEXT".format(green)
last ="{}PAUSE".format(purple)
print (f"{statement:^90}")
print( )
print ("🔥▶{}RADIO GAGA".format (white))
print(" {} QUEEN". format(yellow))
print( )
print (f"{first:<20}")
print( )
print  (f"{second:^30}")
print( )
print(f"{last:^60}")


greeting = "WELCOME TO \n                  {} --   ARMBOOK  --".format(blue)
statement = "     {} Definitely not a rip off of".format(yellow)
new="    {} a certain other social ".format(yellow)
end="     {}networking site ".format(yellow)
honest = "{}Honest.{}".format(red,white)
login = "Username:"
last = "Password:"
print (f"{greeting:^100}")
print( )
print(f"{statement:>60}")
print(f"{new:>60}")
print(f"{end:>60}")
print( )
print(f"{honest:^65}")
print( )
print(f"{login:^55}")
print(f"{last:^55}")
