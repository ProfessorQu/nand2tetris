import sys


comp_table = {
    '0': '101010',
    '1': '111111',
    '-1': '111010',
    'D': '001100',
    'A': '110000',
    '!D': '001101',
    '!A': '110001',
    '-D': '001111',
    '-A': '110011',
    'D+1': '011111',
    'A+1': '110111',
    'D-1': '001110',
    'A-1': '110010',
    'D+A': '000010',
    'D-A': '010011',
    'A-D': '000111',
    'D&A': '000000',
    'D|A': '010101',
}

jmp_table = {
    '': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

dest_table = {
    '': '000',
    'M': '001',
    'D': '010',
    'MD': '011',
    'A': '100',
    'AM': '101',
    'AD': '110',
    'AMD': '111',
}


def format_line(line: str) -> str:
    line = line.strip()

    if line.startswith('//'):
        return ''
    if line == '':
        return ''

    return line


def parse_line(line: str) -> str:
    binary = '0'

    if line[0] == '@':
        binary = bin(int(line[1:]))[2:]
        binary = binary.zfill(16)

        return binary

    binary = '111'
    dest, jump = '', ''

    if '=' in line:
        dest, comp = line.split('=')
    else:
        comp = line

    if ';' in comp:
        comp, jump = comp.split(';')

    if 'M' in comp:
        binary += '1'

        temp = comp.replace('M', 'A')
        binary += comp_table[temp]
    else:
        binary += '0'

        binary += comp_table[comp]

    binary += dest_table[dest]
    binary += jmp_table[jump]

    return binary

def main():
    lines = ''

    filename = sys.argv[1]
    asmfile = open(filename, 'r')

    for line in asmfile.readlines():
        line = format_line(line)
        if line != '':
            lines += parse_line(line) + '\n'
    
    filename = filename.replace('.asm', '.hack')

    hackfile = open(filename, 'w')
    hackfile.write(lines)

main()