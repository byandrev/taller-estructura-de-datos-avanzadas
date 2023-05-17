import random
from Tree import generate
from file_manager import write_file
from generate_output import execute

def generate_tests():
    content="20\n"
    for i in range(20):
        n = random.randint(1, 100)
        t = generate()
        content+=t+"\n"
    try:
        write_file("./dist/input_problem3", content)
        print("File writed")
    except:
        print("Error to write file")


def generate_outputs():
    execute("cpp", "3", "input_problem3", False)


if __name__ == '__main__':
    generate_tests()
    generate_outputs()