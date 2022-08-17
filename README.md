<img src="https://i.imgur.com/lRzzpEU.png"></img>

# ALSABAH

<div align="center"><h2><br/><br/>
 An assembly-ish thing intended to be a compile target for future versions of ALNOOR<br/><br/>Made by Raiyaxi Ziaoi
</h2></div>
<br>

Keywords: <br/>
PSH: Pushes a value to the stack; "PSH 3"<br/>
ARG: Adds a register with default value '0'; "ARG"<br/>
PLL: Pulls a value from a register and pushes it to the stack; "PLL 0"<br/>
SET: Sets a register to a value from the stack; "SET 0 -1"<br/>
MOV: Copies a value from one register to another and resets the first; "MOV 0 1"<br/>
HLD: Makes a register hold a value specified; "HLD 0 1"<br/>
POP: Deletes last value in the stack; "POP"<br/>
ADD, SUB, MUL, DIV: Does arithmetic to the last two values of the stack and deletes them and pushes the result<br/>
LOG: Logs value of member of stack given an indice; "LOG - 1"<br/>
HLT: Halts the program; "HLT"<br/>
PSS: Starts a one-line comment; "PSS 🗿"<br/>
CHP: Prints a character given an indice of the value in question on the stack<br/>
RGP: Prints a character given the register number<br/>
MRG: Adds multiple registers; "MRG 10"<br/>
