from Print import print_tree
from Tree import deserialize
from file_manager import write_file


def read_input():
    file_input = open("./dist/input_problem1.txt", "r")
    file_output = open("./dist/1_out.txt", "r")
    inputs_splited = file_input.read().split("\n")
    outputs_splited = file_output.read().split("\n")

    inputs_splited = inputs_splited[1:len(inputs_splited)-1]
    outputs_splited = outputs_splited[0:len(outputs_splited)-1]

    content = ""
    index = 0
    index_val = 1
    for i in range(len(outputs_splited)):
        content += f"\nTest #{i+1}\n Input Tree: Insert val: {inputs_splited[index_val]}"
        content += "\n"+print_tree(deserialize(inputs_splited[index]))
        content += "\nOut tree:\n"
        content += print_tree(deserialize(outputs_splited[i]))
        content += "\n-----------------"
        index+=2
        index_val+=2

    write_file("print_problem_1", content)


read_input()