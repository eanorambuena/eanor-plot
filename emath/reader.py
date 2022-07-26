def read(file_name):

    with open(file_name, "r") as file:
        content = file.read()
    
    lines = content.split("\n")

    for line in lines:
        l = line.strip()
        print(l)
