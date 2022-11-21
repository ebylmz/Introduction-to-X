// D-Latch
module latch(input clk, input[3:0] d, output reg[3:0] q);
    // Input d can be change during high state of clock. Since the clk 
    // remains same, the change of d cannot affect the output
    // So keep also d in sensivity list 
    always @ (clk, d)
        if (clk)
            q <= d;
endmodule