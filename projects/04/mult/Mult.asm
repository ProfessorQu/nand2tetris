// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

@R0
D=M
@x
M=D // x = RAM[0]

@R1
D=M
@y
M=D // y = RAM[1]

@sum
M=0

(LOOP)
    @y
    D=M
    @END
    D; JEQ // if y == 0, end

    @x
    D=M
    @sum
    M=M+D // RAM[2] += x

    @y
    M=M-1 // y--

    @LOOP
    0; JMP // Loop

(END)
    @sum
    D=M
    @R2
    M=D // RAM[2] = sum

    @END
    0; JMP