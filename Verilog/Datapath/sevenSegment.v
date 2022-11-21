module sevenSegment(input [3:0] data, output reg[6:0] segments);
	always @ (*) // if there is a change in any signal
		case (data)
			0: segments = 7'b111_1110;
			1: segments = 7'b011_0000;
			2: segments = 7'b110_1101;
			3: segments = 7'b111_1001;
			4: segments = 7'b011_0011;
			5: segments = 7'b101_1011;
			6: segments = 7'b001_1111;
			7: segments = 7'b111_0000;
			8: segments = 7'b111_1111;
			9: segments = 7'b111_0011;
			// for cases 10 . . . 15
			default: segments = 7'b000_0000;
		endcase
endmodule