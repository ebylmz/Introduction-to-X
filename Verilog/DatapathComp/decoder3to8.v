module decoder3to8(input[2:0] I, input E, output[7:0] Y);
	// data flow model
	// assign Y[0] = E & ~I[2] & ~I[1] & ~I[0];
	// assign Y[1] = E & ~I[2] & ~I[1] & I[0];
	// assign Y[2] = E & ~I[2] & I[1] & ~I[0];
	// assign Y[3] = E & ~I[2] & I[1] & I[0];
	// assign Y[4] = E & I[2] & ~I[1] & ~I[0];
	// assign Y[5] = E & I[2] & ~I[1] & I[0];
	// assign Y[6] = E & I[2] & I[1] & ~I[0];
	// assign Y[7] = E & I[2] & I[1] & I[0];
	
	// gate level model
	// E is not used !!!
	decoder2to4 d1(.E(~I[2]), .I(I[1:0]), .Y(Y[3:0]));
	decoder2to4 d2(.E(I[2]), .I(I[1:0]), .Y(Y[7:4]));
endmodule

module decoder2to4(input[1:0] I, input E, output[3:0] Y);
	// data flow model
	// assign Y[0] = E & ~I[1] & ~I[0];
	// assign Y[1] = E & ~I[1] & I[0];
	// assign Y[2] = E & I[1] & ~I[0];
	// assign Y[3] = E & I[1] & I[0];
	
	// gate level model
	wire[1:0] notI;
	not n0(notI[0], I[0]);
	not n1(notI[1], I[1]);
	
	and a0(Y[0], notI[1], notI[0], E);
	and a1(Y[1], notI[1], I[0], E);
	and a2(Y[2], I[1], notI[0], E);
	and a3(Y[3], I[1], I[0], E);
	
endmodule