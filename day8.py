def build_instructions():
    for item in open('day8.input'):
        instruction, num = item.split()
        num = int(num)
        yield instruction, num

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
            
    print(set(range(len(instructions))) - set(traversal))
    return acc

instructions = [item for item in build_instructions()]
print(execute(instructions))
