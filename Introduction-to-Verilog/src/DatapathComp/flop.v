// ‘assign’ statement is not used within always block
// assigned variables need to be declared as reg

// D Flip-Flop
module flop(input clk, input[3:0] d, output reg[3:0] q);
    // posedge defines a rising edge (transition from 0 to 1)  
    // once the clk signal rises: the value of d will be copied to q
    always @(posedge clk)
        q <= d; // q gets d
        // What happens when clock is not rising?
        // q <= q; (The value of q preserved (hidden latch occurs))
endmodule