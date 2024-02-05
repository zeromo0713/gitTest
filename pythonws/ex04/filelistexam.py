import os

path = r"D:\zeromo\workspace\pythonws\ex03"
file_list = os.listdir(path)


file_list_py = [file for file in file_list if file.endswith(".py")]
print ("file_list_py: {}".format(file_list_py))


# 위 구문과 동일함
file_list_py = []
for f in file_list :
    if f.endswith(".py") :
        file_list_py.append(f)

print ("file_list_py: {}".format(file_list_py))