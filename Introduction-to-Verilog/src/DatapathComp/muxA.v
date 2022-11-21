// Multiplexer implmentation with always block
module muxA(input a, b, sel, output reg result);
    always @ (a, b, sel)
        result <= sel ? a : b; 
endmodule