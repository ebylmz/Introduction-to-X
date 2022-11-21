module example5 (
	input CLOCK_50,
	input[9:0] KEY,
	input RESET_N,
	output[9:0] LEDR
);

	wire[31:0] count;
	counter(CLOCK_50, count);
	
	controller(count, ~KEY[0], ~KEY[1], LEDR[1:0], LEDR[9]);
endmodule


module controller(input clk, i, d, output[1:0] number, output odd);
	reg[1:0] s;  // current state
	wire[1:0] n; // next state 

	// state register
	always @ (posedge clk)
		s <= n;
		
	// combinational controller
	assign n[1] = 
		(~s[1] & ~s[0] & ~i & d) +
		(~s[1] & s[0] & i & ~d) +
		(s[1] & ~s[0] & ((~i & ~d) + i)) +
		(s[1] & s[0] & ((i & d) + ~i));
	
	assign n[0] = 
		(~s[1] & ~s[0] & (i ^ d)) +
		(~s[1] & s[0] & (i ~^ d)) +
		(s[1] & ~s[0] & (i ^ d)) +
		(s[1] & s[0] & (i ~^ d));
		
			
	// assign n[0] = ~s[0] & (i ^ d);
	// assign n[1] = ((~i & d) & ~(s[1] ^ s[0])) | ((s[1] ^ s[0]) & (i & ~d));
	
	assign odd = s[0];
	assign number = s;
endmodule

module counter(input clk, output reg[31:0] count);
	always @ (posedge clk)
		count <= count + 32'b1;
endmodule