"""Add new contents to the existing files"""

additions = [
    {
        "name": "todos.txt",
        "content": ["Call mom", "Walk the dog"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["https://python.org", "https://www.djangoproject.com/"]
    }
]

for file in additions:
    with open(f"../data/{file['name']}", 'a') as target_file:
        # file_content = '\n'.join(file["content"]+"\n")
        file_content = [f"{line}\n" for line in file['content']]
        target_file.writelines(file_content)
