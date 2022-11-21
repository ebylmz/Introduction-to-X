module equals(input [3:0] A, input [3:0] B, output eq);
	wire[3:0] compare;
	// structural description
	
	// compare each bit one by one
	xnor c0(compare[0], A[0], B[0]);
	xnor c1(compare[1], A[1], B[1]);
	xnor c2(compare[2], A[2], B[2]);
	xnor c3(compare[3], A[3], B[3]);
	// for equality all the comparions become 1
	and result(eq, compare[0], compare[1], compare[2], compare[3]);

	// data-flow description
	// wire[3:0] c; 
	// assign c = ~(A ^ B); // XNOR
	// assign eq = &c;	// and all the bits of bus c
	
	// really short solution
	// assign eq = (A == B) ? 1 : 0; 
endmodule