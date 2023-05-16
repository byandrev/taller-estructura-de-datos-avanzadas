def write_file(filename, content):
    f = open(f"{filename}.txt", "a")
    f.write(content)
    f.close()
