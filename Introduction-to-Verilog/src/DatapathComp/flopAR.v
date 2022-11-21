// D Flip-Flop with Asynchronous Reset
module flopAR(input clk, input reset, input[3:0] d, output reg[3:0] q);
// in this example: two events can trigger the process:
// a rising edge on clk or a falling edge on reset
    always @ (posedge clk, negedge reset) begin
        // if reset becomes low from high state (negedge)
        if (reset == 0) // independent from clock (asynchoronous)  
            q <= 0;
        else
            q <= d;
    end
endmodule

// Why is reset triggered at negative edge?
// In case of any disconnection on circuit, 
// it's easy to send low pulse rather than high pulse.

// D Flip-Flop with Synchronous Reset
module flopSR(input clk, input reset, input[3:0] d, output reg[3:0] q);
    // reset only happens when the clock rises (synchronous)
    always @ (posedge clk)
        q <= (reset == 0) ? 0 : d;
endmodule


