module example3(
	input CLOCK_50,
	input[3:0] KEY,
	input RESET_N,
	output[9:0] LEDR,
	input[9:0] SW
);

	// Datapath Design
	
	// set a proper frequency clock signal
	wire[31:0] count;
	wire clk = count[25];
	counter(CLOCK_50, count);

	// multiplexer inputs
	wire d0, d1, d2;

	register(clk, ~KEY[0], LEDR[4:0], d0);
	
	adder(SW[9:5], d0, d1);
	
	shiftReg(clk, SW[2], SW[9:5], d2);
	
	// mux m(d0, d1, d2, SW[9:5], SW[1], SW[0], LEDR[4:0]);
	mux m(d0, d1, d2, SW[9:5], SW[1], SW[0], LEDR[4:0]);
endmodule


// Datapath Component Declerations

// 4x1 multiplexer
module mux(input[4:0] d0, d1, d2, d3, input s1, s0, output[4:0] q);
	assign q = s1 ? (s0 ? d3 : d2) : (s0 ? d1 : d0);
endmodule

// 4x1 multiplexer with always block
// module mux(input[4:0] d0, d1, d2, d3, input[1:0] s, output reg[4:0] q);
// 	always @ (*)
// 		case(s)
// 			2'b00: q <= d0;
// 			2'b01: q <= d1;
// 			2'b10: q <= d2;
// 			2'b11: q <= d3;
// 		endcase
// endmodule

 
// parallel load register
module register(input clk, load, input[4:0] d, output reg[4:0] q);
	always @ (posedge clk)
		q <= load ? d : q;
endmodule


// 5 bit adder
module adder(input[4:0] a, b, output c);
	assign c = a + b;
endmodule

// shift register
module shiftReg(input clk, shift_r, input[4:0] d, output reg[4:0] q);
		always @ (posedge clk)
			q <= (shift_r) ? d >> 1 : d << 1;
endmodule

// comparator
module comparator(input[4:0] a, b, output a_lt_b, a_gt_b, a_eq_b);
	assign a_lt_b = a < b;
	assign a_gt_b = a > b;
	assign a_eq_b = a == b;
endmodule

// counter or timer
module counter(input clk, output reg[31:0] count);
	always @ (posedge clk)
		count <= count + 32'b1; // increment by 1
endmodule