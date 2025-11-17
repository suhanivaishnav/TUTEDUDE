# Task 2: Write and Append Data to a File

# Step 1: Write data to output.txt
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

# Step 2: Append more data
with open("output.txt", "a") as file:
    file.write("This is appended text.\n")

# Step 3: Read and display final content
print("\nFinal content of output.txt:\n")

with open("output.txt", "r") as file:
    print(file.read())
