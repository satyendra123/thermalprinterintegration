# thermalprinterintegration
i have integrate the thermal printer with the python code. this is a power, mode, feed in the fronted side

Command Description	ESC/POS Command	Bytes
Initialize printer	ESC @	0x1B 0x40
Print text	Your text\n	ASCII bytes + 0x0A
Line feed	LF	0x0A
Cut paper	GS V 0	0x1D 0x56 0x00
Bold on	ESC E 1	0x1B 0x45 0x01
Bold off	ESC E 0	0x1B 0x45 0x00
Center alignment	ESC a 1	0x1B 0x61 0x01

1B 40                       ; Initialize
1B 61 01                   ; Center align
1B 45 01                   ; Bold on
48 65 6C 6C 6F             ; "Hello"
20 48 6F 6F 6B             ; " Hook"
20 50 72 69 6E 74 65 72    ; " Printer"
1B 45 00                   ; Bold off
0A                         ; New line
1D 56 00                   ; Partial cut
