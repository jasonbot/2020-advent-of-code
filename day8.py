def build_instructions():
    for item in open('day8.input'):
        instruction, num = item.split()
        num = int(num)
        yield instruction, num


def all_permutations(instructions):
    for index, (instruction, acc) in enumerate(instructions):
        if instruction in ('jmp', 'nop'):
            yield (index, instructions[:index] + [('jmp' if instruction == 'nop' else 'nop', acc)] + instructions[index+1:])


def execute(instructions, start_pos=0):
    acc = 0
    visited_instructions = {len(instructions)}
    traversal = []
    while start_pos not in visited_instructions:
        instruction, acc_num = instructions[start_pos]
        visited_instructions.add(start_pos)
        traversal.append(start_pos)
        if instruction == 'nop':
            start_pos += 1
        elif instruction == 'acc':
            acc += acc_num
            start_pos += 1
        elif instruction == 'jmp':
            start_pos += acc_num
        else:
            raise ValueError(f"WHAT? {start_pos} {instruction}, {acc_num}")

    return (start_pos == len(instructions), acc)


instructions = [item for item in build_instructions()]


print(execute(instructions))
print('---')
for index, edit in all_permutations(instructions):
    finished, acc = execute(edit)
    if finished:
        print(finished, acc)
