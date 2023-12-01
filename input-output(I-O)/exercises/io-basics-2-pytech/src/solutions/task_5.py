"""Manipulating file contents"""

with open('../data/todos.txt', 'r') as source:
    content = source.read()  # read content from todos file
    
    with open('../data/todos.secret', 'w') as target:
        
        for char in content:
            code = ord(char)
            target.write(f"{code}\n")
            
with open('../data/todos.secret', 'r') as todos:
    # initialize an empty string
    text = ""
    
    for code in todos:
        text += chr(int(code))
    print(text)    
