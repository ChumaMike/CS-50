filename = input("What is the file? ").lower()

dictend = {".gif": "image/gif", ".jpg": "image/jpeg" , ".jpeg": "image/jpeg", 
           ".png": "image/png", ".pdf": "application/pdf", ".txt": "text/plain",
            ".zip": "application/zip"}

for key, value in dictend.items():
    if filename.endswith(key):
        print(value)
