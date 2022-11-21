module example4 (
	input CLOCK_50,
	input[3:0] KEY,
	input RESET_N,
	output[9:0] LEDR
);

	wire[31:0] count;
	counter(CLOCK_50, count);
	
	// The buttons on DEO board are ON, when it doesn't pressed
	// That's because, use ~KEY[]
	
	// count[25] as clock signal with frequency of 0.7 second
	// use LED[1:0] to display the value of number
	// use LED[9] to display odd number result
	controller(count[25], ~KEY[0], LEDR[1:0], LEDR[9]);
endmodule

 
module controller(input clk, b, output[1:0] number, output odd);
	// controller consist of state register and combinational circuit
	reg[1:0] s;  // current state
	wire[1:0] n; // next state
	
	// state register
	// in each clock cycle state changes
	always @ (posedge clk)
		s <= n; 
	
	// combinational circuit
	assign n[1] = (~s[1] & s[0] & b) + (s[1] & ~s[0]) + (s[1] & s[0] & ~b);
	assign n[0] = s[0] ^ b;
	assign number = s;
	assign odd = s[0];
endmodule


module counter(input clk, output reg[31:0] count);
	always @ (posedge clk)
		count <= count + 32'b1;
endmodule