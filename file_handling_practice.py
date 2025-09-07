# step-1 : writing to a file created  or overwrites a file
with open("myfile.txt", "w") as f:
    f.write("Hello, this is my first line. \n")
    f.write("I am learning file handling in Python. \n")

print("Step 1: file written successfully!")

# step 2: Reading the whole file
with open("myfile.txt", "r") as f:
    content = f.read()
    print("\nStep 2: Reading whole file")
    print(content)

# Step 3: Reading line by line
with open("myfile.txt", "r") as f:
    print("\nStep 3: Reading line by line")
    line1 = f.readline()
    line2 = f.readline()
    print("Line 1:", line1.strip())
    print("Line 2:", line2.strip())

# Step 4: Reading all lines into a list
with open("myfile.txt", "r") as f:
    lines = f.readlines()
print("\nStep4: Reading all lines into a list")
print(lines)

#Step 5: Appending to a file
with open("myfile.txt", "a") as f:
    f.write("This is an extra line added later.\n")
print("\n Step 5: Appended a new line!")

# step 6: Reading again after append
with open("myfile.txt", "r") as f:
    content = f.read()
print("\nStep 6: File content after append: ")
print(content)

# Step 7: using r+ read and write together
with open("myfile.txt", "r+") as f:
    old_content = f.read()
    f.write("\n This new content is added after the r+ mode.")
print("\nStep 7: used r+ mode ( read + write ).")

# Final check show everything in file
with open("myfile.txt", "r") as f:
    final_content = f.read()
print("\nFinal File Content: ")
print(final_content)



