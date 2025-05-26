
s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
j = len(s)
n = int(j/2)
for i in range (0 , n):
    a = s[i]
    s[i] = s[len(s)-i-1]
    s[len(s)-i-1] = a
    
print (s)