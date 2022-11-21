// Converts either of the two binary digits or signals into the other

// This is a combinational circuit (no clock, no memorizing the value) 
// If the statements define the signals completely, 
// nothing is memorized, block becomes combinational.

module inverter(input inv,  input[3:0] data, output reg[3:0] result);
    // when inv is 1, result is ~data
    always @ (inv, data) 
        result <= inv ? ~data : data;
endmodule