module example2 (
	input CLOCK_50, 
	input[3:0] KEY, 
	input RESET_N, 
	output[9:0] LEDR,	
	input[9:0] SW
);
	// counter or timer
	reg[31:0] count;
	
	always @ (posedge CLOCK_50)
		count <= count + 32'b1;
		
	// state register
	reg[1:0] s; // current state
	
	always @ (count[25])
		s <= n;
		
	// combinational logic 
	wire[1:0] n; // next state
	wire[3:0] x, y, z, w;
	
	// derived from state table
	assign n[0] = ~s[0];
	assign n[1] = s[0] ^ s[1];
	assign x = s[1];
	assign y = s[1] & ~s[0];
	assign z = ~s[1] & s[0];
	assign w = ~s[1];
	
	// concatenate and assign the outputs x, y, z, w 
	assign LEDR[3:0] = {x, y, z, w}; 
	// assign the current state
    assign LEDR[9:8] = s; 
	
endmodule
