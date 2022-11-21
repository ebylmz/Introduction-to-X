// data flox modeling
module comparator(input [3:0] A, B, output equals, larger, smaller);
	wire[3:0] eq; 
	// compare each bit one by one
	assign eq[3] = A[3] ~^ B[3];
	assign eq[2] = A[2] ~^ B[2];
	assign eq[1] = A[1] ~^ B[1];
	assign eq[0] = A[0] ~^ B[0];
	assign equals = &eq;
	
	wire[3:0] comp;
	assign comp[3] = A[3] & ~B[3];
	assign comp[2] = eq[3] & A[2] & ~B[2];
	assign comp[1] = eq[3] & eq[2] & A[1] & ~B[1];
	assign comp[0] = eq[3] & eq[2] & eq[1] & A[0] & ~B[0];
	assign larger = |comp;
	assign smaller = ~(larger | equals);
endmodule


// Gate Level Modeling
// module comparator(input[3:0] A, B, output larger, smaller, equals);
// 	wire[3:0] eq;
// 	xnor (eq[3], A[3], B[3]);
// 	xnor (eq[2], A[2], B[2]);
// 	xnor (eq[1], A[1], B[1]);
// 	xnor (eq[0], A[0], B[0]);
// 	and result0(equals, eq[0], eq[1], eq[2], eq[3]);
	
// 	wire[3:0] notB;
// 	not(notB[3], B3);
// 	not(notB[2], B2);
// 	not(notB[1], B1);
// 	not(notB[0], B0);
	
// 	wire[3:0] comp;
// 	and (comp[3], A[3], notB[3]);
// 	and (comp[2], eq[3], A[2], notB[2]);
// 	and (comp[1], eq[3], eq[2], A[1], notB[1]);
// 	and (comp[0], eq[3], eq[2], eq[1], A[0], notB[0]);

// 	or result1(larger, comp[3], comp[2], comp[1], comp[0]);
// 	nor result2(smaller, larger, equals);
// endmodule

