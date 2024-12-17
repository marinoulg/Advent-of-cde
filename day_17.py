import pandas as pd
import numpy as np


def combo_operand(num, A=None, B=None, C=None):
    if num in range(0,4):
        return num
    elif num == 4:
        return A
    elif num == 5:
        return B
    elif num == 6:
        return C
    else:
        return f'invalid combo operand - {num}'


def to_binary(num_a, num_b):
    num_a = int(num_a)
    num_b = int(num_b)

    if num_a > num_b:
        bin_a = f'{num_a:0b}'
        my_int = int(len(bin_a))
        bin_b = f'{num_b:{my_int}b}'
        bin_b = bin_b.replace(' ', '0')
        return bin_a, bin_b
    elif num_b > num_a:
        bin_b = f'{num_b:0b}'
        my_int = int(len(bin_b))
        bin_a = f'{num_a:{my_int}b}'
        bin_a = bin_a.replace(' ', '0')
        return bin_a, bin_b
    else:
        bin_a = f'{num_a:0b}'
        bin_b = f'{num_b:0b}'
        return bin_a, bin_b

def bitwise_XOR(a, b):
    num_a, num_b = to_binary(a,b)

    temp_a = []
    for i in range(len(str(num_a))):
        temp_a.append((str(num_a)[i]))

    temp_b = []
    for i in range(len(str(num_b))):
        temp_b.append((str(num_b)[i]))

    new = np.array(temp_a) == np.array(temp_b)

    c = []
    for i in new:
        if i == False:
            c.append(1)
        else:
            c.append(0)

    new_str = str()
    for i in c:
        if isinstance(i, int):
            new_str += str(i)

    return int(new_str, 2)


def instructions(instr, operand, A=None, B=None, C=None):
    opcodes = {
        0: 'adv', # A
        1: 'bxl', # B
        2: 'bst', # B
        3: 'jnz', # any
        4: 'bxc', # B
        5: 'out', # outputs
        6: 'bdv', # B
        7: 'cdv' # C
    }
    outputs = str()

    if instr == 0:
        # ---> division
        # numerator: value in the A register
        # denominator: raising 2 to the power of the instruction's combo operand
        nb = combo_operand(operand, A, B, C)
        res = A / (2**nb)

        # Examples :
        # an operand of 2 would divide A by 4 (2^2);
        # an operand of 5 would divide A by 2^B.)

        # The result of the division operation is truncated to an integer
        res = int(res)

        # and then written to the A register
        A = res

        return A, B, C, outputs


    elif instr == 1:
        # calculates the bitwise XOR of register B and the instruction's literal operand,
        B = bitwise_XOR(B, operand)
        # then stores the result in register B
        return A, B, C, outputs

    elif instr == 2:
        # calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits),
        num = combo_operand(operand, A, B, C)
        num = num%8

        # then writes that value to the B register
        B = num

        return A, B, C, outputs

    elif instr == 3:
        if A == 0:
            # does nothing if the A register is 0
            # print('the end')
            pass
        else:
            # if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
            # instr == operand
            return instructions(operand, operand, A, B, C)

            # if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.


    elif instr == 4:
        # calculates the bitwise XOR of register B and register C,
        B = bitwise_XOR(B, C)
        # then stores the result in register B.
        return A, B, C, outputs

    elif instr == 5:
        # calculates the value of its combo operand modulo 8, then outputs that value.
        num = combo_operand(operand, A, B, C)
        num = num%8
        outputs += str(num)

        # (If a program outputs multiple values, they are separated by commas.)

        return A, B, C, outputs

    elif instr == 6:
        # ---> division
        # numerator: value in the A register
        # denominator: raising 2 to the power of the instruction's combo operand
        num = combo_operand(operand, A, B, C)
        res = A / (2**num)

        # Examples :
        # an operand of 2 would divide A by 4 (2^2);
        # an operand of 5 would divide A by 2^B.)

        # The result of the division operation is truncated to an integer and then written to the B register
        res = int(res)
        B = res

        return A, B, C, outputs

    elif instr == 7:
            # ---> division
            # numerator: value in the A register
            # denominator: raising 2 to the power of the instruction's combo operand
            num = combo_operand(operand, A, B, C)
            res = A / (2**num)

            # Examples :
            # an operand of 2 would divide A by 4 (2^2);
            # an operand of 5 would divide A by 2^B.)

            # The result of the division operation is truncated to an integer and then written to the C register
            C = res

            return A, B, C, outputs

def get_final_list(A,B,C,program):
    pointers = []
    operands = []
    outs = []

    for i in range(len(program)):
        if i%2 == 0:
            pointers.append(program[i])
        else:
            operands.append(program[i])

    try :
        while isinstance(A, int):
            for j in range(len(pointers)):
                A,B,C,outputs = instructions(pointers[j], operands[j], A, B, C)
                if outputs:
                    outs.append(outputs)
    except TypeError:
        pass

    return outs



def final_result(outputs):
    return (",".join(map(str, outputs)))

def part_2(program, min=0, max=1000000, B=0, C=0):
    str_progr = str(program).replace('[', '').replace(']', '').replace(' ', '')

    for i in range(min, max):
        result = get_final_list(1+i, B, C, program)
        if (final_result(result)) != str_progr:
            print('❓ i=',i)
            next
        else:
            print(1+i)
            break

if __name__ == '__main__':
    part_2(program=[2,4,1,7,7,5,1,7,0,3,4,1,5,5,3,0], min=21485939, max=100000000)
