from time import time

def readline(input):
    return input.readline().strip()

def one_int(input):
    return int(input.readline().strip())

def two_int(input):
    left, right = map(int, input.readline().strip().split())
    return left, right

def array_int(input):
    return list(map(int, input.readline().strip().split()))

def process_command(command, commands):
    if command == "LEFT":
        return int(-1)
    elif command == "RIGHT":
        return int(+1)
    else:
        com_line = command.split()
        #print(f"com_line = {com_line}")

        sub_position = int(com_line[2])
        sub_command = ' '.join(com_line[0:2]) 

#        print(f"sub_command = {sub_command}")
#        print(f"sub_position = {sub_position}")
#        print(f"commands[sub_position-1] = {commands[sub_position-1]}")

        return process_command(commands[sub_position-1], commands)
 
if __name__ == '__main__':
    start = time()
    with open('input.txt', 'rt') as input:
        with open('output.txt', 'wt') as output:
            num_cases = int(input.readline().strip())
            for _ in range(num_cases):
                num_steps = int(input.readline().strip())
                position = 0
                commands = []
                for step in range(num_steps):
                    command = input.readline().strip()
                    commands.append(command)
#                    print(command)
                    position += process_command(command,commands)
#                    print(f"p={position}")
#                print(f"position final = {position}")
                print(position)

    diff = (time() - start) * 1000
    print("time: {} ms".format(diff))

exit(0)
