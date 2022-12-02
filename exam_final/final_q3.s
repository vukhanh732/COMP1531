# read an integer
# print 1 iff  the least significant bit is equal to the most significant bit
# print 0 otherwise

main:
    li   $v0, 5
    syscall

    # THESE LINES JUST PRINT 42
    # REPLACE THE LINES BELOW WITH YOUR CODE
    move $t0, $v0
    andi $t1, $t0, 0xFF
    srl  $t2, $t1, 8
    andi $t2, $t2, 0xFF

    beq $t1, $t2, print_one
    #bne $t1, $t2, print_zero

    li $a0, 0
    j print
    # REPLACE THE LINES ABOVE WITH YOUR CODE

print_one:
    li $a0, 1

#print_zero:
    #li $a0, 0
print:
    li $v0, 1
    syscall

    li $a0, '\n'
    li $v0, 11
    syscall

end:
    li $v0, 0
    jr $31
