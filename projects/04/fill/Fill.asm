// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

@SCREEN
D=A
@addr
M=D // addr = base addr of screen

@24575
D=A
@max_screen
M=D

@color
M=0

(CHECKKEY)
    @KBD
    D=M

    @WHITE
    D; JEQ

    @BLACK
    0; JMP

(BLACK)
    @color
    M=-1

    @FLIP
    0; JMP

(WHITE)
    @color
    M=0

    @FLIP
    0; JMP

(FLIP)
    @SCREEN
    D=A
    @screen
    M=D // addr = base addr of screen

    (FLIP_ROW)
        @color
        D=M

        @screen
        A=M
        M=D

        @screen
        M=M+1
        D=M

        @max_screen
        D=M-D

        @FLIP_ROW
        D; JGE
    
    @CHECKKEY
    0; JMP

(END)
    @END
    0; JMP