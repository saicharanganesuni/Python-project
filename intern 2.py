# The below function splits the snetence using the split function and finds the length of the list formed.
def cnt(st):
    st_split=st.split(" ")
    res=len(st_split)
    # Returns the list length.
    return res
# Taking input string from the end user.
st=input("Enter the string : ")
#Loop to validate the input and goes to next word count until valid input is given.
while((not st.strip()) or (st[0]==" ")):
    print("Error: No input detected. Please enter some text.")
    print()
    st=input("Enter the string : ")
# Function is calling with name cnt with attribute given sentence.
words_cnt=cnt(st)
# Displays the number of words.
print("Number of words in the given sentence are :",words_cnt)
'''
This program gives the number of words present in the given input or sentence by using split functions.
'''