#   read log file in python and check  " python" word is present or not and display the message.

with open("log_file.txt") as f:
    content= f.read()

if "python" in content.lower():
    print("python is present")
else:
    print("python is not present")

    

if "EDC8112I" in content:
    print("EDC8112I is present")
else:
    print("EDC8112I is not present")