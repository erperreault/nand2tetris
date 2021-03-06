// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

@sum	// sum=0
M=0
@i	// i=0
M=0
@diff	// diff=0
M=0	


(LOOP)
@i	// get i
D=M
@R1	// subtract i from y
D=M-D
@RESULT	// goto end if y-i == 0
D;JEQ
@R0	// get x
D=M	
@sum	// add x to sum
M=M+D 
@i	// increment i
M=M+1	
@LOOP	// loop
0;JMP

(RESULT)
@sum	// get final sum
D=M
@R2	// set R2 to final sum
M=D

(END)
@END
0;JMP
