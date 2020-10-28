def arithmetic_arranger(problems, evaluate=None):
    # problems are a string list with basic math problems.
    if len(problems) > 5:
        return "Error: Too many problems."
    arranged_problems = ""
    first_operands = []
    second_operands = []
    dashes_list = []
    results = []

    for i in range(len(problems)):
        underline_string = '-'
        operands_and_operator = problems[i].split(" ")

        if not (operands_and_operator[1] == "+" or operands_and_operator[1] == "-"):
            return "Error: Operator must be '+' or '-'."
        elif (not operands_and_operator[0].isdigit()) or (not operands_and_operator[2].isdigit()):
            return "Error: Numbers must only contain digits."
        elif (len(operands_and_operator[0]) > 4) or (len(operands_and_operator[2]) > 4):
            return "Error: Numbers cannot be more than four digits."

        longest_operand = operands_and_operator[0] if len(operands_and_operator[0]) >= len(operands_and_operator[2]) \
            else operands_and_operator[2]
        if longest_operand == operands_and_operator[0]:
            first_operands.append(f"{operands_and_operator[0].rjust(len(operands_and_operator[0]) + 2)}")
        else:
            first_operands.append(f"{operands_and_operator[0].rjust(len(longest_operand) + 2)}")
        second_operands.append(f"{operands_and_operator[1]}{operands_and_operator[2].rjust(len(longest_operand) + 1)}")
        if evaluate:
            results.append(f"{str(eval(problems[i])).rjust(len(longest_operand) + 2)}")
        underline_string *= (len(longest_operand) + 2)
        dashes_list.append(f"{underline_string}")

    arranged_problems += add_formatted_operands(first_operands, len(problems)) + f"\n"

    arranged_problems += add_formatted_operands(second_operands, len(problems)) + f"\n"

    arranged_problems += add_formatted_operands(dashes_list, len(problems))

    if evaluate:
        arranged_problems += f"\n"
        arranged_problems += add_formatted_operands(results, len(problems))
    return arranged_problems


def add_formatted_operands(operand_list, size):
    formatted_operands = ""
    for i in range(size):
        if i < size - 1:
            formatted_operands += operand_list[i] + "    "
        else:
            formatted_operands += f"{operand_list[i]}"
    return formatted_operands


if __name__ == "__main__":
    print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
