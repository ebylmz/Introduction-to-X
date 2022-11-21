module aboveMirrorDisplay(
	input CLOCK_50,
	input[3:0] KEY,
	input RESET_N,
	output[9:0] LEDR,
	input[9:0] SW
);

	wire[7:0] d; // 8-bit data
	wire[3:0] ld; // load for registers
	wire[7:0] q[3:0]; // output of registers

	// decoder to send the data to specific register
	decoder(SW[0], SW[1], SW[2], ld);

	// register declerations
	loadReg r0(CLOCK_50, ld[0], d, q[0]);
	loadReg r1(CLOCK_50, ld[1], d, q[1]);
	loadReg r2(CLOCK_50, ld[2], d, q[2]);
	loadReg r3(CLOCK_50, ld[3], d, q[3]);

	// multiplexer to get the output from specific register
	mux(q[0], q[1], q[2], q[3], SW[1], SW[2], LEDR[7:0]);

endmodule


// 2x4 decoder (Dataflow modeling)
module decoder(input e, s1, s0, output[3:0] d);
	assign d[0] = e & ~s1 & ~s0;
	assign d[1] = e & ~s1 & s0;
	assign d[2] = e & s1 & ~s0;
	assign d[3] = e & s1 & s0;
endmodule

// // 2x4 decoder (Behavioral modeling) 
// module decoder(input s1, s0, e, output reg d0, d1, d2, d3);
// 	always @ (e, s1, s0) begin
// 		d0 <= e & ~s1 & ~s0;
// 		d1 <= e & ~s1 & s0;
// 		d2 <= e & s1 & ~s0;
// 		d3 <= e & s1 & s0;
// 	end
// endmodule

// 4x1 8-bit multiplexer
module mux(input[7:0] d0, d1, d2, d3, input s1, s0, output[7:0] q);
	assign q = s1 ? (s0 ? d3 : d2) : (s0 ? d1 : d0);
endmodule

// 8-bit load register
module loadReg(input clk, load, input[7:0] d, output reg[7:0] q);
	always @ (posedge clk)
		q <= load ? d : q;
endmodule