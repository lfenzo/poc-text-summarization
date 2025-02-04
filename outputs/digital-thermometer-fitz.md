

## General Description 

 The DS18B20 digital thermometer provides 9-bit to  12-bit Celsius temperature measurements and has an  alarm function with nonvolatile user-programmable upper  and lower trigger points. The DS18B20 communicates  over a 1-Wire bus that by definition requires only one  data line (and ground) for communication with a central    microprocessor. In addition, the DS18B20 can derive  power directly from the data line (“parasite power”),    eliminating the need for an external power supply.  Each DS18B20 has a unique 64-bit serial code, which  allows multiple DS18B20s to function on the same 1-Wire  bus. Thus, it is simple to use one microprocessor to  control many DS18B20s distributed over a large area.  Applications that can benefit from this feature include  HVAC environmental controls, temperature monitoring  systems inside buildings, equipment, or machinery, and  process monitoring and control systems. 

## Applications 

 ● ● Thermostatic Controls ● ● Industrial Systems ● ● Consumer Products ● ● Thermometers ● ● Thermally Sensitive Systems 

## Benefits and Features 

 ● ● ● ● Stored in On-Board ROM ● ● Flexible User-Definable Nonvolatile (NV) Alarm Settings  with Alarm Search Command Identifies Devices with  Temperatures Outside Programmed Limits ● ● Available in 8-Pin SO (150 mils), 8-Pin µSOP, and  3-Pin TO-92 Packages 19-7487; Rev 6; 7/19 Ordering Information  appears at end of data sheet. 1-Wire is a registered trademark of Maxim Integrated Products, Inc. 

## Pin Configurations 

 BOTTOM VIEW 8 7 6 5 2 N.C. N.C. V DD DQ N.C. N.C. N.C. GND DS18B20 SO (150 mils) (DS18B20Z)  + 1 4 3 7 8 5 6 1 2 3 4 + DQ N.C. N.C. GND V DD N.C. N.C. N.C. DS18B20 µSOP (DS18B20U) DS18B20 1 2 3 GND DQ V DD 1     1 2 3 TOP VIEW TO-92  (DS18B20) 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 Click  here   for production status of specific part numbers. Voltage Range on Any Pin Relative to Ground.....-0.5V to +6.0V Operating Temperature Range. ......................... -55°C to +125°C Storage Temperature Range. ............................ -55°C to +125°C Solder Temperature. ...............................Refer to the IPC/JEDEC  J-STD-020 Specification. (-55°C to +125°C; V DD  = 3.0V to 5.5V) Note 1: Note 2: Note 3: Note 4: Note 5: 	 To guarantee a presence pulse under low voltage parasite power conditions, V ILMAX  may have to be reduced to as low as  0.5V.  Note 6: 	 Logic-high voltages are specified at a source current of 1mA. Note 7: 	 Standby current specified up to +70°C. Standby current typically is 3µA at +125°C. Note 8: 	 To minimize I DDS , DQ should be within the following ranges: GND ≤ DQ ≤ GND + 0.3V or  V DD  – 0.3V ≤ DQ ≤ V DD . Note 9: 	 Active current refers to supply current during active temperature conversions or EEPROM writes. Note 10: 	 DQ line is high (“high-Z” state). Note 11: 	 Drift data is based on a 1000-hour stress test at +125°C with V DD  = 5.5V. PARAMETER SYMBOL CONDITIONS MIN TYP MAX UNITS Supply Voltage V DD Local power (Note 1) +3.0 +5.5 V Pullup Supply Voltage V PU Parasite power  (Notes 1, 2) +3.0 +5.5 V Local power  +3.0 V DD -10°C to +85°C  ±0.5 

## Absolute Maximum Ratings 

 These are stress ratings only and functional operation of the device at these or any other conditions above those indicated in the operation sections of this specification is not implied. Exposure  to absolute maximum rating conditions for extended periods of time may affect reliability. 

## DC Electrical Characteristics 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    2 (-55°C to +125°C; V (-55°C to +125°C; V DD  = 3.0V to 5.5V) Note 12: Note 13: 	 Under parasite power, if t RSTL  > 960µs, a power-on reset can occur. Figure 1. Typical Performance Curve PARAMETER SYMBOL CONDITIONS MIN TYP MAX UNITS 

## AC Electrical Characteristics–NV Memory AC Electrical Characteristics 

 DS18B20 TYPICAL ERROR CURVE 0 -0.1 -0.2 -0.3 -0.4 -0.5 THERMOMETER ERROR (°C) 0 70 10 20 30 40 50 60 TEMPERATURE (°C) MEAN ERROR -3s ERROR 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    3 Figure 2. Timing Diagrams 4 1 2 DQ Data Input/Output. Open-drain 1-Wire interface pin. Also provides power to the  device when used in parasite power mode (see the  Powering the DS18B20  section.)  5 4 1 GND Ground 

## Pin Description 

 1-WIRE READ ZERO TIME SLOT t SLOT 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    4 

## Overview 

 Figure 3 pin descriptions are given in the  The 64-bit ROM stores the device’s unique serial code.  The scratchpad memory contains the 2-byte temperature  register that stores the digital output from the temperature  sensor. In addition, the scratchpad provides access to the  1-byte upper and lower alarm trigger registers (T T tion register allows the user to set the resolution of the  temperature-to-digital conversion to 9, 10, 11, or 12 bits.  The T (EEPROM), so they will retain data when the device is  powered down. The DS18B20 uses Maxim’s exclusive 1-Wire bus proto- col that implements bus communication using one control  signal. The control line requires a weak pullup resistor  since all devices are linked to the bus via a 3-state or  open-drain port (the DQ pin in the case of the DS18B20).  In this bus system, the microprocessor (the master  device) identifies and addresses devices on the bus  using each device’s unique 64-bit code. Because each  device has a unique code, the number of devices that  can be addressed on one bus is virtually unlimited. The  1-Wire bus protocol, including detailed explanations of the  commands and “time slots,” is covered in the  1-Wire Bus  System  section. Another feature of the DS18B20 is the ability to oper- ate without an external power supply. Power is instead  supplied through the 1-Wire pullup resistor through the  DQ pin when the bus is high. The high bus signal also  ), which then supplies  power to the device when the bus is low. This method of  deriving power from the 1-Wire bus is referred to as “para- site power.” As an alternative, the DS18B20 may also be  The core functionality of the DS18B20 is its direct-to- digital temperature sensor. The resolution of the tempera- ture sensor is user-configurable to 9, 10, 11, or 12 bits,  corresponding to increments of 0.5°C, 0.25°C, 0.125°C,  and 0.0625°C, respectively. The default resolution at  power-up is 12-bit. The DS18B20 powers up in a low- power idle state. To initiate a temperature measurement  and A-to-D conversion, the master must issue a Convert  T [44h] command. Following the conversion, the resulting  thermal data is stored in the 2-byte temperature register  in the scratchpad memory and the DS18B20 returns to its  idle state. If the DS18B20 is powered by an external sup- ply, the master can issue “read time slots” (see the  1-Wire  Bus System   section) after the Convert T command and  the DS18B20 will respond by transmitting 0 while the tem- perature conversion is in progress and 1 when the con- version is done. If the DS18B20 is powered with parasite  power, this notification technique cannot be used since  the bus must be pulled high by a strong pullup during the  entire temperature conversion. The bus requirements for  parasite power are explained in detail in the  Powering the  DS18B20  section. Figure 3. DS18B20 Block Diagram TEMPERATURE  SENSOR SCRATCHPAD MEMORY CONTROL LOGIC 64-BIT ROM  AND 1-Wire  PORT PARASITE POWER CIRCUIT POWER- SUPPLY SENSE INTERNAL V DD GND DQ V PU 4.7kΩ CONFIGURATION REGISTER (EEPROM)   8-BIT CRC  GENERATOR V DD C PP DS18B20 ALARM LOW TRIGGER (T L )  REGISTER (EEPROM) ALARM HIGH TRIGGER (T H )  REGISTER (EEPROM) 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    5 The DS18B20 output temperature data is calibrated in  degrees Celsius; for Fahrenheit applications, a lookup  table or conversion routine must be used. The tempera- ture data is stored as a 16-bit sign-extended two’s comple- ment number in the temperature register (see  The sign bits (S) indicate if the temperature is positive  or negative: for positive numbers S = 0 and for negative  numbers S = 1. If the DS18B20 is configured for 12-bit  resolution, all bits in the temperature register will contain  valid data. For 11-bit resolution, bit 0 is undefined. For  10-bit resolution, bits 1 and 0 are undefined, and for 9-bit  resolution bits 2, 1, and 0 are undefined.  examples of digital output data and the corresponding  temperature reading for 12-bit resolution conversions.  

## Operation—Alarm Signaling 

 After the DS18B20 performs a temperature conversion,  the temperature value is compared to the user-defined  two’s complement alarm trigger values stored in the  ). The sign bit (S)  indicates if the value is positive or negative: for positive     registers are nonvolatile (EEPROM) so they will  L  can be accessed through bytes 2 and 3 of the scratchpad  Only bits 11 through 4 of the temperature register are   are  8-bit registers. If the measured temperature is lower than  Figure 4. Temperature Register Format Figure 5. T H  and T L  Register Format 

### Table 1. Temperature/Data Relationship  

 *The power-on reset value of the temperature register is +85°C. BIT 7 BIT 6 BIT 5 BIT 4 BIT 3 BIT 2 BIT 1 BIT 0 LS BYTE  2 3 2 2 2 1 2 0 2 -1 2 -2 2 -3 2 -4 BIT 15 BIT 14 BIT 13 BIT 12 BIT 11 BIT 10 BIT 9 BIT 8 MS BYTE S S S S S 2 6 2 5 2 4 S = SIGN TEMPERATURE (°C) DIGITAL OUTPUT (BINARY) DIGITAL OUTPUT (HEX) +125 0000 0111 1101 0000 07D0h +85* 0000 0101 0101 0000 0550h +25.0625 0000 0001 1001 0001 0191h +10.125 0000 0000 1010 0010 00A2h +0.5 0000 0000 0000 1000 0008h 0 0000 0000 0000 0000 0000h -0.5 1111 1111 1111 1000 FFF8h -10.125 1111 1111 0101 1110 FF5Eh -25.0625 1111 1110 0110 1111 FE6Fh -55 1111 1100 1001 0000 FC90h BIT 7 BIT 6 BIT 5 BIT 4 BIT 3 BIT 2 BIT 1 BIT 0 S 2 6 2 5 2 4 2 3 2 2 2 1 2 0 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    6 or equal to T , an alarm con- dition exists and an alarm flag is set inside the DS18B20.  This flag is updated after every temperature measure- ment; therefore, if the alarm condition goes away, the flag  will be turned off after the next temperature conversion.  The master device can check the alarm flag status of  all DS18B20s on the bus by issuing an Alarm Search  [ECh] command. Any DS18B20s with a set alarm flag will  respond to the command, so the master can determine  exactly which DS18B20s have experienced an alarm  condition. If an alarm condition exists and the T H  or T L  settings have changed, another temperature conversion  should be done to validate the alarm condition. 

## Powering the DS18B20 

 The DS18B20 can be powered by an external supply on  the V DD  pin, or it can operate in “parasite power” mode,  which allows the DS18B20 to function without a local  external supply. Parasite power is very useful for applica- tions that require remote temperature sensing or that are  very space constrained.  Figure 3  shows the DS18B20’s  parasite-power control circuitry, which “steals” power from  the 1-Wire bus via the DQ pin when the bus is high. The  stolen charge powers the DS18B20 while the bus is high,  and some of the charge is stored on the parasite power  capacitor (C PP ) to provide power when the bus is low.  When the DS18B20 is used in parasite power mode, the  V DD  pin must be connected to ground. In parasite power mode, the 1-Wire bus and CPP can pro- vide sufficient current to the DS18B20 for most operations  as long as the specified timing and voltage requirements  are met (see the  DC Electrical Characteristics  and  AC  Electrical Characteristics ). However, when the DS18B20  is performing temperature conversions or copying data  from the scratchpad memory to EEPROM, the operating  current can be as high as 1.5mA. This current can cause  an unacceptable voltage drop across the weak 1-Wire  pullup resistor and is more current than can be supplied  by C . To assure that the DS18B20 has sufficient supply  current, it is necessary to provide a strong pullup on the  1-Wire bus whenever temperature conversions are tak- ing place or data is being copied from the scratchpad to  EEPROM. This can be accomplished by using a MOSFET  to pull the bus directly to the rail as shown in  Figure 6 . The  1-Wire bus must be switched to the strong pullup within  10µs (max) after a Convert T [44h] or Copy Scratchpad  [48h] command is issued, and the bus must be held high  by the pullup for the duration of the conversion (t CONV )  or data transfer (t WR  = 10ms). No other activity can take  place on the 1-Wire bus while the pullup is enabled. The DS18B20 can also be powered by the conventional  method of connecting an external power supply to the  V DD  pin, as shown in  Figure 7 . The advantage of this  method is that the MOSFET pullup is not required, and  the 1-Wire bus is free to carry other traffic during the tem- perature conversion time. The use of parasite power is not recommended for tem- peratures above +100°C since the DS18B20 may not be  able to sustain communications due to the higher leak- age currents that can exist at these temperatures. For  applications in which such temperatures are likely, it is  strongly recommended that the DS18B20 be powered by  an external power supply. In some situations the bus master may not know whether  the DS18B20s on the bus are parasite powered or pow- ered by external supplies. The master needs this informa- tion to determine if the strong bus pullup should be used  during temperature conversions. To get this information,  the master can issue a Skip ROM [CCh] command fol- lowed by a Read Power Supply [B4h] command followed  by a “read time slot”. During the read time slot, parasite  powered DS18B20s will pull the bus low, and externally  powered DS18B20s will let the bus remain high. If the  bus is pulled low, the master knows that it must supply  the strong pullup on the 1-Wire bus during temperature  conversions. Figure 6. Supplying the Parasite-Powered DS18B20 During  Temperature Conversions Figure 7. Powering the DS18B20 with an External Supply V PU 4.7kΩ  V PU 1-Wire BUS DS18B20 GND DQ V DD TO OTHER  1-Wire DEVICES µP V PU 4.7kΩ  1-Wire BUS DS18B20 GND DQ V DD TO OTHER  1-Wire DEVICES µP V DD  (EXTERNAL  SUPPLY) 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    7 

## 64-BIT Lasered ROM code 

 Each DS18B20 contains a unique 64–bit code (see  8 code contain the DS18B20’s 1-Wire family code: 28h. The  next 48 bits contain a unique serial number. The most  significant 8 bits contain a cyclic redundancy check (CRC)  byte that is calculated from the first 56 bits of the ROM  code. A detailed explanation of the CRC bits is provided  in the  associated ROM function control logic allow the DS18B20  to operate as a 1-Wire device using the protocol detailed  in the  1-Wire Bus System  section.  

## Memory 

 The DS18B20’s memory is organized as shown in  Figure  9 . The memory consists of an SRAM scratchpad with  nonvolatile EEPROM storage for the high and low alarm  trigger registers (T H  and T L ) and configuration register.  Note that if the DS18B20 alarm function is not used,  the TH and TL registers can serve as general-purpose  memory. All memory commands are described in detail in  the  DS18B20 Function Commands  section. Byte 0 and byte 1 of the scratchpad contain the LSB and  the MSB of the temperature register, respectively. These  bytes are read-only. Bytes 2 and 3 provide access to TH  and TL registers. Byte 4 contains the configuration regis- Configuration   section. Bytes 5, 6, and 7 are reserved for inter- Byte 8 of the scratchpad is read-only and contains the  CRC code for bytes 0 through 7 of the scratchpad.  The DS18B20 generates this CRC using the method  Data is written to bytes 2, 3, and 4 of the scratchpad using  the Write Scratchpad [4Eh] command; the data must be  transmitted to the DS18B20 starting with the least signifi- cant bit of byte 2. To verify data integrity, the scratchpad  can be read (using the Read Scratchpad [BEh] command)  after the data is written. When reading the scratchpad,  data is transferred over the 1-Wire bus starting with the  least significant bit of byte 0. To transfer the T H , T L  and  configuration data from the scratchpad to EEPROM, the  master must issue the Copy Scratchpad [48h] command.  Data in the EEPROM registers is retained when the  device is powered down; at power-up the EEPROM data  is reloaded into the corresponding scratchpad locations.  Data can also be reloaded from EEPROM to the scratch- pad at any time using the Recall E 2  [B8h] command. The  master can issue read time slots following the Recall E 2   command and the DS18B20 will indicate the status of the  recall by transmitting 0 while the recall is in progress and  1 when the recall is done.  Figure 8. 64-Bit Lasered ROM Code Figure 9. DS18B20 Memory Map 8-BIT CRC 48-BIT SERIAL NUMBER 8-BIT FAMILY CODE (28h) MSB LSB MSB LSB MSB LSB BYTE 0 BYTE 1 TEMPERATURE LSB (50h) TEMPERATURE MSB (05h) (85°C) BYTE 2 BYTE 3 T H  REGISTER OR USER BYTE 1* T L  REGISTER OR USER BYTE 2* BYTE 4 BYTE 5 CONFIGURATION REGISTER* RESERVED (FFh) BYTE 6 BYTE 7 RESERVED RESERVED (10h) BYTE 8 CRC* *POWER-UP STATE DEPENDS ON VALUE(S) STORED IN EEPROM. T H  REGISTER OR USER BYTE 1* T L  REGISTER OR USER BYTE 2* CONFIGURATION REGISTER* SCRATCHPAD (POWER-UP STATE) EEPROM 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    8 

## Configuration Register 

 Byte 4 of the scratchpad memory contains the configura- tion register, which is organized as illustrated in  Figure 10 .  The user can set the conversion resolution of the DS18B20  using the R0 and R1 bits in this register as shown in  2 1 (12-bit resolution). Note that there is a direct tradeoff  between resolution and conversion time. Bit 7 and bits 0 to  4 in the configuration register are reserved for internal use  by the device and cannot be overwritten. 

## CRC Generation 

 CRC bytes are provided as part of the DS18B20’s 64-bit  ROM code and in the 9 th  byte of the scratchpad memory.  The ROM code CRC is calculated from the first 56 bits  of the ROM code and is contained in the most significant  byte of the ROM. The scratchpad CRC is calculated from  the data stored in the scratchpad, and therefore it chang- es when the data in the scratchpad changes. The CRCs  provide the bus master with a method of data validation  when data is read from the DS18B20. To verify that data  has been read correctly, the bus master must re-calculate  the CRC from the received data and then compare this  value to either the ROM code CRC (for ROM reads) or  to the scratchpad CRC (for scratchpad reads). If the cal- culated CRC matches the read CRC, the data has been  received error free. The comparison of CRC values and  the decision to continue with an operation are determined  entirely by the bus master. There is no circuitry inside the  ceeding if the DS18B20 CRC (ROM or scratchpad) does  The equivalent polynomial function of the CRC (ROM or  The bus master can re-calculate the CRC and compare it  to the CRC values from the DS18B20 using the polyno- mial generator shown in  Figure 11 . This circuit consists  of a shift register and XOR gates, and the shift register  bits are initialized to 0. Starting with the least significant  bit of the ROM code or the least significant bit of byte 0  in the scratchpad, one bit at a time should shifted into the  shift register. After shifting in the 56th bit from the ROM or  the most significant bit of byte 7 from the scratchpad, the  polynomial generator will contain the recalculated CRC.  Next, the 8-bit ROM code or scratchpad CRC from the  DS18B20 must be shifted into the circuit. At this point, if  the re-calculated CRC was correct, the shift register will  contain all 0s. Additional information about the Maxim  1-Wire cyclic redundancy check is available in  Application  Note 27: Understanding and Using Cyclic Redundancy  Checks with Maxim iButton Products . Figure 10. Configuration Register Figure 11. CRC Generator 

### Table 2. Thermometer Resolution Configuration  

 R1 R0 RESOLUTION (BITS) MAX CONVERSION TIME 0 0 9  93.75ms (t CONV /8) 0 1 10 187.5ms (t CONV /4) 1 0 11 375ms (t CONV /2) 1 1 12 750ms (t CONV ) BIT 7 BIT 6 BIT 5 BIT 4 BIT 3 BIT 2 BIT 1 BIT 0 0 R1 R0 1 1 1 1 1 XOR XOR XOR INPUT MSB LSB 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    9 

## 1-Wire Bus System 

 The 1-Wire bus system uses a single bus master to con- trol one or more slave devices. The DS18B20 is always a  slave. When there is only one slave on the bus, the sys- tem is referred to as a “single-drop” system; the system is  “multidrop” if there are multiple slaves on the bus.  All data and commands are transmitted least significant  bit first over the 1-Wire bus. The following discussion of the 1-Wire bus system is  broken down into three topics: hardware configuration,  transaction sequence, and 1-Wire signaling (signal types  and timing). 

## Hardware Configuration 

 The 1-Wire bus has by definition only a single data line.  Each device (master or slave) interfaces to the data line  via an open-drain or 3-state port. This allows each device  to “release” the data line when the device is not transmit- ting data so the bus is available for use by another device.  The 1-Wire port of the DS18B20 (the DQ pin) is open  drain with an internal circuit equivalent to that shown in  Figure 12 .  The 1-Wire bus requires an external pullup resistor of  approximately 5kΩ; thus, the idle state for the 1-Wire  bus is high. If for any reason a transaction needs to be  suspended, the bus MUST be left in the idle state if the  transaction is to resume. Infinite recovery time can occur  between bits so long as the 1-Wire bus is in the inactive  (high) state during the recovery period. If the bus is held  low for more than 480µs, all components on the bus will  be reset. 

## Transaction Sequence 

 The transaction sequence for accessing the DS18B20 is  as follows: Step 1.	 Initialization Step 2.	 ROM Command (followed by any required data  exchange) Step 3.	 DS18B20 Function Command (followed by any  required data exchange) It is very important to follow this sequence every time the  DS18B20 is accessed, as the DS18B20 will not respond  if any steps in the sequence are missing or out of order.  Exceptions to this rule are the Search ROM [F0h] and  Alarm Search [ECh] commands. After issuing either of  these ROM commands, the master must return to Step 1  in the sequence.  

## Initialization 

 All transactions on the 1-Wire bus begin with an initializa- tion sequence. The initialization sequence consists of a  reset pulse transmitted by the bus master followed by  presence pulse(s) transmitted by the slave(s). The pres- ence pulse lets the bus master know that slave devices  (such as the DS18B20) are on the bus and are ready  to operate. Timing for the reset and presence pulses is  detailed in the  1-Wire Signaling  section. 

## ROM Commands 

 After the bus master has detected a presence pulse, it  can issue a ROM command. These commands operate  on the unique 64-bit ROM codes of each slave device  and allow the master to single out a specific device if  many are present on the 1-Wire bus. These commands  also allow the master to determine how many and what  types of devices are present on the bus or if any device  has experienced an alarm condition. There are five ROM  commands, and each command is 8 bits long. The master  device must issue an appropriate ROM command before  issuing a DS18B20 function command. A flowchart for  operation of the ROM commands is shown in  Figure 13 . 

#### Search Rom [F0h] 

 When a system is initially powered up, the master must  identify the ROM codes of all slave devices on the bus,  which allows the master to determine the number of  slaves and their device types. The master learns the  ROM codes through a process of elimination that requires  the master to perform a Search ROM cycle (i.e., Search  ROM command followed by data exchange) as many  times as necessary to identify all of the slave devices.  Figure 12. Hardware Configuration DQ V PU 4.7k Ω   DS18B20 1-WIRE PORT Rx Tx 100 Ω   MOSFET 5µA TYP 1-WIRE BUS Rx Tx Rx = RECEIVE Tx = TRANSMIT 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    10 If there is only one slave on the bus, the simpler Read  ROM [33h] command can be used in place of the Search  ROM process. For a detailed explanation of the Search  ROM procedure, refer to  Application Note 937: Book of  iButton ®  Standards . After every Search ROM cycle, the  bus master must return to Step 1 (Initialization) in the  transaction sequence. 

#### Read Rom [33h] 

 This command can only be used when there is one slave  on the bus. It allows the bus master to read the slave’s  64-bit ROM code without using the Search ROM proce- dure. If this command is used when there is more than  one slave present on the bus, a data collision will occur  when all the slaves attempt to respond at the same time.  

#### Match Rom [55H] 

 The match ROM command followed by a 64-bit ROM  code sequence allows the bus master to address a  specific slave device on a multidrop or single-drop bus.  Only the slave that exactly matches the 64-bit ROM code  sequence will respond to the function command issued  by the master; all other slaves on the bus will wait for a  reset pulse.  

#### Skip Rom [CCh] 

 The master can use this command to address all devices  on the bus simultaneously without sending out any ROM  code information. For example, the master can make all  DS18B20s on the bus perform simultaneous temperature  conversions by issuing a Skip ROM command followed by  a Convert T [44h] command.  Note that the Read Scratchpad [BEh] command can  follow the Skip ROM command only if there is a single  slave device on the bus. In this case, time is saved by  allowing the master to read from the slave without send- ing the device’s 64-bit ROM code. A Skip ROM command  followed by a Read Scratchpad command will cause  a data collision on the bus if there is more than one  slave since multiple devices will attempt to transmit data    simultaneously.  

#### Alarm Search [ECh] 

 The operation of this command is identical to the operation  of the Search ROM command except that only slaves with  a set alarm flag will respond. This command allows the  master device to determine if any DS18B20s experienced  an alarm condition during the most recent temperature  conversion. After every Alarm Search cycle (i.e., Alarm  Search command followed by data exchange), the bus  master must return to Step 1 (Initialization) in the transac- tion sequence. See the  Operation—Alarm Signaling  sec- tion for an explanation of alarm flag operation. 

## DS18B20 Function Commands  

 After the bus master has used a ROM command to  address the DS18B20 with which it wishes to communi- cate, the master can issue one of the DS18B20 function  commands. These commands allow the master to write  to and read from the DS18B20’s scratchpad memory,  initiate temperature conversions and determine the power  supply mode. The DS18B20 function commands, which  are described below, are summarized in  Table 3  and illus- trated by the flowchart in  Figure 14 . 

#### Convert T [44h] 

 This command initiates a single temperature conversion.  Following the conversion, the resulting thermal data is  stored in the 2-byte temperature register in the scratch- pad memory and the DS18B20 returns to its low-power  idle state. If the device is being used in parasite power  mode, within 10µs (max) after this command is issued  the master must enable a strong pullup on the 1-Wire bus  for the duration of the conversion (t CONV ) as described  in the  Powering the DS18B20  section. If the DS18B20 is  powered by an external supply, the master can issue read  time slots after the Convert T command and the DS18B20  will respond by transmitting a 0 while the temperature  conversion is in progress and a 1 when the conversion is  done. In parasite power mode this notification technique  cannot be used since the bus is pulled high by the strong  pullup during the conversion. 

#### Write Scratchpad [4Eh] 

 This command allows the master to write 3 bytes of data  to the DS18B20’s scratchpad. The first data byte is written  into the T H  register (byte 2 of the scratchpad), the second  byte is written into the T L  register (byte 3), and the third  byte is written into the configuration register (byte 4). Data  must be transmitted least significant bit first. All three  bytes MUST be written before the master issues a reset,  or the data may be corrupted. 

#### Read Scratchpad [BEh] 

 This command allows the master to read the contents of  the scratchpad. The data transfer starts with the least sig- nificant bit of byte 0 and continues through the scratchpad  until the 9th byte (byte 8 – CRC) is read. The master may  issue a reset to terminate reading at any time if only part  of the scratchpad data is needed. iButton is a registered trademark of Maxim Integrated Products, Inc. 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    11 

#### Copy Scratchpad [48h] 

 This command copies the contents of the scratchpad  T H , T L  and configuration registers (bytes 2, 3 and 4) to  EEPROM. If the device is being used in parasite power  mode, within 10µs (max) after this command is issued the  master must enable a strong pullup on the 1-Wire bus for  at least 10ms as described in the  Powering the DS18B20  section. 

#### Recall E 

 This command recalls the alarm trigger values (T T data in bytes 2, 3, and 4, respectively, in the scratchpad  memory. The master device can issue read time slots  following the Recall E 2  command and the DS18B20 will  indicate the status of the recall by transmitting 0 while the  recall is in progress and 1 when the recall is done. The  recall operation happens automatically at power-up, so  valid data is available in the scratchpad as soon as power  is applied to the device. 

#### Read Power Supply [B4h] 

 The master device issues this command followed by a  read time slot to determine if any DS18B20s on the bus  nally powered DS18B20s will let the bus remain high. See  section for usage information  

### Table 3. DS18B20 Function Command Set 

 Note 1: 	 For parasite-powered DS18B20s, the master must enable a strong pullup on the 1-Wire bus during temperature conver- sions and copies from the scratchpad to EEPROM. No other bus activity may take place during this time. Note 2: 	 The master can interrupt the transmission of data at any time by issuing a reset. Note 3: 	 All three bytes must be written before a reset is issued. Scratchpad CRC byte. BEh to master. 2 Write  Scratchpad Writes data into scratchpad bytes 2, 3, and  4 (T H , T L , and configuration registers). 4Eh Master transmits 3 data bytes to  DS18B20. 3 Copy  Scratchpad Copies T H , T L , and configuration register  data from the scratchpad to EEPROM. 48h None 1 Recall E 2 Recalls T H , T L , and configuration register  data from EEPROM to the scratchpad. B8h DS18B20 transmits recall status to  master. Read Power  Supply Signals DS18B20 power supply mode to  the master. B4h DS18B20 transmits supply status to  master. 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    12 Figure 13. ROM Commands Flowchart MASTER Tx FUNCTION  COMMAND (FIGURE 14) 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    13 Figure 14. DS18B20 Function Commands Flowchart  RETURN TO INITIALIZATION  SEQUENCE (FIGURE 13)  FOR NEXT TRANSACTION 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    14 

## 1-Wire Signaling 

 The DS18B20 uses a strict 1-Wire communication pro- tocol to ensure data integrity. Several signal types are  defined by this protocol: reset pulse, presence pulse, write  0, write 1, read 0, and read 1. The bus master initiates all  these signals, with the exception of the presence pulse. 

## Initialization Procedure—Reset And  Presence Pulses 

 All communication with the DS18B20 begins with an ini- tialization sequence that consists of a reset pulse from the  master followed by a presence pulse from the DS18B20.  This is illustrated in  the presence pulse in response to the reset, it is indicating  to the master that it is on the bus and ready to operate.  During the initialization sequence the bus master trans- mits (T X ) the reset pulse by pulling the 1-Wire bus low  for a minimum of 480µs. The bus master then releases  the bus and goes into receive mode (R X ). When the bus  is released, the 5kΩ pullup resistor pulls the 1-Wire bus  high. When the DS18B20 detects this rising edge, it waits  15µs to 60µs and then transmits a presence pulse by pull- ing the 1-Wire bus low for 60µs to 240µs. The bus master writes data to the DS18B20 during write  time slots and reads data from the DS18B20 during read  time slots. One bit of data is transmitted over the 1-Wire  There are two types of write time slots: “Write 1” time slots  and “Write 0” time slots. The bus master uses a Write 1  time slot to write a logic 1 to the DS18B20 and a Write  0 time slot to write a logic 0 to the DS18B20. All write  time slots must be a minimum of 60µs in duration with a  minimum of a 1µs recovery time between individual write  slots. Both types of write time slots are initiated by the  To generate a Write 1 time slot, after pulling the 1-Wire  bus low, the bus master must release the 1-Wire bus  within 15µs. When the bus is released, the 5kΩ pullup  resistor will pull the bus high. To generate a Write 0 time  slot, after pulling the 1-Wire bus low, the bus master must  continue to hold the bus low for the duration of the time  slot (at least 60µs). The DS18B20 samples the 1-Wire bus during a window  that lasts from 15µs to 60µs after the master initiates the  write time slot. If the bus is high during the sampling win- dow, a 1 is written to the DS18B20. If the line is low, a 0  is written to the DS18B20. Figure 15. Initialization Timing LINE TYPE LEGEND DS18B20 PULLING LOW RESISTOR PULLUP   MASTER Tx RESET PULSE 480µs MINIMUM   MASTER Rx 480µs MINIMUM DS18B20  WAITS 15-60µs V PU 1-Wire BUS GND DS18B20 TX PRESENCE  PULSE 60-240µS BUS MASTER PULLING LOW 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    15 

## Read Time Slots 

 The DS18B20 can only transmit data to the master when  the master issues read time slots. Therefore, the master  must generate read time slots immediately after issuing  a Read Scratchpad [BEh] or Read Power Supply [B4h]  command, so that the DS18B20 can provide the request- ed data. In addition, the master can generate read time  slots after issuing Convert T [44h] or Recall E mands to find out the status of the operation as explained  in the  All read time slots must be a minimum of 60µs in duration  with a minimum of a 1µs recovery time between slots. A  read time slot is initiated by the master device pulling the  1-Wire bus low for a minimum of 1µs and then releasing  the bus (see  Figure 16 ). After the master initiates the  read time slot, the DS18B20 will begin transmitting a 1  or 0 on bus. The DS18B20 transmits a 1 by leaving the  bus high and transmits a 0 by pulling the bus low. When  transmitting a 0, the DS18B20 will release the bus by the  end of the time slot, and the bus will be pulled back to  its high idle state by the pullup resister. Output data from  the DS18B20 is valid for 15µs after the falling edge that  initiated the read time slot. Therefore, the master must  release the bus and then sample the bus state within  , and  T SAMPLE  must be less than 15µs for a read time slot.  Figure 18  shows that system timing margin is maximized  by keeping T INIT  and T RC  as short as possible and by  locating the master sample time during read time slots  towards the end of the 15µs period. Figure 16. Read/Write Time Slot Timing Diagram MASTER WRITE “0” SLOT MASTER WRITE “1” SLOT 60µs < Tx “0” < 120µs START OF SLOT START OF SLOT 1µs < T REC  < ∞  1µs MIN              TYP      MAX DS18B20 SAMPLES 15µs 15µs 30µs MIN              TYP      MAX DS18B20 SAMPLES 15µs 15µs 30µs V PU 1-Wire BUS GND 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    16 

## Related Application Notes 

 The  following  application  notes  can  be  applied to the DS18B20 and are available at  www.maximintegrated.com . Application Note 27: Understanding and Using Cyclic  Redundancy Checks with Maxim iButton Products Application Note 122: Using Dallas’ 1-Wire ICs in 1-Cell  Li-Ion Battery Packs with Low-Side N-Channel Safety  FETs Master  Application Note 126: 1-Wire Communication Through  Software Application Note 162: Interfacing the DS18x20/DS1822  1-Wire Temperature Sensor in a Microcontroller  Environment Application Note 208: Curve Fitting the Error of a  Application Note 2420: 1-Wire Communication with a  Application Note 3754: Single-Wire Serial Bus Carries  Sample 1-Wire subroutines that can be used in conjunc- pplication Note 74: Reading and Writing iBut-  can be downloaded from the  Figure 17. Detailed Master Read 1 Timing Figure 18. Recommended Master Read 1 Timing  VIH OF MASTER MASTER SAMPLES V PU 1-Wire BUS GND 15µs T INT  > 1µs T RC VIH OF MASTER       V PU 1-Wire BUS GND 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    17 

## DS18B20 Operation Example 1 

 In this example there are multiple DS18B20s on the bus  and they are using parasite power. The bus master initi- ates a temperature conversion in a specific DS18B20 and  then reads its scratchpad and recalculates the CRC to  verify the data.  

## DS18B20 Operation Example 2 

 In this example there is only one DS18B20 on the bus and  it is using parasite power. The master writes to the TH, TL,  and configuration registers in the DS18B20 scratchpad  and then reads the scratchpad and recalculates the CRC  to verify the data. The master then copies the scratchpad  contents to EEPROM.  Rx 9 data bytes scratchpad and compares the  calculated CRC with the read  CRC (byte 9). If they match,  the master continues; if not, the  read operation is repeated. the master continues; if not, the  read operation is repeated. Tx Reset Master issues reset pulse. Rx Presence DS18B20 responds with  presence pulse. Tx CCh Master issues Skip ROM  command. Tx 48h Master issues Copy Scratchpad  command.  Tx DQ line  held high by  strong pullup Master applies strong pullup to  DQ for at least 10ms while copy  operation is in progress. 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    18 +Denotes a lead-free package. A “+” will appear on the top mark of lead-free packages. T&R = Tape and reel. * TO-92 packages in tape and reel can be ordered with straight or formed leads. Choose “SL” for straight leads. Bulk TO-92 orders  are straight leads only. PART TEMP RANGE PIN-PACKAGE TOP MARK DS18B20 -55°C to +125°C 3 TO-92 18B20 DS18B20+ -55°C to +125°C 3 TO-92 18B20 DS18B20/T&R -55°C to +125°C 3 TO-92 (2000 Piece) 18B20 DS18B20+T&R -55°C to +125°C 3 TO-92 (2000 Piece) 18B20  DS18B20-SL/T&R -55°C to +125°C 3 TO-92 (2000 Piece)* 18B20 DS18B20-SL+T&R -55°C to +125°C 3 TO-92 (2000 Piece)* 18B20  DS18B20U -55°C to +125°C 8 FSOP 18B20 DS18B20U+ -55°C to +125°C 8 FSOP 18B20 DS18B20U/T&R -55°C to +125°C 8 FSOP (3000 Piece) 18B20 DS18B20U+T&R -55°C to +125°C 8 FSOP (3000 Piece) 18B20 DS18B20Z -55°C to +125°C 8 SO DS18B20 DS18B20Z+ -55°C to +125°C 8 SO DS18B20 DS18B20Z/T&R -55°C to +125°C 8 SO (2500 Piece) DS18B20 DS18B20Z+T&R -55°C to +125°C 8 SO (2500 Piece)  DS18B20 

## Ordering Information 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 www.maximintegrated.com Maxim Integrated   │    19 REVISION  DATE DESCRIPTION PAGES  CHANGED 3/1/07 In the Absolute Maximum Ratings section, removed the reflow oven temperature value of +220°C.  Reference to JEDEC specification for reflow remains. 19 10/12/07 In the  Operation—Alarm Signaling  section, added “or equal to” in the description for a TH alarm  condition 5 In the  Memory  section, removed incorrect text describing memory. 7 In the  Configuration Register  section, removed incorrect text describing configuration register. 8 4/22/08 In the  Ordering Information  table, added TO-92 straight-lead packages and included a note that the  TO-92 package in tape and reel can be ordered with either formed or straight leads. 2 1/15 Updated  Benefits and Features  section 1 09/18 Updated  DC Electrical Characteristics  table 2 7/19 Updated Figure 12 10 

## Revision History 

 Maxim Integrated cannot assume responsibility for use of any circuitry other than circuitry entirely embodied in a Maxim Integrated product. No circuit patent licenses  are implied. Maxim Integrated reserves the right to change the circuitry and specifications without notice at any time. The parametric values (min and max limits)  shown in the Electrical Characteristics table are guaranteed. Other parametric values quoted in this data sheet are provided for guidance. Maxim Integrated and the Maxim Integrated logo are trademarks of Maxim Integrated Products, Inc. 

# DS18B20 Programmable Resolution  1-Wire Digital Thermometer  

 ©  2019 Maxim Integrated Products, Inc.   │    20 For pricing, delivery, and ordering information, please visit Maxim Integrated’s online storefront at https://www.maximintegrated.com/en/storefront/storefront.html. 