main:
    li $v0, 5
    syscall
    move $t0, $v0

    li $v0, 5
    syscall
    move $t1, $v0


    # THESE LINES JUST PRINT 42
    # REPLACE THE LINES BELOW WITH YOUR CODE
    move $t3, $t0
loop:
    bge $t3, $t1, end_loop
    
    andi $t4, $t3, 0x1
    ble $t4, 0, continue

    andi $t4, $t3, 0x2
    ble $t4, 0, continue

    move $a0, $t3
    li $v0, 1
    syscall

    li $a0, '\n'
    li $v0, 11
    syscall
continue:
    addi $t3, $t3, 1
    j loop
    
end_loop:
    j end
    # REPLACE THE LINES ABOVE WITH YOUR CODE

end:
    li $v0, 0
    jr $31  