# A) Write a Python script using class, which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case.
class stringUpper():
    string = ""
    def __init__(self):
        self.string = ""
        
    
    def getString(self,str):
        self.string = str

    def printString(self):
        print(self.string.upper())

st = stringUpper()

st.getString(input("Enter the string to be converted to the upper case : "))
st.printString()