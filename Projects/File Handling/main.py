#file_obj = open("sample.txt", 'w')
#string = """Hi hello
#This is Seeta Susmitha
#Today's Topic is FileHandling"""
#file_obj.write(string)
#file_obj.close()

## opening file in write mode
# file_obj = open("sample.txt", 'w')
# strings_list = ["Welcome to File Handling\n",
#                 "This is write operation\n"]
# file_obj.writelines(strings_list)
# file_obj.close()

## Opening file in read mode
# try:
#     file_obj = open("text.txt", 'w')
#     data = file_obj.read()
#     print(data)
# except Exception as e:
#     print(f"Some thing wrong: {e}")
# finally:
#     file_obj.close()


## opening file using 'with' keyword
try:
    with open('sample.txt', 'r') as file_obj:
        data = file_obj.read()
        print(type(data))
        print(data[:10])
        print(data)
    
except Exception as e:
    print(f"Some thing wrong: {e}")

