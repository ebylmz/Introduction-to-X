// 5 bit binary adder
// it can be used to build a 10 bit adder since it also takes Cin value
module adder(input [4:0] A, input [4:0] B, input Cin, output [4:0] Sum, output Cout);
	wire [3:0] c; // carry out
	fullAdder FA0(.A(A[0]), .B(B[0]), .Cin(Cin), .Sum(Sum[0]), .Cout(c[0]));
	fullAdder FA1(.A(A[1]), .B(B[1]), .Cin(c[0]), .Sum(Sum[1]), .Cout(c[1]));
	fullAdder FA2(.A(A[2]), .B(B[2]), .Cin(c[1]), .Sum(Sum[2]), .Cout(c[2]));
	fullAdder FA3(.A(A[3]), .B(B[3]), .Cin(c[2]), .Sum(Sum[3]), .Cout(c[3]));
	fullAdder FA4(.A(A[4]), .B(B[4]), .Cin(c[3]), .Sum(Sum[4]), .Cout(Cout));
endmodule


module fullAdder(input A, B, Cin, output Sum, Cout);
	wire sumFirst;
	wire[2:0] c;
	halfAdder HA0(.A(A), .B(B), .Sum(sumFirst), .Carry(c[0]));
	halfAdder HA1(.A(sumFirst), .B(Cin), .Sum(Sum), .Carry(c[1]));
	or or1(Cout, c[0], c[1]);
endmodule 


module halfAdder(input A, B, output Sum, Carry);
	xor g1(Sum, A, B);
	// if A and B both are 1 then Sum becames 0, Cary becames 1
	and g2(Carry, A, B);

endmodule 