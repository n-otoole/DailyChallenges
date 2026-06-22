#from freeCodeCamp daily challenge 22/06/26 
#Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

#Letter	Leet
#a	4
#e	3
#g	9
#i	1
#l	1
#o	0
#s	5
#t	7
#Characters with no substitution are left unchanged.
def make_leet(s):
    newS = ""
    for i in range(len(s)):
        if s[i] == "a":
            newS = newS + "4"
        elif s[i] == "e":
            newS = newS+"3"
        elif s[i] == "g":
            newS = newS+"9"
        elif s[i] == "i" or s[i] == "l":
            newS = newS + "1"
        elif s[i] == "o":
            newS = newS + "0"
        elif s[i] == "s":
            newS =newS +"5"
        elif s[i] == "t": 
            newS = newS + "7"       
        else:
            newS = newS + s[i]

    return newS
