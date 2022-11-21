// A simple FSM which has 3 state
module simpleFSM(input clk, reset, output q);
	// Each FSM consists of three separate parts:
	// 1. next state logic
	// 2. state register
	// 3. output logic

	// define current state and next state as 2-bit reg
	reg[1:0] state, nextstate;

	parameter S0 = 2'b00;
	parameter S1 = 2'b01;
	parameter S2 = 2'b10;

	// state register
	always @ (posedge clk, negedge reset)
		// if reset is low, then state becomes initial state S0
		state <= (!reset) ? S0 : nextstate;
		
	// next state logic
	always @ (*)
		case(state)
			S0: nextstate = S1;
			S1: nextstate = S2;
			S2: nextstate = S0;
			default nextstate = S0;
		endcase

	// output logic
	assign q = (state == S0); // output depends only on state (Moore type FSM)
endmodule 