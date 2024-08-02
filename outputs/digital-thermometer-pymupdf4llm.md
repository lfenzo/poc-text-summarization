_[Click here](https://www.maximintegrated.com/en/storefront/storefront.html)_ _for production status of specific part numbers._

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**General Description**
The DS18B20 digital thermometer provides 9-bit to
12-bit Celsius temperature measurements and has an
alarm function with nonvolatile user-programmable upper
and lower trigger points. The DS18B20 communicates
over a 1-Wire bus that by definition requires only one
data line (and ground) for communication with a central
microprocessor. In addition, the DS18B20 can derive
power directly from the data line (“parasite power”),
eliminating the need for an external power supply.

Each DS18B20 has a unique 64-bit serial code, which
allows multiple DS18B20s to function on the same 1-Wire
bus. Thus, it is simple to use one microprocessor to
control many DS18B20s distributed over a large area.
Applications that can benefit from this feature include
HVAC environmental controls, temperature monitoring
systems inside buildings, equipment, or machinery, and
process monitoring and control systems.

**Applications**

- ● Thermostatic Controls

- ● Industrial Systems

- ● Consumer Products

- ● Thermometers

- ● Thermally Sensitive Systems

**_Ordering Information appears at end of data sheet._**

_1-Wire is a registered trademark of Maxim Integrated Products, Inc._


**Benefits and Features**

- ● Unique 1-Wire[®] Interface Requires Only One Port
Pin for Communication

- ● Reduce Component Count with Integrated
Temperature Sensor and EEPROM

-  Measures Temperatures from -55°C to +125°C
(-67°F to +257°F)

-  ±0.5°C Accuracy from -10°C to +85°C

-  Programmable Resolution from 9 Bits to 12 Bits

-  No External Components Required

- ● Parasitic Power Mode Requires Only 2 Pins for
Operation (DQ and GND)

- ● Simplifies Distributed Temperature-Sensing
Applications with Multidrop Capability

-  Each Device Has a Unique 64-Bit Serial Code
Stored in On-Board ROM

- ● Flexible User-Definable Nonvolatile (NV) Alarm Settings
with Alarm Search Command Identifies Devices with
Temperatures Outside Programmed Limits

- ● Available in 8-Pin SO (150 mils), 8-Pin µSOP, and
3-Pin TO-92 Packages

**Pin Configurations**

|Col1|1|Col3|
|---|---|---|

|Col1|8|Col3|
|---|---|---|

|Col1|2|Col3|
|---|---|---|

|Col1|7|Col3|
|---|---|---|

|Col1|2|Col3|
|---|---|---|
||3||
||4||

|Col1|7|Col3|
|---|---|---|
||6||
||5||


TOP VIEW

**+**

N.C. 1 8 N.C.

**DS18B20**

N.C. 2 **DS18B20** 7 N.C.

1 2 3

VDD 3 6 N.C.

DQ 4 5 GND

**SO (150 mils)**
**(DS18B20Z)**

DQ 1 **+** 8 VDD

GND DQ VDD N.C. 2 7 N.C.

**DS18B20**

N.C. 3 6 N.C.

1 2 3 GND 4 5 N.C.

1 **µSOP**

BOTTOM VIEW **(DS18B20U)**

**TO-92**
**(DS18B20)**


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

**Absolute Maximum Ratings**

Voltage Range on Any Pin Relative to Ground.....-0.5V to +6.0V Storage Temperature Range............................. -55°C to +125°C
Operating Temperature Range.......................... -55°C to +125°C Solder Temperature................................Refer to the IPC/JEDEC
J-STD-020 Specification.

_These are stress ratings only and functional operation of the device at these or any other conditions above those indicated in the operation sections of this specification is not implied. Exposure_
_to absolute maximum rating conditions for extended periods of time may affect reliability._

**DC Electrical Characteristics**

(-55°C to +125°C; VDD = 3.0V to 5.5V)

|PARAMETER|SYMBOL|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
|Supply Voltage|VDD|Local power (Note 1)||+3.0 +5.5|V|
|Pullup Supply Voltage|VPU|Parasite power|(Notes 1, 2)|+3.0 +5.5|V|
|||Local power||+3.0 VDD||
|Thermometer Error|tERR|-10°C to +85°C|(Note 3)|±0.5|°C|
|||-30°C to +100°C||±1||
|||-55°C to +125°C||±2||
|Input Logic-Low|VIL|(Notes 1, 4, 5)||-0.3 +0.8|V|
|Input Logic-High|VIH|Local power|(Notes 1,6)|+2.2 The lower of 5.5 or +3.0 VDD + 0.3|V|
|||Parasite power||||
|Sink Current|IL|VI/O = 0.4V||4.0|mA|
|Standby Current|IDDS|(Notes 7, 8)||750 1000|nA|
|Active Current|IDD|VDD = 5V (Note 9)||1 1.5|mA|
|DQ Input Current|IDQ|(Note 10)||5|µA|
|Drift||(Note 11)||±0.2|°C|



**Note 1:** All voltages are referenced to ground.
**Note 2:** The Pullup Supply Voltage specification assumes that the pullup device is ideal, and therefore the high level of the
pullup is equal to VPU. In order to meet the VIH spec of the DS18B20, the actual supply rail for the strong pullup transistor must include margin for the voltage drop across the transistor when it is turned on; thus: VPU_ACTUAL = VPU_IDEAL +
VTRANSISTOR.
**Note 3:** See typical performance curve in Figure 1. Thermometer Error limits are 3-sigma values.
**Note 4:** Logic-low voltages are specified at a sink current of 4mA.
**Note 5:** To guarantee a presence pulse under low voltage parasite power conditions, VILMAX may have to be reduced to as low as
0.5V.
**Note 6:** Logic-high voltages are specified at a source current of 1mA.
**Note 7:** Standby current specified up to +70°C. Standby current typically is 3µA at +125°C.
**Note 8:** To minimize IDDS, DQ should be within the following ranges: GND ≤ DQ ≤ GND + 0.3V or VDD – 0.3V ≤ DQ ≤ VDD.
**Note 9:** Active current refers to supply current during active temperature conversions or EEPROM writes.
**Note 10: DQ line is high (“high-Z” state).**
**Note 11: Drift data is based on a 1000-hour stress test at +125°C with VDD = 5.5V.**


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

**AC Electrical Characteristics–NV Memory**


(-55°C to +125°C; VDD = 3.0V to 5.5V)

|PARAMETER|SYMBOL|CONDITIONS|MIN TYP MAX|UNITS|
|---|---|---|---|---|
|NV Write Cycle Time|tWR||2 10|ms|
|EEPROM Writes|NEEWR|-55°C to +55°C|50k|writes|
|EEPROM Data Retention|tEEDR|-55°C to +55°C|10|years|


**PARAMETER** **SYMBOL** **CONDITIONS** **MIN** **TYP** **MAX** **UNITS**

NV Write Cycle Time tWR 2 10 ms

EEPROM Writes NEEWR -55°C to +55°C 50k writes

EEPROM Data Retention tEEDR -55°C to +55°C 10 years


**AC Electrical Characteristics**


(-55°C to +125°C; VDD = 3.0V to 5.5V)

|PARAMETER|SYMBOL|CONDITIONS|Col4|MIN TYP MAX|UNITS|
|---|---|---|---|---|---|
|Temperature Conversion Time|tCONV|9-bit resolution|(Note 12)|93.75|ms|
|||10-bit resolution||187.5||
|||11-bit resolution||375||
|||12-bit resolution||750||
|Time to Strong Pullup On|tSPON|Start convert T command issued||10|µs|
|Time Slot|tSLOT|(Note 12)||60 120|µs|
|Recovery Time|tREC|(Note 12)||1|µs|
|Write 0 Low Time|tLOW0|(Note 12)||60 120|µs|
|Write 1 Low Time|tLOW1|(Note 12)||1 15|µs|
|Read Data Valid|tRDV|(Note 12)||15|µs|
|Reset Time High|tRSTH|(Note 12)||480|µs|
|Reset Time Low|tRSTL|(Notes 12, 13)||480|µs|
|Presence-Detect High|tPDHIGH|(Note 12)||15 60|µs|
|Presence-Detect Low|tPDLOW|(Note 12)||60 240|µs|
|Capacitance|CIN/OUT|||25|pF|


**PARAMETER** **SYMBOL** **CONDITIONS** **MIN** **TYP** **MAX** **UNITS**

9-bit resolution 93.75

10-bit resolution 187.5

Temperature Conversion Time tCONV (Note 12) ms

11-bit resolution 375

12-bit resolution 750

Time to Strong Pullup On tSPON Start convert T command issued 10 µs

Time Slot tSLOT (Note 12) 60 120 µs

Recovery Time tREC (Note 12) 1 µs

Write 0 Low Time tLOW0 (Note 12) 60 120 µs

Write 1 Low Time tLOW1 (Note 12) 1 15 µs

Read Data Valid tRDV (Note 12) 15 µs

Reset Time High tRSTH (Note 12) 480 µs

Reset Time Low tRSTL (Notes 12, 13) 480 µs

Presence-Detect High tPDHIGH (Note 12) 15 60 µs

Presence-Detect Low tPDLOW (Note 12) 60 240 µs

Capacitance CIN/OUT 25 pF


**Note 12: See the timing diagrams in Figure 2.**
**Note 13: Under parasite power, if tRSTL > 960µs, a power-on reset can occur.**


**DS18B20 TYPICAL ERROR CURVE**


0.5

0.4

0.3

0.2

0.1


-0.1

-0.2

-0.3

-0.4

-0.5

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||+3s ERR|OR|||
||||||||
||||||||
||||||||
||||||-3s ERROR||
||||||||
|MEA|N ERROR||||||
||||||||


0

_Figure 1. Typical Performance Curve_


10 20 30 40 50 60 70

TEMPERATURE (°C)


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

**1-WIRE WRITE ZERO TIME SLOT**

tSLOT

tREC START OF NEXT CYCLE

tLOW0

**1-WIRE READ ZERO TIME SLOT**

tSLOT
START OF NEXT CYCLE

tREC

tRDV

**1-WIRE RESET PULSE**

RESET PULSE FROM HOST

tRSTL tRSTH

PRESENCE DETECT

**1-WIRE PRESENCE DETECT**

tPDIH

tPDLOW


_Figure 2. Timing Diagrams_

|Pin Description|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|PIN|||NAME|FUNCTION|
|SO|µSOP|TO-92|||
|1, 2, 6, 7, 8|2, 3, 5, 6, 7|—|N.C.|No Connection|
|3|8|3|VDD|Optional VDD. VDD must be grounded for operation in parasite power mode.|
|4|1|2|DQ|Data Input/Output. Open-drain 1-Wire interface pin. Also provides power to the device when used in parasite power mode (see the Powering the DS18B20 section.)|
|5|4|1|GND|Ground|


**PIN**
**NAME** **FUNCTION**
**SO** **µSOP** **TO-92**

1, 2, 6, 2, 3, 5,
— N.C. No Connection
7, 8 6, 7

3 8 3 VDD Optional VDD. VDD must be grounded for operation in parasite power mode.

Data Input/Output. Open-drain 1-Wire interface pin. Also provides power to the
4 1 2 DQ
device when used in parasite power mode (see the Powering the DS18B20 section.)

5 4 1 GND Ground


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**Overview**
Figure 3 shows a block diagram of the DS18B20, and
pin descriptions are given in the _Pin Description table._
The 64-bit ROM stores the device’s unique serial code.
The scratchpad memory contains the 2-byte temperature
register that stores the digital output from the temperature
sensor. In addition, the scratchpad provides access to the
1-byte upper and lower alarm trigger registers (TH and
TL) and the 1-byte configuration register. The configuration register allows the user to set the resolution of the
temperature-to-digital conversion to 9, 10, 11, or 12 bits.
The TH, TL, and configuration registers are nonvolatile
(EEPROM), so they will retain data when the device is
powered down.

The DS18B20 uses Maxim’s exclusive 1-Wire bus protocol that implements bus communication using one control
signal. The control line requires a weak pullup resistor
since all devices are linked to the bus via a 3-state or
open-drain port (the DQ pin in the case of the DS18B20).
In this bus system, the microprocessor (the master
device) identifies and addresses devices on the bus
using each device’s unique 64-bit code. Because each
device has a unique code, the number of devices that
can be addressed on one bus is virtually unlimited. The
1-Wire bus protocol, including detailed explanations of the
commands and “time slots,” is covered in the 1-Wire Bus
_System section._

Another feature of the DS18B20 is the ability to operate without an external power supply. Power is instead
supplied through the 1-Wire pullup resistor through the

|Col1|PARASITE POWER CIRCUIT|Col3|
|---|---|---|
||CPP|INTERNAL VDD|
|||POWER-|
||SUPPLY SENSE||


VPU

MEMORY

4.7kΩ PARASITE POWER CIRCUIT CONTROL LOGIC **DS18B20**

DQ

TEMPERATURE
SENSOR

GND INTERNAL VDD 64-BIT ROM ALARM HIGH TRIGGER (TH)

REGISTER (EEPROM)

AND 1-Wire

CPP PORT ALARM LOW TRIGGER (TL)

SCRATCHPAD

REGISTER (EEPROM)

VDD POWER- CONFIGURATION

SUPPLY SENSE REGISTER (EEPROM)

8-BIT CRC
GENERATOR


_Figure 3. DS18B20 Block Diagram_


DQ pin when the bus is high. The high bus signal also
charges an internal capacitor (CPP), which then supplies
power to the device when the bus is low. This method of
deriving power from the 1-Wire bus is referred to as “parasite power.” As an alternative, the DS18B20 may also be
powered by an external supply on VDD.

**Operation—Measuring Temperature**
The core functionality of the DS18B20 is its direct-todigital temperature sensor. The resolution of the temperature sensor is user-configurable to 9, 10, 11, or 12 bits,
corresponding to increments of 0.5°C, 0.25°C, 0.125°C,
and 0.0625°C, respectively. The default resolution at
power-up is 12-bit. The DS18B20 powers up in a lowpower idle state. To initiate a temperature measurement
and A-to-D conversion, the master must issue a Convert
T [44h] command. Following the conversion, the resulting
thermal data is stored in the 2-byte temperature register
in the scratchpad memory and the DS18B20 returns to its
idle state. If the DS18B20 is powered by an external supply, the master can issue “read time slots” (see the 1-Wire
_Bus System_ section) after the Convert T command and
the DS18B20 will respond by transmitting 0 while the temperature conversion is in progress and 1 when the conversion is done. If the DS18B20 is powered with parasite
power, this notification technique cannot be used since
the bus must be pulled high by a strong pullup during the
entire temperature conversion. The bus requirements for
parasite power are explained in detail in the Powering the
_DS18B20 section._


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**Operation—Alarm Signaling**
After the DS18B20 performs a temperature conversion,
the temperature value is compared to the user-defined
two’s complement alarm trigger values stored in the
1-byte TH and TL registers (see Figure 5). The sign bit (S)
indicates if the value is positive or negative: for positive
numbers S = 0 and for negative numbers S = 1. The TH
and TL registers are nonvolatile (EEPROM) so they will
retain data when the device is powered down. TH and TL
can be accessed through bytes 2 and 3 of the scratchpad
as explained in the Memory section.

Only bits 11 through 4 of the temperature register are
used in the TH and TL comparison since TH and TL are
8-bit registers. If the measured temperature is lower than


The DS18B20 output temperature data is calibrated in
degrees Celsius; for Fahrenheit applications, a lookup
table or conversion routine must be used. The temperature data is stored as a 16-bit sign-extended two’s complement number in the temperature register (see Figure 4).
The sign bits (S) indicate if the temperature is positive
or negative: for positive numbers S = 0 and for negative
numbers S = 1. If the DS18B20 is configured for 12-bit
resolution, all bits in the temperature register will contain
valid data. For 11-bit resolution, bit 0 is undefined. For
10-bit resolution, bits 1 and 0 are undefined, and for 9-bit
resolution bits 2, 1, and 0 are undefined. Table 1 gives
examples of digital output data and the corresponding
temperature reading for 12-bit resolution conversions.

|23|22|21|20|2-1|2-2|2-3|2-4|
|---|---|---|---|---|---|---|---|


|S|S|S|S|S|26|25|24|
|---|---|---|---|---|---|---|---|


**BIT 7** **BIT 6** **BIT 5** **BIT 4** **BIT 3** **BIT 2** **BIT 1** **BIT 0**

**LS BYTE** 2[3] 2[2] 2[1] 2[0] 2[-1] 2[-2] 2[-3] 2[-4]

**BIT 15** **BIT 14** **BIT 13** **BIT 12** **BIT 11** **BIT 10** **BIT 9** **BIT 8**

**MS BYTE** S S S S S 2[6] 2[5] 2[4]

S = SIGN


_Figure 4. Temperature Register Format_

**Table 1. Temperature/Data Relationship**

|TEMPERATURE (°C)|DIGITAL OUTPUT (BINARY)|DIGITAL OUTPUT (HEX)|
|---|---|---|
|+125|0000 0111 1101 0000|07D0h|
|+85*|0000 0101 0101 0000|0550h|
|+25.0625|0000 0001 1001 0001|0191h|
|+10.125|0000 0000 1010 0010|00A2h|
|+0.5|0000 0000 0000 1000|0008h|
|0|0000 0000 0000 0000|0000h|
|-0.5|1111 1111 1111 1000|FFF8h|
|-10.125|1111 1111 0101 1110|FF5Eh|
|-25.0625|1111 1110 0110 1111|FE6Fh|
|-55|1111 1100 1001 0000|FC90h|


**DIGITAL OUTPUT** **DIGITAL OUTPUT**
**TEMPERATURE (°C)**
**(BINARY)** **(HEX)**

+125 0000 0111 1101 0000 07D0h

+85* 0000 0101 0101 0000 0550h

+25.0625 0000 0001 1001 0001 0191h

+10.125 0000 0000 1010 0010 00A2h

+0.5 0000 0000 0000 1000 0008h

0 0000 0000 0000 0000 0000h

-0.5 1111 1111 1111 1000 FFF8h

-10.125 1111 1111 0101 1110 FF5Eh

-25.0625 1111 1110 0110 1111 FE6Fh

-55 1111 1100 1001 0000 FC90h


_*The power-on reset value of the temperature register is +85°C._

|S|26|25|24|23|22|21|20|
|---|---|---|---|---|---|---|---|


**BIT 7** **BIT 6** **BIT 5** **BIT 4** **BIT 3** **BIT 2** **BIT 1** **BIT 0**

S 2[6] 2[5] 2[4] 2[3] 2[2] 2[1] 2[0]


_Figure 5. TH and TL Register Format_


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


or equal to TL or higher than or equal to TH, an alarm condition exists and an alarm flag is set inside the DS18B20.
This flag is updated after every temperature measurement; therefore, if the alarm condition goes away, the flag
will be turned off after the next temperature conversion.

The master device can check the alarm flag status of
all DS18B20s on the bus by issuing an Alarm Search

[ECh] command. Any DS18B20s with a set alarm flag will
respond to the command, so the master can determine
exactly which DS18B20s have experienced an alarm
condition. If an alarm condition exists and the TH or TL
settings have changed, another temperature conversion
should be done to validate the alarm condition.

**Powering the DS18B20**
The DS18B20 can be powered by an external supply on
the VDD pin, or it can operate in “parasite power” mode,
which allows the DS18B20 to function without a local
external supply. Parasite power is very useful for applications that require remote temperature sensing or that are
very space constrained. Figure 3 shows the DS18B20’s
parasite-power control circuitry, which “steals” power from
the 1-Wire bus via the DQ pin when the bus is high. The
stolen charge powers the DS18B20 while the bus is high,
and some of the charge is stored on the parasite power
capacitor (CPP) to provide power when the bus is low.
When the DS18B20 is used in parasite power mode, the
VDD pin must be connected to ground.

In parasite power mode, the 1-Wire bus and CPP can provide sufficient current to the DS18B20 for most operations
as long as the specified timing and voltage requirements
are met (see the _DC Electrical Characteristics and_ _AC_
_Electrical Characteristics). However, when the DS18B20_
is performing temperature conversions or copying data
from the scratchpad memory to EEPROM, the operating
current can be as high as 1.5mA. This current can cause
an unacceptable voltage drop across the weak 1-Wire
pullup resistor and is more current than can be supplied


by CPP. To assure that the DS18B20 has sufficient supply
current, it is necessary to provide a strong pullup on the
1-Wire bus whenever temperature conversions are taking place or data is being copied from the scratchpad to
EEPROM. This can be accomplished by using a MOSFET
to pull the bus directly to the rail as shown in Figure 6. The
1-Wire bus must be switched to the strong pullup within
10µs (max) after a Convert T [44h] or Copy Scratchpad

[48h] command is issued, and the bus must be held high
by the pullup for the duration of the conversion (tCONV)
or data transfer (tWR = 10ms). No other activity can take
place on the 1-Wire bus while the pullup is enabled.

The DS18B20 can also be powered by the conventional
method of connecting an external power supply to the
VDD pin, as shown in Figure 7. The advantage of this
method is that the MOSFET pullup is not required, and
the 1-Wire bus is free to carry other traffic during the temperature conversion time.

The use of parasite power is not recommended for temperatures above +100°C since the DS18B20 may not be
able to sustain communications due to the higher leakage currents that can exist at these temperatures. For
applications in which such temperatures are likely, it is
strongly recommended that the DS18B20 be powered by
an external power supply.

In some situations the bus master may not know whether
the DS18B20s on the bus are parasite powered or powered by external supplies. The master needs this information to determine if the strong bus pullup should be used
during temperature conversions. To get this information,
the master can issue a Skip ROM [CCh] command followed by a Read Power Supply [B4h] command followed
by a “read time slot”. During the read time slot, parasite
powered DS18B20s will pull the bus low, and externally
powered DS18B20s will let the bus remain high. If the
bus is pulled low, the master knows that it must supply
the strong pullup on the 1-Wire bus during temperature
conversions.

|Col1|Col2|
|---|---|


VPU

**DS18B20**

VPU

GND DQ VDD

µP

4.7kΩ

1-Wire BUS TO OTHER

1-Wire DEVICES


**DS18B20**

VPU VDD (EXTERNAL

GND DQ VDD SUPPLY)

µP

4.7kΩ

1-Wire BUS TO OTHER

1-Wire DEVICES


_Figure 6. Supplying the Parasite-Powered DS18B20 During_ _Figure 7. Powering the DS18B20 with an External Supply_
_Temperature Conversions_


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**64-BIT Lasered ROM code**
Each DS18B20 contains a unique 64–bit code (see Figure
8) stored in ROM. The least significant 8 bits of the ROM
code contain the DS18B20’s 1-Wire family code: 28h. The
next 48 bits contain a unique serial number. The most
significant 8 bits contain a cyclic redundancy check (CRC)
byte that is calculated from the first 56 bits of the ROM
code. A detailed explanation of the CRC bits is provided
in the CRC Generation section. The 64-bit ROM code and
associated ROM function control logic allow the DS18B20
to operate as a 1-Wire device using the protocol detailed
in the 1-Wire Bus System section.

**Memory**
The DS18B20’s memory is organized as shown in Figure
9. The memory consists of an SRAM scratchpad with
nonvolatile EEPROM storage for the high and low alarm
trigger registers (TH and TL) and configuration register.
Note that if the DS18B20 alarm function is not used,
the TH and TL registers can serve as general-purpose
memory. All memory commands are described in detail in
the DS18B20 Function Commands section.

Byte 0 and byte 1 of the scratchpad contain the LSB and
the MSB of the temperature register, respectively. These
bytes are read-only. Bytes 2 and 3 provide access to TH
and TL registers. Byte 4 contains the configuration regis
|8-BIT CRC|48-BIT SERIAL NUMBER|8-BIT FAMILY CODE (28h)|
|---|---|---|


8-BIT CRC 48-BIT SERIAL NUMBER 8-BIT FAMILY CODE (28h)

MSB LSB MSB LSB MSB LSB


_Figure 8. 64-Bit Lasered ROM Code_

BYTE 8 CRC*


ter data, which is explained in detail in the Configuration
_Register section. Bytes 5, 6, and 7 are reserved for inter-_
nal use by the device and cannot be overwritten.

Byte 8 of the scratchpad is read-only and contains the
CRC code for bytes 0 through 7 of the scratchpad.
The DS18B20 generates this CRC using the method
described in the CRC Generation section.

Data is written to bytes 2, 3, and 4 of the scratchpad using
the Write Scratchpad [4Eh] command; the data must be
transmitted to the DS18B20 starting with the least significant bit of byte 2. To verify data integrity, the scratchpad
can be read (using the Read Scratchpad [BEh] command)
after the data is written. When reading the scratchpad,
data is transferred over the 1-Wire bus starting with the
least significant bit of byte 0. To transfer the TH, TL and
configuration data from the scratchpad to EEPROM, the
master must issue the Copy Scratchpad [48h] command.

Data in the EEPROM registers is retained when the
device is powered down; at power-up the EEPROM data
is reloaded into the corresponding scratchpad locations.
Data can also be reloaded from EEPROM to the scratchpad at any time using the Recall E[2] [B8h] command. The
master can issue read time slots following the Recall E[2]
command and the DS18B20 will indicate the status of the
recall by transmitting 0 while the recall is in progress and
1 when the recall is done.

8-BIT FAMILY CODE (28h)

LSB MSB LSB

**EEPROM**

|SCRATCHPAD (POWER-UP STATE)|Col2|
|---|---|
|TEMPERATURE LSB (50h)||
|TEMPERATURE MSB (05h)|(85°C)|
|TH REGISTER OR USER BYTE 1*||
|TL REGISTER OR USER BYTE 2*||
|CONFIGURATION REGISTER*||
|RESERVED (FFh)||
|RESERVED||
|RESERVED (10h)||
|CRC*||


TH REGISTER OR USER BYTE 1*

TL REGISTER OR USER BYTE 2*

CONFIGURATION REGISTER*


*POWER-UP STATE DEPENDS ON VALUE(S) STORED IN EEPROM.

_Figure 9. DS18B20 Memory Map_


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**Configuration Register**
Byte 4 of the scratchpad memory contains the configuration register, which is organized as illustrated in Figure 10.
The user can set the conversion resolution of the DS18B20
using the R0 and R1 bits in this register as shown in Table
2. The power-up default of these bits is R0 = 1 and R1 =
1 (12-bit resolution). Note that there is a direct tradeoff
between resolution and conversion time. Bit 7 and bits 0 to
4 in the configuration register are reserved for internal use
by the device and cannot be overwritten.

**CRC Generation**
CRC bytes are provided as part of the DS18B20’s 64-bit
ROM code and in the 9[th] byte of the scratchpad memory.
The ROM code CRC is calculated from the first 56 bits
of the ROM code and is contained in the most significant
byte of the ROM. The scratchpad CRC is calculated from
the data stored in the scratchpad, and therefore it changes when the data in the scratchpad changes. The CRCs
provide the bus master with a method of data validation
when data is read from the DS18B20. To verify that data
has been read correctly, the bus master must re-calculate
the CRC from the received data and then compare this
value to either the ROM code CRC (for ROM reads) or
to the scratchpad CRC (for scratchpad reads). If the calculated CRC matches the read CRC, the data has been

|0|R1|R0|1|1|1|1|1|
|---|---|---|---|---|---|---|---|


**BIT 7** **BIT 6** **BIT 5** **BIT 4** **BIT 3** **BIT 2** **BIT 1** **BIT 0**

0 R1 R0 1 1 1 1 1


_Figure 10. Configuration Register_


received error free. The comparison of CRC values and
the decision to continue with an operation are determined
entirely by the bus master. There is no circuitry inside the
DS18B20 that prevents a command sequence from proceeding if the DS18B20 CRC (ROM or scratchpad) does
not match the value generated by the bus master.

The equivalent polynomial function of the CRC (ROM or
scratchpad) is:

CRC = X[8] + X[5] + X[4 ]+ 1

The bus master can re-calculate the CRC and compare it
to the CRC values from the DS18B20 using the polynomial generator shown in Figure 11. This circuit consists
of a shift register and XOR gates, and the shift register
bits are initialized to 0. Starting with the least significant
bit of the ROM code or the least significant bit of byte 0
in the scratchpad, one bit at a time should shifted into the
shift register. After shifting in the 56th bit from the ROM or
the most significant bit of byte 7 from the scratchpad, the
polynomial generator will contain the recalculated CRC.
Next, the 8-bit ROM code or scratchpad CRC from the
DS18B20 must be shifted into the circuit. At this point, if
the re-calculated CRC was correct, the shift register will
contain all 0s. Additional information about the Maxim
1-Wire cyclic redundancy check is available in Application
_Note 27: Understanding and Using Cyclic Redundancy_
_Checks with Maxim iButton Products._


**Table 2. Thermometer Resolution Configuration**

|R1|R0|RESOLUTION (BITS)|MAX CONVERSION TIME|Col5|
|---|---|---|---|---|
|0|0|9|93.75ms|(tCONV/8)|
|0|1|10|187.5ms|(tCONV/4)|
|1|0|11|375ms|(tCONV/2)|
|1|1|12|750ms|(tCONV)|


**RESOLUTION**
**R1** **R0** **MAX CONVERSION TIME**
**(BITS)**

0 0 9 93.75ms (tCONV/8)

0 1 10 187.5ms (tCONV/4)

1 0 11 375ms (tCONV/2)

1 1 12 750ms (tCONV)

INPUT

XOR XOR XOR

MSB LSB


_Figure 11. CRC Generator_


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**1-Wire Bus System**
The 1-Wire bus system uses a single bus master to control one or more slave devices. The DS18B20 is always a
slave. When there is only one slave on the bus, the system is referred to as a “single-drop” system; the system is
“multidrop” if there are multiple slaves on the bus.

All data and commands are transmitted least significant
bit first over the 1-Wire bus.

The following discussion of the 1-Wire bus system is
broken down into three topics: hardware configuration,
transaction sequence, and 1-Wire signaling (signal types
and timing).

**Hardware Configuration**
The 1-Wire bus has by definition only a single data line.
Each device (master or slave) interfaces to the data line
via an open-drain or 3-state port. This allows each device
to “release” the data line when the device is not transmitting data so the bus is available for use by another device.
The 1-Wire port of the DS18B20 (the DQ pin) is open
drain with an internal circuit equivalent to that shown in
Figure 12.

The 1-Wire bus requires an external pullup resistor of
approximately 5kΩ; thus, the idle state for the 1-Wire
bus is high. If for any reason a transaction needs to be
suspended, the bus MUST be left in the idle state if the
transaction is to resume. Infinite recovery time can occur
between bits so long as the 1-Wire bus is in the inactive
(high) state during the recovery period. If the bus is held
low for more than 480µs, all components on the bus will
be reset.

VPU

**DS18B20**
4.7kΩ **1-WIRE PORT**

Rx 1-WIRE BUS DQ Rx

5µA Tx
TYP

100Ω
MOSFET

Tx

Rx = RECEIVE
Tx = TRANSMIT


_Figure 12. Hardware Configuration_


**Transaction Sequence**
The transaction sequence for accessing the DS18B20 is
as follows:

Step 1. Initialization

Step 2. ROM Command (followed by any required data
exchange)

Step 3. DS18B20 Function Command (followed by any
required data exchange)

It is very important to follow this sequence every time the
DS18B20 is accessed, as the DS18B20 will not respond
if any steps in the sequence are missing or out of order.
Exceptions to this rule are the Search ROM [F0h] and
Alarm Search [ECh] commands. After issuing either of
these ROM commands, the master must return to Step 1
in the sequence.

**Initialization**
All transactions on the 1-Wire bus begin with an initialization sequence. The initialization sequence consists of a
reset pulse transmitted by the bus master followed by
presence pulse(s) transmitted by the slave(s). The presence pulse lets the bus master know that slave devices
(such as the DS18B20) are on the bus and are ready
to operate. Timing for the reset and presence pulses is
detailed in the 1-Wire Signaling section.

**ROM Commands**
After the bus master has detected a presence pulse, it
can issue a ROM command. These commands operate
on the unique 64-bit ROM codes of each slave device
and allow the master to single out a specific device if
many are present on the 1-Wire bus. These commands
also allow the master to determine how many and what
types of devices are present on the bus or if any device
has experienced an alarm condition. There are five ROM
commands, and each command is 8 bits long. The master
device must issue an appropriate ROM command before
issuing a DS18B20 function command. A flowchart for
operation of the ROM commands is shown in Figure 13.

**Search Rom [F0h]**
When a system is initially powered up, the master must
identify the ROM codes of all slave devices on the bus,
which allows the master to determine the number of
slaves and their device types. The master learns the
ROM codes through a process of elimination that requires
the master to perform a Search ROM cycle (i.e., Search
ROM command followed by data exchange) as many
times as necessary to identify all of the slave devices.


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


If there is only one slave on the bus, the simpler Read
ROM [33h] command can be used in place of the Search
ROM process. For a detailed explanation of the Search
ROM procedure, refer to _[Application Note 937: Book of](http://www.Application Note 937)_
_[iButton[®] Standards. After every Search ROM cycle, the](http://www.Application Note 937)_
bus master must return to Step 1 (Initialization) in the
transaction sequence.

**Read Rom [33h]**
This command can only be used when there is one slave
on the bus. It allows the bus master to read the slave’s
64-bit ROM code without using the Search ROM procedure. If this command is used when there is more than
one slave present on the bus, a data collision will occur
when all the slaves attempt to respond at the same time.

**Match Rom [55H]**
The match ROM command followed by a 64-bit ROM
code sequence allows the bus master to address a
specific slave device on a multidrop or single-drop bus.
Only the slave that exactly matches the 64-bit ROM code
sequence will respond to the function command issued
by the master; all other slaves on the bus will wait for a
reset pulse.

**Skip Rom [CCh]**
The master can use this command to address all devices
on the bus simultaneously without sending out any ROM
code information. For example, the master can make all
DS18B20s on the bus perform simultaneous temperature
conversions by issuing a Skip ROM command followed by
a Convert T [44h] command.

Note that the Read Scratchpad [BEh] command can
follow the Skip ROM command only if there is a single
slave device on the bus. In this case, time is saved by
allowing the master to read from the slave without sending the device’s 64-bit ROM code. A Skip ROM command
followed by a Read Scratchpad command will cause
a data collision on the bus if there is more than one
slave since multiple devices will attempt to transmit data
simultaneously.

**Alarm Search [ECh]**
The operation of this command is identical to the operation
of the Search ROM command except that only slaves with
a set alarm flag will respond. This command allows the
master device to determine if any DS18B20s experienced
an alarm condition during the most recent temperature
conversion. After every Alarm Search cycle (i.e., Alarm
Search command followed by data exchange), the bus

_iButton is a registered trademark of Maxim Integrated Products, Inc._


master must return to Step 1 (Initialization) in the transaction sequence. See the Operation—Alarm Signaling section for an explanation of alarm flag operation.

**DS18B20 Function Commands**
After the bus master has used a ROM command to
address the DS18B20 with which it wishes to communicate, the master can issue one of the DS18B20 function
commands. These commands allow the master to write
to and read from the DS18B20’s scratchpad memory,
initiate temperature conversions and determine the power
supply mode. The DS18B20 function commands, which
are described below, are summarized in Table 3 and illustrated by the flowchart in Figure 14.

**Convert T [44h]**
This command initiates a single temperature conversion.
Following the conversion, the resulting thermal data is
stored in the 2-byte temperature register in the scratchpad memory and the DS18B20 returns to its low-power
idle state. If the device is being used in parasite power
mode, within 10µs (max) after this command is issued
the master must enable a strong pullup on the 1-Wire bus
for the duration of the conversion (tCONV) as described
in the Powering the DS18B20 section. If the DS18B20 is
powered by an external supply, the master can issue read
time slots after the Convert T command and the DS18B20
will respond by transmitting a 0 while the temperature
conversion is in progress and a 1 when the conversion is
done. In parasite power mode this notification technique
cannot be used since the bus is pulled high by the strong
pullup during the conversion.

**Write Scratchpad [4Eh]**
This command allows the master to write 3 bytes of data
to the DS18B20’s scratchpad. The first data byte is written
into the TH register (byte 2 of the scratchpad), the second
byte is written into the TL register (byte 3), and the third
byte is written into the configuration register (byte 4). Data
must be transmitted least significant bit first. All three
bytes MUST be written before the master issues a reset,
or the data may be corrupted.

**Read Scratchpad [BEh]**
This command allows the master to read the contents of
the scratchpad. The data transfer starts with the least significant bit of byte 0 and continues through the scratchpad
until the 9th byte (byte 8 – CRC) is read. The master may
issue a reset to terminate reading at any time if only part
of the scratchpad data is needed.


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


following the Recall E[2] command and the DS18B20 will
indicate the status of the recall by transmitting 0 while the
recall is in progress and 1 when the recall is done. The
recall operation happens automatically at power-up, so
valid data is available in the scratchpad as soon as power
is applied to the device.

**Read Power Supply [B4h]**
The master device issues this command followed by a
read time slot to determine if any DS18B20s on the bus
are using parasite power. During the read time slot, parasite powered DS18B20s will pull the bus low, and externally powered DS18B20s will let the bus remain high. See
the Powering the DS18B20 section for usage information
for this command.


**Copy Scratchpad [48h]**
This command copies the contents of the scratchpad
TH, TL and configuration registers (bytes 2, 3 and 4) to
EEPROM. If the device is being used in parasite power
mode, within 10µs (max) after this command is issued the
master must enable a strong pullup on the 1-Wire bus for
at least 10ms as described in the Powering the DS18B20
section.

**Recall E[2] [B8h]**
This command recalls the alarm trigger values (TH and
TL) and configuration data from EEPROM and places the
data in bytes 2, 3, and 4, respectively, in the scratchpad
memory. The master device can issue read time slots

**Table 3. DS18B20 Function Command Set**

|COMMAND|DESCRIPTION|PROTOCOL|1-Wire BUS ACTIVITY AFTER COMMAND IS ISSUED|NOTES|
|---|---|---|---|---|
|TEMPERATURE CONVERSION COMMANDS|||||
|Convert T|Initiates temperature conversion.|44h|DS18B20 transmits conversion status to master (not applicable for parasite- powered DS18B20s).|1|
|MEMORY COMMANDS|||||
|Read Scratchpad|Reads the entire scratchpad including the CRC byte.|BEh|DS18B20 transmits up to 9 data bytes to master.|2|
|Write Scratchpad|Writes data into scratchpad bytes 2, 3, and 4 (TH, TL, and configuration registers).|4Eh|Master transmits 3 data bytes to DS18B20.|3|
|Copy Scratchpad|Copies TH, TL, and configuration register data from the scratchpad to EEPROM.|48h|None|1|
|Recall E2|Recalls TH, TL, and configuration register data from EEPROM to the scratchpad.|B8h|DS18B20 transmits recall status to master.||
|Read Power Supply|Signals DS18B20 power supply mode to the master.|B4h|DS18B20 transmits supply status to master.||


**Note 1: For parasite-powered DS18B20s, the master must enable a strong pullup on the 1-Wire bus during temperature conver-**
sions and copies from the scratchpad to EEPROM. No other bus activity may take place during this time.
**Note 2: The master can interrupt the transmission of data at any time by issuing a reset.**
**Note 3: All three bytes must be written before a reset is issued.**


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

MASTER Tx RESET PULSE

INITIALIZATION
SEQUENCE

DS18B20 Tx PRESENCE PULSE

MASTER Tx ROM COMMAND

33h READ N 55h MATCH N F0h N ECh N CCh N
ROM ROM SEARCH ROM ALARM SEARCH SKIP ROM
COMMAND COMMAND COMMAND COMMAND COMMAND

Y Y Y Y Y

DS18B20 Tx BIT 0 DS18B20 Tx BIT 0

MASTER Tx
BIT 0 DS18B20 Tx BIT 0 DS18B20 Tx BIT 0

MASTER Tx BIT 0 MASTER TX BIT 0

BIT 0 N N BIT 0 N DEVICE(S) N

WITH ALARM

MATCH ? MATCH ?

FLAG SET ?

DS18B20 TX Y Y Y
FAMILY CODE 1
BYTE

DS18B20 Tx BIT 1

MASTER Tx

DS18B20 Tx BIT 1 DS18B20 Tx BIT 1
SERIAL NUMBER

MASTER Tx BIT 1

6 BYTES

DS18B20 Tx
CRC BYTE BIT 1 N N BIT 1

MATCH? MATCH?

Y Y

DS18B20 Tx BIT 63

MASTER Tx
BIT 63 DS18B20 Tx BIT 63

MASTER Tx BIT 63

BIT 63 N N BIT 63
MATCH? MATCH?

Y Y

MASTER Tx FUNCTION
COMMAND (FIGURE 14)


_Figure 13. ROM Commands Flowchart_


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

MASTER Tx 44h CONVERT N 48h COPY N
FUNCTION COMMAND TEMPERATURE ? SCRATCHPAD ?

Y Y

N PARASITE Y N PARASITE Y

POWER ? POWER ?

DS18B20 BEGINS
CONVERSION

MASTER ENABLES STRONG MASTER ENABLES STRONG
PULL-UP ON DQ PULL-UP ON DQ

DEVICE
CONVERTING N DS18B20 CONVERTS COPY IN N DATA COPIED FROM
TEMPERATURE ? TEMPERATURE PROGRESS ? SCRATCHPAD TO EEPROM

Y MASTER DISABLES Y MASTER DISABLES

STRONG PULLUP STRONG PULLUP

MASTER MASTER MASTER MASTER
Rx “0s” Rx “1s” Rx “0s” Rx “1s”

N B4h READ N B8h N BEh READ N 4Eh WRITE

POWER SUPPLY ? RECALL E[2 ]? SCRATCHPAD ? SCRATCHPAD ?

Y Y Y Y

MASTER BEGINS

N PARASITE Y DATA RECALL FROM MASTER Rx DATA

POWER ? E[2] PROM BYTE FROM MASTER Tx TH BYTE TO

SCRATCHPAD SCRATCHPAD

MASTER MASTER

MASTER Tx TL BYTE TO

Rx “1s” Rx “0s” DEVICE BUSY N MASTER Tx Y SCRATCHPAD

RECALLING RESET ?
DATA ?

Y N MASTER TX CONFIG. BYTE

TO SCRATCHPAD

MASTER MASTER
Rx “0s” Rx “1s” N HAVE 8 BYTES

BEEN READ ?

Y

MASTER Rx
SCRATCHPAD CRC
BYTE

RETURN TO INITIALIZATION
SEQUENCE (FIGURE 13)
FOR NEXT TRANSACTION


_Figure 14. DS18B20 Function Commands Flowchart_


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**1-Wire Signaling**
The DS18B20 uses a strict 1-Wire communication protocol to ensure data integrity. Several signal types are
defined by this protocol: reset pulse, presence pulse, write
0, write 1, read 0, and read 1. The bus master initiates all
these signals, with the exception of the presence pulse.

**Initialization Procedure—Reset And**
**Presence Pulses**
All communication with the DS18B20 begins with an initialization sequence that consists of a reset pulse from the
master followed by a presence pulse from the DS18B20.
This is illustrated in Figure 15. When the DS18B20 sends
the presence pulse in response to the reset, it is indicating
to the master that it is on the bus and ready to operate.

During the initialization sequence the bus master transmits (TX) the reset pulse by pulling the 1-Wire bus low
for a minimum of 480µs. The bus master then releases
the bus and goes into receive mode (RX). When the bus
is released, the 5kΩ pullup resistor pulls the 1-Wire bus
high. When the DS18B20 detects this rising edge, it waits
15µs to 60µs and then transmits a presence pulse by pulling the 1-Wire bus low for 60µs to 240µs.

MASTER Tx RESET PULSE MASTER Rx
480µs MINIMUM 480µs MINIMUM

DS18B20

DS18B20 TX PRESENCE

WAITS 15-60µs

PULSE 60-240µS

VPU

1-Wire BUS

GND

LINE TYPE LEGEND

BUS MASTER PULLING LOW

DS18B20 PULLING LOW

RESISTOR PULLUP


_Figure 15. Initialization Timing_


**Read/Write Time Slots**
The bus master writes data to the DS18B20 during write
time slots and reads data from the DS18B20 during read
time slots. One bit of data is transmitted over the 1-Wire
bus per time slot.

**Write Time Slots**
There are two types of write time slots: “Write 1” time slots
and “Write 0” time slots. The bus master uses a Write 1
time slot to write a logic 1 to the DS18B20 and a Write
0 time slot to write a logic 0 to the DS18B20. All write
time slots must be a minimum of 60µs in duration with a
minimum of a 1µs recovery time between individual write
slots. Both types of write time slots are initiated by the
master pulling the 1-Wire bus low (see Figure 14).

To generate a Write 1 time slot, after pulling the 1-Wire
bus low, the bus master must release the 1-Wire bus
within 15µs. When the bus is released, the 5kΩ pullup
resistor will pull the bus high. To generate a Write 0 time
slot, after pulling the 1-Wire bus low, the bus master must
continue to hold the bus low for the duration of the time
slot (at least 60µs).

The DS18B20 samples the 1-Wire bus during a window
that lasts from 15µs to 60µs after the master initiates the
write time slot. If the bus is high during the sampling window, a 1 is written to the DS18B20. If the line is low, a 0
is written to the DS18B20.


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

START START
OF SLOT OF SLOT

**MASTER WRITE “0” SLOT**

1µs < TREC < ∞ **MASTER WRITE “1” SLOT**

60µs < Tx “0” < 120µs

1µs

VPU

1-Wire BUS

GND

**DS18B20 SAMPLES** **DS18B20 SAMPLES**

MIN    TYP MAX MIN    TYP MAX

15µs 15µs 30µs 15µs 15µs 30µs

**MASTER READ “0” SLOT** **MASTER READ “1” SLOT**

1µs < TREC < ∞

VPU

1-Wire BUS

GND

MASTER SAMPLES > 1µs

MASTER SAMPLES

> 1µs

15µs 45µs 15µs

LINE TYPE LEGEND

BUS MASTER PULLING LOW DS18B20 PULLING LOW RESISTOR PULLUP


_Figure 16. Read/Write Time Slot Timing Diagram_


**Read Time Slots**
The DS18B20 can only transmit data to the master when
the master issues read time slots. Therefore, the master
must generate read time slots immediately after issuing
a Read Scratchpad [BEh] or Read Power Supply [B4h]
command, so that the DS18B20 can provide the requested data. In addition, the master can generate read time
slots after issuing Convert T [44h] or Recall E[2] [B8h] commands to find out the status of the operation as explained
in the DS18B20 Function Commands section.

All read time slots must be a minimum of 60µs in duration
with a minimum of a 1µs recovery time between slots. A
read time slot is initiated by the master device pulling the
1-Wire bus low for a minimum of 1µs and then releasing
the bus (see Figure 16). After the master initiates the


read time slot, the DS18B20 will begin transmitting a 1
or 0 on bus. The DS18B20 transmits a 1 by leaving the
bus high and transmits a 0 by pulling the bus low. When
transmitting a 0, the DS18B20 will release the bus by the
end of the time slot, and the bus will be pulled back to
its high idle state by the pullup resister. Output data from
the DS18B20 is valid for 15µs after the falling edge that
initiated the read time slot. Therefore, the master must
release the bus and then sample the bus state within
15µs from the start of the slot.

Figure 17 illustrates that the sum of TINIT, TRC, and
TSAMPLE must be less than 15µs for a read time slot.
Figure 18 shows that system timing margin is maximized
by keeping TINIT and TRC as short as possible and by
locating the master sample time during read time slots
towards the end of the 15µs period.


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

VPU

VIH OF MASTER

1-Wire BUS

GND

TINT > 1µs TRC MASTER SAMPLES

15µs


_Figure 17. Detailed Master Read 1 Timing_

VPU

VIH OF MASTER

1-Wire BUS

GND

TINT = TRC =
SMALL SMALL MASTER SAMPLES

15µs

LINE TYPE LEGEND

BUS MASTER PULLING LOW

RESISTOR PULLUP


_Figure 18. Recommended Master Read 1 Timing_


**Related Application Notes**
The following application notes can be
applied to the DS18B20 and are available at
**www.maximintegrated.com.**

_Application Note 27: Understanding and Using Cyclic_
_Redundancy Checks with Maxim iButton Products_

_Application Note 122: Using Dallas’ 1-Wire ICs in 1-Cell_
_Li-Ion Battery Packs with Low-Side N-Channel Safety_
_FETs Master_

_Application Note 126: 1-Wire Communication Through_
_Software_


_Application Note 162: Interfacing the DS18x20/DS1822_
_1-Wire Temperature Sensor in a Microcontroller_
_Environment_

_Application Note 208: Curve Fitting the Error of a_
_Bandgap-Based Digital Temperature Sensor_

_Application Note 2420: 1-Wire Communication with a_
_Microchip PICmicro Microcontroller_

_Application Note 3754: Single-Wire Serial Bus Carries_
_Isolated Power and Data_

Sample 1-Wire subroutines that can be used in conjunction with Application Note 74: Reading and Writing iBut_tons via Serial Interfaces can be downloaded from the_
Maxim website.


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer


**DS18B20 Operation Example 1**
In this example there are multiple DS18B20s on the bus
and they are using parasite power. The bus master initiates a temperature conversion in a specific DS18B20 and
then reads its scratchpad and recalculates the CRC to
verify the data.


**DS18B20 Operation Example 2**
In this example there is only one DS18B20 on the bus and
it is using parasite power. The master writes to the TH, TL,
and configuration registers in the DS18B20 scratchpad
and then reads the scratchpad and recalculates the CRC
to verify the data. The master then copies the scratchpad
contents to EEPROM.

|MASTER MODE|DATA (LSB FIRST)|COMMENTS|
|---|---|---|
|Tx|Reset|Master issues reset pulse.|
|Rx|Presence|DS18B20s respond with presence pulse.|
|Tx|55h|Master issues Match ROM command.|
|Tx|64-bit ROM code|Master sends DS18B20 ROM code.|
|Tx|44h|Master issues Convert T command.|
|Tx|DQ line held high by strong pullup|Master applies strong pullup to DQ for the duration of the conversion (tCONV).|
|Tx|Reset|Master issues reset pulse.|
|Rx|Presence|DS18B20s respond with presence pulse.|
|Tx|55h|Master issues Match ROM command.|
|Tx|64-bit ROM code|Master sends DS18B20 ROM code.|
|Tx|BEh|Master issues Read Scratchpad command.|
|Rx|9 data bytes|Master reads entire scratchpad including CRC. The master then recalculates the CRC of the first eight data bytes from the scratchpad and compares the calculated CRC with the read CRC (byte 9). If they match, the master continues; if not, the read operation is repeated.|

|MASTER MODE|DATA (LSB FIRST)|COMMENTS|
|---|---|---|
|Tx|Reset|Master issues reset pulse.|
|Rx|Presence|DS18B20 responds with presence pulse.|
|Tx|CCh|Master issues Skip ROM command.|
|Tx|4Eh|Master issues Write Scratchpad command.|
|Tx|3 data bytes|Master sends three data bytes to scratchpad (TH, TL, and config).|
|Tx|Reset|Master issues reset pulse.|
|Rx|Presence|DS18B20 responds with presence pulse.|
|Tx|CCh|Master issues Skip ROM command.|
|Tx|BEh|Master issues Read Scratchpad command.|
|Rx|9 data bytes|Master reads entire scratchpad including CRC. The master then recalculates the CRC of the first eight data bytes from the scratchpad and compares the calculated CRC with the read CRC (byte 9). If they match, the master continues; if not, the read operation is repeated.|
|Tx|Reset|Master issues reset pulse.|
|Rx|Presence|DS18B20 responds with presence pulse.|
|Tx|CCh|Master issues Skip ROM command.|
|Tx|48h|Master issues Copy Scratchpad command.|
|Tx|DQ line held high by strong pullup|Master applies strong pullup to DQ for at least 10ms while copy operation is in progress.|


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

**Ordering Information**

**PART** **TEMP RANGE** **PIN-PACKAGE** **TOP MARK**

DS18B20 -55°C to +125°C 3 TO-92 18B20

DS18B20+ -55°C to +125°C 3 TO-92 18B20

DS18B20/T&R -55°C to +125°C 3 TO-92 (2000 Piece) 18B20

DS18B20+T&R -55°C to +125°C 3 TO-92 (2000 Piece) 18B20

DS18B20-SL/T&R -55°C to +125°C 3 TO-92 (2000 Piece)* 18B20

DS18B20-SL+T&R -55°C to +125°C 3 TO-92 (2000 Piece)* 18B20

DS18B20U -55°C to +125°C 8 FSOP 18B20

DS18B20U+ -55°C to +125°C 8 FSOP 18B20

DS18B20U/T&R -55°C to +125°C 8 FSOP (3000 Piece) 18B20

DS18B20U+T&R -55°C to +125°C 8 FSOP (3000 Piece) 18B20

DS18B20Z -55°C to +125°C 8 SO DS18B20

DS18B20Z+ -55°C to +125°C 8 SO DS18B20

DS18B20Z/T&R -55°C to +125°C 8 SO (2500 Piece) DS18B20

DS18B20Z+T&R -55°C to +125°C 8 SO (2500 Piece) DS18B20


_+Denotes a lead-free package. A “+” will appear on the top mark of lead-free packages._

_T&R = Tape and reel._

*TO-92 packages in tape and reel can be ordered with straight or formed leads. Choose “SL” for straight leads. Bulk TO-92 orders
_are straight leads only._


-----

# DS18B20 Programmable Resolution 1-Wire Digital Thermometer

**Revision History**

|REVISION DATE|DESCRIPTION|PAGES CHANGED|
|---|---|---|
|3/1/07|In the Absolute Maximum Ratings section, removed the reflow oven temperature value of +220°C. Reference to JEDEC specification for reflow remains.|19|
|10/12/07|In the Operation—Alarm Signaling section, added “or equal to” in the description for a TH alarm condition|5|
||In the Memory section, removed incorrect text describing memory.|7|
||In the Configuration Register section, removed incorrect text describing configuration register.|8|
|4/22/08|In the Ordering Information table, added TO-92 straight-lead packages and included a note that the TO-92 package in tape and reel can be ordered with either formed or straight leads.|2|
|1/15|Updated Benefits and Features section|1|
|09/18|Updated DC Electrical Characteristics table|2|
|7/19|Updated Figure 12|10|



For pricing, delivery, and ordering information, please visit Maxim Integrated’s online storefront at https://www.maximintegrated.com/en/storefront/storefront.html.

_Maxim Integrated cannot assume responsibility for use of any circuitry other than circuitry entirely embodied in a Maxim Integrated product. No circuit patent licenses_
_are implied. Maxim Integrated reserves the right to change the circuitry and specifications without notice at any time. The parametric values (min and max limits)_
_shown in the Electrical Characteristics table are guaranteed. Other parametric values quoted in this data sheet are provided for guidance._


-----

