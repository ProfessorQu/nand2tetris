import sys
from tables import comp_table, dest_table, jmp_table, symbol_table


variable_cursor = 16
root = sys.argv[1]

def format_line(line: str) -> str:
    # Strip whitespace
    line = line.strip()

    # Remove comment-only lines and empty lines
    if line.startswith('//'):
        return ''
    if not line:
        return ''

    # Remove comments
    line = line.split('//')[0]

    return line

def translateAinstruction(line: str) -> str:
    global variable_cursor

    if line.isdigit():
        return f'0{bin(int(line))[2:].zfill(15)}'
    if line not in symbol_table:
        symbol_table[line] = variable_cursor
        variable_cursor += 1

    return f'0{bin(symbol_table[line])[2:].zfill(15)}'

def translateCinstruction(line: str) -> str:
    dest, jmp = '', ''

    if "=" in line:
        dest, comp = line.split('=')
        dest = dest.strip()
        comp = comp.strip()
        
    if ";" in line:
        comp, jmp = line.split(';')
        comp = comp.strip()
        jmp = jmp.strip()
    
    a = '0'
    if 'M' in comp:
        comp = comp.replace('M', 'A')
        a = '1'

    return f'111{a}{comp_table[comp]}{dest_table[dest]}{jmp_table[jmp]}'

def translate(line: str) -> str:
    line = format_line(line)

    if line.startswith('@'):
        return translateAinstruction(line[1:])
    else:
        return translateCinstruction(line)

def first_pass():
    index = 0

    with open(root, 'r') as f:
        for line in f:
            line = format_line(line)

            if line != '':
                if line.startswith('('):
                    symbol_table[line[1:-1]] = index
                else:
                    index += 1

def assemble():
    hackfilename = root.replace('.asm', '.hack')

    with open(root, 'r') as asmfile, open(hackfilename, 'w') as hackfile:
        for line in asmfile:
            line = format_line(line)

            if line != '' and not line.startswith('('):
                hackfile.write(translate(line) + '\n')

def main():
    first_pass()
    assemble()

if __name__ == '__main__':
    main()