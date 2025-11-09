import re

def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("File", file_name, "wasn't opened")
        return None
    else:
        print("File", file_name, "was opened")
        return file

file1_name = "TF2_1.txt"
file2_name = "TF2_2.txt"

file_1_w = Open(file1_name, "w")

if file_1_w != None:
    file_1_w.write("Hello, the password is 123.\n")
    file_1_w.write("I was born on March 24, 2005.\n")
    file_1_w.write("My telephone number is 0995672985.\n")
    print("Information was successfully added to TF2_1.txt")
    file_1_w.close()
    print("File TF2_1.txt was closed")

file_2_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_2_r != None and file_2_w != None:
    text = file_2_r.read()

    numbers = re.findall(r"\d{3,}", text)

    file_2_w.write(" ".join(numbers))

    file_2_r.close()
    file_2_w.close()
    print("Files TF2_1.txt and TF2_2.txt were closed")

print("\nNew sequence:")

file_3_r = Open(file2_name, "r")

if file_3_r is not None:
    text = file_3_r.read()
    words = text.split()
    print(" ".join(words))
    print("File TF2_2.txt was closed")
    file_3_r.close()