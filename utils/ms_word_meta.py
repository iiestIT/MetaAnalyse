import zipfile

with zipfile.ZipFile("test.docx") as docs:
    print(docs.namelist())
    first = docs.read("word/settings.xml")
    print(first)