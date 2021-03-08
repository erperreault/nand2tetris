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

// Put your code here.

(CHECK)
@SCREEN	// reset addr
D=A
@addr
M=D
@KBD	// check keyboard
D=M
@EMPTY
D;JEQ
@FILL
D;JNE

(EMPTY)
@fill	// we'll fill with 000000...
M=0
@RUN
0;JMP

(FILL)
@fill	// we'll fill with 111111...
M=-1

(RUN)
@fill	// Get fill value
D=M
@addr	// Fill register
A=M
M=D
@addr	// Increment addr
M=M+1
D=M
@KBD	// Loop while addr < KBD
D=A-D
@RUN
D;JNE
@CHECK	// Start over if addr == KBD
0;JMP
