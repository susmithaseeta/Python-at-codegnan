import csv

# try:
#     with open('users.csv', 'w', newline = "") as file:
#         writer = csv.writer(file)
#         writer.writerows([['Id', 'Name', 'Age'],
#                          ['1', "Susmitha", '21'],
#                          ['2' , "Akshya", '22']])

# except Exception as e:
#     print(f"Something Wrong: {e}")


## reading csv content
try:
    with open('users.csv', 'r', newline = "") as file:
        reader = csv.reader(file)
        print(reader)
        for row in reader:
            print(row)
except Exception as e:
    print(f"Something Wrong: {e}")