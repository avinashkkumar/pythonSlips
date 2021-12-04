# B) Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case. 
# Further modify the program to reverse a string word by word and print it in lower case.

class stringMan():
    s = ""
    rs = ""
    def getString(self):
        self.s = input("Enter a string for manupulation : ")

    def printString(self):
        print(self.s)
    
    def getString(self):
        self.s = input("Enter the string for manupulation : ")
    
    def stringReverse(self):
        t = self.s.split()
        for i in range(len(t)):
            self.rs = t[i] + " " + self.rs
    
    

s1 = stringMan()
s1.getString()
s1.printString()
s1.stringReverse()
print(s1.rs.upper())
print(s1.rs.lower())
        
