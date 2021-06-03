from sys import argv #this is from a system file

script, filename = argv #script that will print after that command

txt = open(filename) #opens the filename

print(f"Here's your file {filename}:")  #prints
print(txt.read())  #reads and prints

print("Type the filename again:") #the print for the input to type the filename
txt_again = open(file_again) #opens the file

print(txt_again.read()) #prints the text in the file
