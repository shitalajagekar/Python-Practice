#  Introduction of file program

"""
#  Reading a data from File
f=open("sample.txt","r")  # by default open() is read in mode
data=f.read() # used to read all lines of file
data = f.read(5) # read 5 characters of file
print(data)
f.close()

"""
# Writing a data into file
"""f=open("sample.txt","w")  
data= input("Enter the text to write into file...")
f.write(data)

f.close()
"""

# readline ()
"""f=open("sample.txt")
data= f.readline() # read one line at a time
print(data)

data= f.readline() # read second line of prg
print(data)

data= f.readline() # read third line of prg
print(data)
f.close()

"""

# readlines()
"""f=open("sample.txt","rb")
data= f.readlines() # read all lines at a time
print(data)
f.close()
"""
# write()

"""f = open("another.txt","w") # if file is not created then it create first then open it
f.write("First line of file...")
f.close()

"""
# append mode 
"""f = open("another.txt","a") # if file is not created then it create first then open it
f.write("\n third  line of file...")
f.close()

"""
# with open statement: then no need to close the file externally

"""with open ( "another.txt ","w") as f:
    f.write("First line of file")

with open("another.txt","r") as f:
    print(f.read())

"""
# prg to read lines from given file "poem.txt" and check "twinkle " word present or not

"""with open("poem.txt","w") as f:
    f.write("Twinkle, twinkle, little star\n How I wonder what you are \n Up above the world so high \n Like a diamond in the sky  \n Twinkle, twinkle little star \n How I wonder what you are")

with open("poem.txt","r") as f:

    data=f.read()
    if "Twinkle" in data:
        print(" Twinkle word present")
    else:
        print(" Twinkle word not present")

    """

# program 

"""def game():
    return 6542

score = game()
with open("score.txt") as f:
    highscore= f.read()

if highscore == "":
    with open("score.txt","w") as f:
            f.write(str(score))
elif int(highscore) < score:
        with open("score.txt","w") as f:
            f.write(str(score))


"""
# write a prog to write 2's table into file
with open(" multiplication_table_of_2","w") as f:
    for i in range(1,11):
        f.write(f" 2 * {i} = {2* i} \n")