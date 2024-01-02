"""Changing contents of a text file."""

changes = [
    {
        "name": "todos.txt",
        "change": ("Call mom", "Clean up house")
    },
    {
        "name": "bookmarks.txt",
        "change": ("https://google.com", "https://www.w3resource.com")
    }
]

for file in changes:
    old_line = file['change'][0]
    new_line = file['change'][1]
    
    with open(f"../data/{file['name']}", 'r+') as target_file:
        content = target_file.read()  # read the contents of the file
        start = content.index(old_line)  # find starting index of old text
        end = start + len(old_line)  # find the ending index of old text
        suffix = content[end:]  # Move the file position to end of line
        target_file.seek(start)  # Move the file position to the start index of the old text
        target_file.write(new_line + suffix)  # overwrite the text
