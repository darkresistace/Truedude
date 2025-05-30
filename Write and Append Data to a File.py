def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data written to the file.")

def append_to_file(filename):
    additional_input = input("Enter additional text to append to the file: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print("Data appended to the file.")

def read_file(filename):
    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# File name to use
file_name = 'output.txt'

# Perform tasks
write_to_file(file_name)
append_to_file(file_name)
read_file(file_name)
