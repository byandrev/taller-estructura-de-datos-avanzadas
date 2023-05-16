from subprocess import check_output
from datetime import datetime
from os import path, getcwd

from file_manager import write_file


def get_command(language, file, is_windows):
    ans = ""

    if (language == "cpp"):
        if is_windows:
            ans = ".\D.exe"
        else:
            ans = "./D"
    elif (language == "python"):
        ans = f"python {file}"
    elif (language == "java"):
        ans = f"java D"
    elif (language == "php"):
        ans = f"php D"
    elif (language == "javascript"):
        ans = f"node D.js"

    return ans

"""
    arguments:
        languaje: options-> java, cpp, python
        filename: name file
        input: name file txt
        is_windows: True or False
"""
def execute(language, filename, input, is_windows=False):
    if (language=="cpp"):
        check_output(f"c++ ./problems/{filename} -o ./dist/{filename}", shell=True)

    name_file = ""

    if language=="cpp":
        if is_windows:
            name_file = ".\problems\{filename}.exe"
        else:
            name_file = "./problems/{filename}"
    elif language=="java":
        name_file = f"java ./problems/{filename}.java"
    else:
        name_file = f"python {getcwd()}/problems/{filename}.py"

    comando = f"{name_file} < {getcwd()}/dist/{input}.txt"
    out = check_output(comando, shell=True)
    ans = out.decode("ascii").split("\n")
    content = ""

    for l in ans:
        if (len(l) > 0):
            content += l.replace(" ", "").replace("'null'", "null") + "\n"

    write_file(f"{getcwd()}/dist/{filename}_out", content)