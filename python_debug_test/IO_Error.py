def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        return data

# 尝试在 C 盘根目录写入文件，通常会导致权限问题
file_path = "C:\\output.txt"
write_to_file(file_path, "This is a test content.")

# 读取文件内容（如果之前写入文件失败，这里会抛出 IOError）
file_content = read_from_file(file_path)
print("File content:", file_content)

# 由于权限问题，程序会在文件操作时引发错误
print("End of program.")
