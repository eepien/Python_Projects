from pathlib import Path
# Absolute path: starts from the rool of our pathlist, e.g. c:\Program Files\Microsoft
#Relative path starts from the current directory, e.g. ecommerce
path = Path("ecommerce")
print(path.exists())          #returns true if ecommerce directory exists.

path2 = Path("emails")
print(path2.mkdir())            # creates directory ./emails. Will return an error if path already exists
print(path2.rmdir())            # removes directory ./emails. Will return an error if path does not exist.

path = Path()
#print(path.glob("*.py"))       #this line just gives you a generator object.
# To see all python files in the current directory, we do the following loop.
for file in path.glob("*.py"):  #"*" = all files/dir, "a*.py" = all python files with filename starting with a....
    print(file)
#see program directory2 for a cleaner code

