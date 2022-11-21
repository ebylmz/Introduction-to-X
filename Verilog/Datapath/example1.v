module example1 (
	input CLOCK_50, 
	input[3:0] KEY, 
	input RESET_N, 
	output[9:0] LEDR,	
	input[9:0] SW
);
	// button get reverse of KEY[0], since KEY is at high state initially
	wire b = ~KEY[0];
	// The frequency of CLOCK_50 is 50 MHz. 
	// Any change on leds cannot be detected by human eyes. 
	// So to observe the outputs use counter and select a bit
	// which becomes high in x number of rising edges of the clock signal.
	// For exp (1 / 50,000,000) * 2^n gives the frequency of n. bit
	wire[31:0] cnt;
	counter c0(.clk(CLOCK_50), .count(cnt));

	// KEY[0]: button to activate the controller
	// cnt[25]: becomes high in each 0.7 sec and used as a clock signal
	// LEDR[0]: to display the controller output
	// LEDR[9:8]: to display the current state of controller 
	controller(b, cnt[25], LEDR[0], LEDR[9:8]);
endmodule

// logic: if the button (b) pressed, then
// becomes high for 3 clock cycle and then returns low.
module controller(input b, clk, output x, output[1:0] sOut);
	// controller consist of two part
	// 1. state register
	// 2. combinational circuit

	reg[1:0] s; // current state
	wire[1:0] n; // next state
	
	// state register
	always @ (posedge clk)
		s <= n;
		
	// combinational circuit
	// these are founded in state table
	assign n[0] = (~s[1] & ~s[0] & b) | (s[1] & ~s[0]);
 	assign n[1] = s[1] ^ s[0];
	assign x = s[1] | s[0];
	
	// output: current state
	assign sOut = s;
endmodule


module counter(input reset, en, clk, output reg[31:0] count);
	always @ (posedge clk or negedge reset)
		if (!reset)
			count <= 32'b0;
		else // increment or preserve the value
			count <= en ? count + 32'b1 : count;
endmodule