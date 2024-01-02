"""Creating files from a list"""

files = [
    {
        "name": "todos.txt",
        "content": ["My ToDos:", "", "Go shopping", "Finish module"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["My links:", "", "https://google.com", "https://digitalcareerinstitute.org"]
    }
]

for file in files:
    with open(f"../data/{file['name']}", 'x') as target_file:
        # file_content = '\n'.join(file["content"])
        file_content = [f"{line}\n" for line in file['content']]
        target_file.writelines(file_content)
