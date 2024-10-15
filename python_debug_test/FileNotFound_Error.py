def read_file_content(file_path):
    # Attempt to open the file
    with open(file_path, 'r') as file:
        content = file.read()
        print("File content:")
        print(content)


# Test case with an existing file (this won't cause an error if the file exists)
file_path1 = "existing_file.txt"
read_file_content(file_path1)

# Test case with a non-existent file (this will cause FileNotFoundError)
file_path2 = "non_existent_file.txt"
read_file_content(file_path2)
