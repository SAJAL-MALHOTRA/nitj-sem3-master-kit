# COMPUTER SYSTEM ARCHITECTURE (ITDC0209 / ITPC-209)
## ULTIMATE ENDTERM EXAMINATION THEORY MASTER BOOK
### Complete, Exhaustive Academic Course Notes & Practical Guide

---

> **Course Level**: Undergraduate B.Tech (Semester 3)  
> **Course Code**: ITDC0209 / ITPC-209  
> **Credit Scheme**: 3-1-0-4  
> **Primary References**:  
> 1. M. Morris Mano, *Computer System Architecture*, 3rd Edition, Pearson.  
> 2. David A. Patterson & John L. Hennessy, *Computer Organization and Design: The Hardware/Software Interface*, 6th Edition, Morgan Kaufmann.  
> 3. William Stallings, *Computer Organization and Architecture: Designing for Performance*, 11th Edition, Pearson.  
> 4. Ramesh S. Gaonkar, *Microprocessor Architecture, Programming, and Applications with the 8085*, 6th Edition, Penram.

---

## MASTER TABLE OF CONTENTS

1. [UNIT 1: INTRODUCTION, DATA REPRESENTATION, BUSES, AND RTL](#unit-1-introduction-data-representation-buses-and-rtl)
   - 1.1 Number Systems, Radix Conversions, and Precision Limits
   - 1.2 Fixed-Point Representation and Signed Arithmetic
   - 1.3 Floating-Point Representation and IEEE 754 Standard (Single & Double Precision)
   - 1.4 Error Detection & Correction: Hamming Codes & SECDED
   - 1.5 Digital Computer Generations, Architectural Classifications, and Types
   - 1.6 Functional Units, Stored-Program Concept, and Register Interconnections
   - 1.7 System Buses, Timing Protocols, and Bus Arbitration Schemes
   - 1.8 Register Transfer Language (RTL), Tri-State Buffers, and Memory Transfers
   - 1.9 Unit 1 High-Probability Exam Questions & Step-by-Step Solutions
   - 1.10 Unit 1 Common Traps, Pitfalls, and Concept Checks

2. [UNIT 2: CENTRAL PROCESSING UNIT & COMPUTER ARITHMETIC](#unit-2-central-processing-unit--computer-arithmetic)
   - 2.1 Addition and Subtraction Hardware: Ripple Carry vs Look-Ahead Carry Adders
   - 2.2 2's Complement Adder-Subtractor Circuit & Overflow Detection
   - 2.3 Multiplication Algorithms: Unsigned Array Multiplier & Booth's Signed Multiplication (Radix-2 & Radix-4)
   - 2.4 Division Algorithms: Restoring and Non-Restoring Division
   - 2.5 Floating-Point Arithmetic Operations (Addition, Subtraction, Multiplication, Division)
   - 2.6 Processor Organization & General Register Organization (Control Word Architecture)
   - 2.7 Stack Organization: Register Stack vs Memory Stack & RPN Evaluation
   - 2.8 Addressing Modes: Exhaustive Analysis, Effective Address (EA) Derivations, and Comprehensive Numericals
   - 2.9 Unit 2 High-Probability Exam Questions & Step-by-Step Solutions
   - 2.10 Unit 2 Common Traps, Pitfalls, and Concept Checks

3. [UNIT 3: CONTROL UNIT DESIGN & MICROPROGRAMMING](#unit-3-control-unit-design--microprogramming)
   - 3.1 Instruction Formats and Types: 3-Address, 2-Address, 1-Address, and 0-Address Machines
   - 3.2 Instruction Cycle: Fetch, Decode, Effective Address Calculation, Execution, and Subcycles
   - 3.3 Register Transfer Level (RTL) Execution of Complete Instructions
   - 3.4 Hardwired Control Unit: Architecture, Timing Decoders, and Logic Synthesis
   - 3.5 Microprogrammed Control Unit: Architecture, Control Store, and Address Sequencing
   - 3.6 Microinstruction Design: Horizontal vs Vertical Microprogramming vs Nanoprogramming
   - 3.7 Advanced Control Unit Concepts: Wide Branch Addressing and Pre-Fetching Microinstructions
   - 3.8 Unit 3 High-Probability Exam Questions & Step-by-Step Solutions
   - 3.9 Unit 3 Common Traps, Pitfalls, and Concept Checks

4. [UNIT 4: MEMORY SYSTEM ORGANIZATION & CACHE ARCHITECTURE](#unit-4-memory-system-organization--cache-architecture)
   - 4.1 Memory Hierarchy, Technological Bottlenecks, and Locality of Reference
   - 4.2 Semiconductor RAM Memories: 6T SRAM vs 1T-1C DRAM & Dynamic Refreshing
   - 4.3 Internal Memory Organization: 2D vs 2.5D Coincident Decoding Architecture
   - 4.4 Read-Only Memories (ROM, PROM, EPROM, EEPROM, Flash NOR/NAND)
   - 4.5 Cache Memory Architecture: Performance Metrics, Hit Ratio, and AMAT Formulation
   - 4.6 Cache Mapping Techniques: Direct, Associative, and Set-Associative (Bit Field Derivations & Numericals)
   - 4.7 Cache Replacement Algorithms (LRU, FIFO, LFU, Random) and Write Policies (Write-Through vs Write-Back)
   - 4.8 Auxiliary and Secondary Storage: Magnetic Disks (HDD Latency Numericals), Tapes, and Optical Storage
   - 4.9 Virtual Memory: Paging, Page Tables, Address Translation, TLB, EMAT, and Page Fault Handling
   - 4.10 Segmentation vs Paging Comparative Analysis
   - 4.11 Unit 4 High-Probability Exam Questions & Step-by-Step Solutions
   - 4.12 Unit 4 Common Traps, Pitfalls, and Concept Checks

5. [UNIT 5: INPUT / OUTPUT ORGANIZATION & PERIPHERALS](#unit-5-input--output-organization--peripherals)
   - 5.1 Peripheral Devices, I/O Interface Architecture, and Handshaking Protocols
   - 5.2 Isolated I/O (Port-Mapped) vs Memory-Mapped I/O Architectural Comparison
   - 5.3 Modes of Data Transfer: Programmed I/O, Interrupt-Initiated I/O, and Direct Memory Access (DMA)
   - 5.4 DMA Controller Architecture, Operating Modes (Burst, Cycle Stealing, Transparent), and Bus Protocols
   - 5.5 Interrupt System: Hardware Polling, Daisy-Chained Priority, and Vectored Priority Controllers (8259A)
   - 5.6 Types of Interrupts: External, Internal (Traps/Exceptions), and Software Interrupts
   - 5.7 I/O Channels and Independent I/O Processors (IOP)
   - 5.8 Serial Communication: Asynchronous (UART Framing) vs Synchronous Communication, Baud Rate, and Standards (RS-232, USB)
   - 5.9 Unit 5 High-Probability Exam Questions & Step-by-Step Solutions
   - 5.10 Unit 5 Common Traps, Pitfalls, and Concept Checks

6. [COMPLETE EXECUTABLE C++ HARDWARE ALGORITHM SIMULATORS](#complete-executable-c-hardware-algorithm-simulators)
   - 6.1 Booth's Multiplication Simulator with Step-by-Step Binary Traces
   - 6.2 Restoring Division Simulator with Accumulator/Quotient Register Visualizer
   - 6.3 Non-Restoring Division Simulator
   - 6.4 IEEE 754 Floating-Point Converter & Special Value Inspector
   - 6.5 Cache Memory Mapping & AMAT Performance Calculator

7. [MASTER COMPARATIVE ARCHITECTURAL TABLES & FORMULA CHEAT SHEET](#master-comparative-architectural-tables--formula-cheat-sheet)

---

# UNIT 1: INTRODUCTION, DATA REPRESENTATION, BUSES, AND RTL

---

## 1.1 NUMBER SYSTEMS, RADIX CONVERSIONS, AND PRECISION LIMITS

### 1.1.1 Positional Number Representation
In digital computation, numbers are expressed in positional notation with base (radix) $r$:
$$N = \sum_{i=-m}^{n-1} d_i \cdot r^i = d_{n-1} r^{n-1} + \dots + d_1 r^1 + d_0 r^0 + d_{-1} r^{-1} + \dots + d_{-m} r^{-m}$$
where:
- $r$ is the radix or base ($r \in \{2, 8, 10, 16\}$).
- $d_i$ are digits such that $0 \le d_i < r$.
- $n$ is the number of integer digits, and $m$ is the number of fractional digits.
- The radix point separates the integer power terms ($i \ge 0$) from the negative power terms ($i < 0$).

### 1.1.2 Radix Conversion Algorithms
1. **Integer Part Conversion (Base 10 to Base $r$)**:
   - **Repeated Division by $r$**: Divide the decimal integer by $r$, record the integer quotient and the remainder.
   - Continue dividing the successive quotients by $r$ until the quotient is $0$.
   - Read the remainders from bottom to top (the first remainder generated is the Least Significant Digit $d_0$; the final remainder is the Most Significant Digit $d_{n-1}$).

2. **Fractional Part Conversion (Base 10 to Base $r$)**:
   - **Repeated Multiplication by $r$**: Multiply the fractional part by $r$.
   - Extract the resulting integer part as the next fractional digit ($d_{-1}, d_{-2}, \dots$).
   - Multiply the remaining fractional part by $r$ and repeat until the fraction becomes exactly $0$ or the desired precision limit is reached.
   - Read the extracted integer digits from top to bottom.

```
Example: Convert Decimal 55.875 to Binary (Radix 2)

Step 1: Integer Part (55)
  55 / 2 = 27  Remainder 1 (LSB: d0)
  27 / 2 = 13  Remainder 1 (d1)
  13 / 2 = 6   Remainder 1 (d2)
   6 / 2 = 3   Remainder 0 (d3)
   3 / 2 = 1   Remainder 1 (d4)
   1 / 2 = 0   Remainder 1 (MSB: d5)
  Result: 55_10 = 110111_2

Step 2: Fractional Part (0.875)
  0.875 * 2 = 1.750  -> Integer: 1 (d-1)
  0.750 * 2 = 1.500  -> Integer: 1 (d-2)
  0.500 * 2 = 1.000  -> Integer: 1 (d-3)
  0.000 (Terminated)
  Result: 0.875_10 = 0.111_2

Final Combined Result: 55.875_10 = 110111.111_2
```

### 1.1.3 Octal and Hexadecimal Groupings
Because $8 = 2^3$ and $16 = 2^4$, conversions between binary, octal, and hexadecimal bypass decimal entirely by grouping bits:
- **Binary to Octal**: Group binary bits into sets of 3 bits, radiating outward from the radix point (pad with zeros to the left of the integer MSB and to the right of the fractional LSB). Replace each 3-bit group with its octal digit ($0-7$).
- **Binary to Hexadecimal**: Group binary bits into sets of 4 bits (nibbles) radiating outward from the radix point. Replace each 4-bit nibble with its hexadecimal digit ($0-9, \text{A}-\text{F}$).

```
Example: Convert 110111.111_2 to Hexadecimal:
  Integer Part:   0011 0111  -> 3 7_16
  Fractional Part: 1110      -> E_16  (padded with one 0 on the right)
  Result: 37.E_16
```

### 1.1.4 Non-Terminating Binary Fractions & Machine Precision
A decimal fraction can be represented as a finite terminating binary fraction if and only if its irreducible denominator has prime factors that are exclusively powers of $2$. 
Fractions such as $0.1_{10} = \frac{1}{10} = \frac{1}{2 \times 5}$ have a prime factor of $5$, resulting in an infinite repeating binary fraction:
$$0.1_{10} = 0.00011001100110011\dots_2 = 0.0\overline{0011}_2$$
In finite hardware registers, this truncation causes machine round-off error and representation drift.

---

## 1.2 FIXED-POINT REPRESENTATION AND SIGNED ARITHMETIC

Fixed-point numbers allocate a fixed number of bits to the integer part and a fixed number to the fractional part. In integer arithmetic, the binary point is assumed to lie immediately to the right of the least significant bit.

### 1.2.1 Comparison of Signed Integer Systems (n-bit words)

| Property | Signed Magnitude | 1's Complement | 2's Complement |
| :--- | :--- | :--- | :--- |
| **MSB Meaning** | Sign ($0=+, 1=-$) | Sign ($0=+, 1=-$) | Sign ($0=+, 1=-$) |
| **Magnitude Bits** | $n-1$ bits directly store $|N|$ | Inverted $|N|$ if negative | $2^n - N$ if negative |
| **Range (8-bit)** | $-127$ to $+127$ | $-127$ to $+127$ | $-128$ to $+127$ |
| **General Range** | $-(2^{n-1}-1)$ to $+(2^{n-1}-1)$ | $-(2^{n-1}-1)$ to $+(2^{n-1}-1)$ | $-2^{n-1}$ to $+(2^{n-1}-1)$ |
| **Zero Representation** | Dual: $+0$ (`00000000`), $-0$ (`10000000`) | Dual: $+0$ (`00000000`), $-0$ (`11111111`) | Unique: $+0$ (`00000000`) |
| **Arithmetic Hardware** | Complex (separate comparator/adder) | Adder requires End-Around Carry | Standard binary adder with 2's comp |
| **Asymmetric Range** | Symmetric | Symmetric | Asymmetric (extra negative number) |

### 1.2.2 1's Complement (Diminished Radix Complement)
The 1's complement of an $n$-bit binary number $N$ is defined formally as:
$$K_1 = (2^n - 1) - N$$
Operationally, subtracting any bit from $1$ yields its logical NOT ($1 - 0 = 1$, $1 - 1 = 0$). Hence, 1's complement is formed by bitwise inversion.
- **Addition Complication**: When adding two numbers in 1's complement, if a carry-out occurs from the sign bit, an **End-Around Carry** must be added back to the LSB. This requires two adder cycles, slowing down arithmetic.

### 1.2.3 2's Complement (Radix Complement)
The 2's complement of an $n$-bit binary number $N$ is defined formally as:
$$K_2 = 2^n - N = [(2^n - 1) - N] + 1 = \text{1's Complement}(N) + 1$$
Operationally, 2's complement is generated by:
1. Inverting all bits of $N$ and adding $1$ to the LSB.
2. **Fast Hardware Inspection Rule**: Scan the binary word from Right to Left (LSB toward MSB). Leave all bits unchanged up to and including the first `1`. Invert all subsequent bits to the left.

```
Example: Find the 8-bit 2's complement of +78 (01001110_2)
Method 1 (Invert and add 1):
  Invert bits: 10110001
  Add 1:       +       1
  Result:      10110010 (-78_10)

Method 2 (Scan Right to Left):
  Original:   0 1 0 0 1 1 1 0
  First '1':              1 0  (keep identical)
  Invert left:1 0 1 1 0 0      (invert 01001 -> 10110)
  Result:     1 0 1 1 0 0 1 0  (-78_10)
```

#### The Value of an n-bit 2's Complement Number
An $n$-bit 2's complement vector $B = b_{n-1} b_{n-2} \dots b_1 b_0$ represents the algebraic value:
$$V(B) = -b_{n-1} 2^{n-1} + \sum_{i=0}^{n-2} b_i 2^i$$
The MSB $b_{n-1}$ carries a negative weight $-2^{n-1}$. This mathematically explains why:
- If $b_{n-1} = 0$, the value is non-negative: $\sum_{i=0}^{n-2} b_i 2^i$.
- If $b_{n-1} = 1$, the value is negative.
- The maximum positive value occurs when $b_{n-1}=0$ and all other bits are $1$: $+2^{n-1} - 1$ ($+127$ for $n=8$).
- The minimum negative value occurs when $b_{n-1}=1$ and all other bits are $0$: $-2^{n-1}$ ($-128$ for $n=8$).

> **Important Asymmetry Trap**: In an 8-bit system, $-128 = 10000000_2$. Taking the 2's complement of $10000000$: invert $\to 01111111$, add $1 \to 10000000$. It returns to $-128$ because $+128$ cannot be represented in 8 bits! Attempting to negate $-128$ causes signed arithmetic overflow.

### 1.2.4 Sign Extension
When extending an $n$-bit signed number to an $m$-bit word ($m > n$):
- **Unsigned Extension (Zero Extension)**: Pad $m - n$ zeros to the left.
- **Signed 2's Complement Extension (Sign Extension)**: Replicate the sign bit ($b_{n-1}$) into all $m - n$ upper bit positions.
  $$\text{Value is preserved because: } -2^{n-1} = -2^m + \sum_{j=n-1}^{m-1} 2^j$$

```
Example:
  +45 in 8 bits:  00101101  -> In 16 bits: 00000000 00101101
  -45 in 8 bits:  11010011  -> In 16 bits: 11111111 11010011
```

### 1.2.5 2's Complement Subtraction & Carry vs Overflow
Subtraction is performed directly via addition:
$$A - B = A + (-B) = A + (\overline{B} + 1)$$
Any carry generated out of the MSB is **discarded** (it has an algebraic weight of $2^n \equiv 0 \pmod{2^n}$).

#### Carry-Out vs Arithmetic Overflow: The Critical Distinction
- **Carry-Out ($C_{out}$)**: Indicates that an unsigned addition generated a result that exceeds $2^n - 1$. In unsigned arithmetic, $C_{out} = 1$ denotes an overflow. In signed 2's complement arithmetic, $C_{out}$ is mathematically expected when adding negative numbers and is simply discarded.
- **Arithmetic Overflow ($V$)**: Indicates that the signed result exceeds the representable range $[-2^{n-1}, +2^{n-1}-1]$.

#### Rules Governing Signed Overflow:
1. Overflow can **ONLY** occur when adding two operands of the **SAME** algebraic sign:
   - $(+) + (+) \to (-)$ (Positive overflow)
   - $(-) + (-) \to (+)$ (Negative overflow)
2. Adding two numbers of opposite signs can **NEVER** overflow because the magnitude of the sum is strictly smaller than the larger magnitude operand:
   $$(+) + (-) \implies \text{No Overflow Possible}$$
3. **Hardware Overflow Logic**: Overflow occurs if and only if the carry into the sign bit ($C_{in}$) is different from the carry out of the sign bit ($C_{out}$):
   $$V = C_{in} \oplus C_{out}$$

#### Full Truth Table for Sign Bit Addition and Overflow Detection:

| $A_{n-1}$ (Sign A) | $B_{n-1}$ (Sign B) | $C_{in}$ (Carry into MSB) | Sum $S_{n-1}$ | $C_{out}$ (Carry out of MSB) | Overflow $V = C_{in} \oplus C_{out}$ | Condition Description |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | 0 | 0 | 0 | Pos + Pos = Pos (Correct) |
| 0 | 0 | 1 | 1 | 0 | **1** | Pos + Pos = Neg (**Overflow**) |
| 0 | 1 | 0 | 1 | 0 | 0 | Pos + Neg = Neg (Correct) |
| 0 | 1 | 1 | 0 | 1 | 0 | Pos + Neg = Pos (Correct) |
| 1 | 0 | 0 | 1 | 0 | 0 | Neg + Pos = Neg (Correct) |
| 1 | 0 | 1 | 0 | 1 | 0 | Neg + Pos = Pos (Correct) |
| 1 | 1 | 0 | 0 | 1 | **1** | Neg + Neg = Pos (**Overflow**) |
| 1 | 1 | 1 | 1 | 1 | 0 | Neg + Neg = Neg (Correct) |

```
ASCII Circuit: 2's Complement Overflow Detection Logic

            A[n-1] --------\
                           +----[ Full Adder Stage n-1 ]----+---- S[n-1] (Result Sign)
            B[n-1] --------/                                |
                                                            |
            C[in] ------------------------------------------+-------\
                                                                    (XOR) -----> Overflow Flag (V)
            C[out] -------------------------------------------------/
```

#### Worked Numerical Examples (8-bit signed 2's complement):

**Case 1: Addition with Overflow (+50 + +100 = +150)**
```
    (+50)   =  00110010
   +(+100)  =  01100100
  ---------------------
   Sum      =  10010110
  Carries:
    Into bit 7 (Cin)  = 1
    Out of bit 7 (Cout)= 0
  Sign bit of result is 1 (Negative). Adding two positives produced a negative!
  V = Cin XOR Cout = 1 XOR 0 = 1 (OVERFLOW OCCURRED).
  Mathematical result +150 > +127.
```

**Case 2: Subtraction without Overflow (+45 - +78 = -33)**
```
    A = +45 = 00101101
    B = +78 = 01001110  -> -B = 2's complement of 78 = 10110010
    Perform A + (-B):
       00101101 (+45)
     + 10110010 (-78)
     ----------
       11011111
  Carries:
    Into bit 7 (Cin)  = 0
    Out of bit 7 (Cout)= 0
  V = 0 XOR 0 = 0 (NO OVERFLOW).
  Verification of result: 11011111_2 is negative. 
  2's comp of 11011111: Invert -> 00100000, Add 1 -> 00100001 = 33_10.
  Result = -33_10. Correct!
```

---

## 1.3 FLOATING-POINT REPRESENTATION & IEEE 754 STANDARD

### 1.3.1 Principles of Floating-Point Representation
Real numbers in scientific notation are represented as:
$$N = (-1)^S \times M \times r^E$$
where:
- $S$ is the sign bit ($0 = \text{positive}, 1 = \text{negative}$).
- $M$ is the significand or mantissa.
- $r$ is the base ($r = 2$ in digital hardware).
- $E$ is the exponent determining the dynamic range.

### 1.3.2 Why Biased Exponent (Excess-K) is Used
In floating-point hardware, comparing two numbers requires determining which exponent is larger. If exponents were stored in 2's complement, negative exponents would have a leading `1` and positive exponents a leading `0`, preventing standard unsigned integer magnitude comparators from working directly.
By adding a fixed constant **Bias** to the true exponent $e$:
$$E = e + Bias$$
the stored exponent $E$ is always non-negative ($E \ge 0$). 
For an exponent field of $k$ bits:
$$Bias = 2^{k-1} - 1$$
- For single precision ($k = 8$): $Bias = 2^{8-1} - 1 = 127$.
- For double precision ($k = 11$): $Bias = 2^{11-1} - 1 = 1023$.
- For a custom format with $k = 10$ bits: $Bias = 2^{10-1} - 1 = 511$.

### 1.3.3 IEEE 754 Standard Formats

```
Single Precision (32-bit):
 0      1              8 9                                                     31
+------+----------------+-------------------------------------------------------+
| S(1) |  Exponent (8)  |                    Fraction (23)                      |
+------+----------------+-------------------------------------------------------+

Double Precision (64-bit):
 0      1                 11 12                                                63
+------+--------------------+---------------------------------------------------+
| S(1) |   Exponent (11)    |                    Fraction (52)                  |
+------+--------------------+---------------------------------------------------+
```

#### Detailed Format Specifications:

| Parameter | IEEE 754 Single Precision (Binary32) | IEEE 754 Double Precision (Binary64) |
| :--- | :--- | :--- |
| **Total Width** | 32 bits | 64 bits |
| **Sign Bit ($S$)** | 1 bit (bit 31) | 1 bit (bit 63) |
| **Exponent Bits ($k$)** | 8 bits (bits 30 to 23) | 11 bits (bits 62 to 52) |
| **Fraction Bits ($m$)** | 23 bits (bits 22 to 0) | 52 bits (bits 51 to 0) |
| **Exponent Bias** | 127 ($01111111_2$) | 1023 ($01111111111_2$) |
| **Normalized Exp Range ($E$)** | $1 \le E \le 254$ | $1 \le E \le 2046$ |
| **True Exp Range ($e$)** | $-126 \le e \le +127$ | $-1022 \le e \le +1023$ |
| **Normalized Value** | $(-1)^S \times (1.F) \times 2^{E - 127}$ | $(-1)^S \times (1.F) \times 2^{E - 1023}$ |
| **Subnormal Value** | $(-1)^S \times (0.F) \times 2^{-126}$ | $(-1)^S \times (0.F) \times 2^{-1022}$ |
| **Smallest Normalized Pos** | $1.0 \times 2^{-126} \approx 1.175 \times 10^{-38}$ | $1.0 \times 2^{-1022} \approx 2.225 \times 10^{-308}$ |
| **Smallest Subnormal Pos** | $2^{-23} \times 2^{-126} \approx 1.401 \times 10^{-45}$ | $2^{-52} \times 2^{-1022} \approx 4.94 \times 10^{-324}$ |
| **Largest Finite Pos** | $(2 - 2^{-23}) \times 2^{127} \approx 3.4028 \times 10^{38}$ | $(2 - 2^{-52}) \times 2^{1023} \approx 1.7977 \times 10^{308}$ |

### 1.3.4 The Implicit Leading Bit (Hidden Bit)
In binary, any non-zero normalized number has a leading significant bit of `1`:
$$N = 1.b_{-1} b_{-2} b_{-3} \dots \times 2^e$$
Since this leading bit is always guaranteed to be `1`, storing it in memory is redundant. IEEE 754 adopts the **Hidden Bit Convention**: the leading `1` is omitted from physical storage and implicitly restored by ALU hardware during execution. This yields 24 bits of effective precision while occupying only 23 bits of physical fraction storage.

### 1.3.5 Denormalized (Subnormal) Numbers & Gradual Underflow
When a computed result is smaller in magnitude than the smallest normalized number ($1.0 \times 2^{-126}$), traditional systems suffered from abrupt underflow, flushing the number directly to zero. This created a large representation gap between $0$ and $1.0 \times 2^{-126}$.
IEEE 754 solves this by defining **Denormalized (Subnormal) Numbers**:
- **Condition**: Exponent field $E = 0$ ($00000000_2$) AND Fraction field $F \neq 0$.
- **Hidden Bit Rule**: The implicit leading bit changes from `1` to `0` ($0.F$).
- **Fixed True Exponent**: The true exponent is locked to $1 - Bias = 1 - 127 = -126$ (NOT $0 - 127 = -127$).
- **Mathematical Value**:
  $$V = (-1)^S \times (0.F) \times 2^{-126}$$
This allows numbers to decrease smoothly down to $2^{-23} \times 2^{-126} = 2^{-149}$ before reaching true zero (**Gradual Underflow**).

### 1.3.6 IEEE 754 Special Values Encoding Table

| Stored Exponent ($E$) | Fraction ($F$) | Value Represented | Mathematical Meaning / Cause |
| :---: | :---: | :---: | :--- |
| $00000000_2$ ($0$) | $= 0$ | $\pm 0$ (Signed Zero) | Distinction needed for branch cuts, $1/(+0) = +\infty, 1/(-0) = -\infty$ |
| $00000000_2$ ($0$) | $\neq 0$ | Subnormal number | Gradual underflow: $(-1)^S \times (0.F) \times 2^{-126}$ |
| $00000001_2$ to $11111110_2$ ($1-254$) | Any | Normalized number | General real numbers: $(-1)^S \times (1.F) \times 2^{E - 127}$ |
| $11111111_2$ ($255$) | $= 0$ | $\pm \infty$ (Infinity) | Overflow or division by zero ($x / 0$) |
| $11111111_2$ ($255$) | $\neq 0$, MSB $= 1$ | Quiet NaN (QNaN) | Invalid operation ($0/0, \sqrt{-1}, \infty - \infty$); propagates silently |
| $11111111_2$ ($255$) | $\neq 0$, MSB $= 0$ | Signaling NaN (SNaN) | Invalid operation; raises immediate CPU trap/exception |

### 1.3.7 Step-by-Step Conversion Walkthroughs

#### Problem 1: Convert Decimal $-13.75$ to IEEE 754 Single Precision Hexadecimal
1. **Sign bit**: Negative number $\implies S = 1$.
2. **Convert magnitude $13.75$ to binary**:
   - $13_{10} = 1101_2$
   - $0.75_{10} = 0.11_2$
   - $13.75_{10} = 1101.11_2$
3. **Normalize binary representation**:
   $$1101.11_2 = 1.10111_2 \times 2^3$$
   True exponent $e = +3$.
4. **Compute biased exponent**:
   $$E = e + Bias = 3 + 127 = 130_{10} = 10000010_2$$
5. **Determine 23-bit Fraction field ($F$)**:
   - Normalized significand is $1.10111$.
   - Drop the implicit leading `1`: $F = 10111$.
   - Pad with zeros to 23 bits:
     $$F = 10111000000000000000000_2$$
6. **Assemble the 32-bit word**:
   - Bit 31 (S): `1`
   - Bits 30-23 (E): `10000010`
   - Bits 22-0 (F): `10111000000000000000000`
   - Full 32-bit string: `1 10000010 10111000000000000000000`
7. **Convert to Hexadecimal**:
   - Group into 4-bit nibbles: `1100 0001 0101 1100 0000 0000 0000 0000`
   - Hexadecimal: `0xC15C0000`

#### Problem 2: Convert Decimal $+0.125$ to IEEE 754 Single Precision Hexadecimal
1. **Sign bit**: Positive $\implies S = 0$.
2. **Convert magnitude $0.125$ to binary**:
   - $0.125 = \frac{1}{8} = 2^{-3} = 0.001_2$.
3. **Normalize binary representation**:
   $$0.001_2 = 1.0_2 \times 2^{-3}$$
   True exponent $e = -3$.
4. **Compute biased exponent**:
   $$E = -3 + 127 = 124_{10} = 01111100_2$$
5. **Determine 23-bit Fraction field**:
   - Fractional part after implicit `1` is $0$.
   - $F = 00000000000000000000000_2$.
6. **Assemble 32-bit binary**:
   - `0 01111100 00000000000000000000000`
   - Hexadecimal: `0011 1110 0000 0000 0000 0000 0000 0000` = `0x3E000000`.

#### Problem 3: Interpret IEEE 754 Single Precision Hexadecimal `0x40A00000` to Decimal
1. **Convert to 32-bit binary**:
   `0100 0000 1010 0000 0000 0000 0000 0000`
2. **Parse fields**:
   - $S = 0$ (Positive)
   - $E = 10000001_2 = 129_{10}$
   - $F = 01000000000000000000000_2 = 0.01_2$
3. **Compute true exponent and value**:
   - $e = E - 127 = 129 - 127 = 2$.
   - Significand $= 1 + 0.01_2 = 1 + 0.25 = 1.25$.
   - Algebraic value $= (+1) \times 1.25 \times 2^2 = 1.25 \times 4 = +5.0_{10}$.

---

## 1.4 ERROR DETECTION & CORRECTION: HAMMING CODES & SECDED

### 1.4.1 Principles of Parity
Parity bits append redundant check information to data words to detect bit corruption during transmission or memory storage:
- **Even Parity**: Total number of `1`s in the transmitted codeword (data + parity) must be even.
- **Odd Parity**: Total number of `1`s in the transmitted codeword must be odd.
- **Limitation**: Simple single-bit parity detects any odd number of bit errors (1, 3, 5...), but fails completely if an even number of bits (2, 4...) flip. It cannot locate the error bit.

### 1.4.2 Hamming Code Derivation & Parity Bit Positioning
Richard Hamming developed linear error-correcting codes where parity bits are positioned at powers of $2$ ($1, 2, 4, 8, \dots, 2^{r-1}$).

#### 1. Mathematical Inequality for Parity Bits ($r$):
To protect $m$ data bits with $r$ parity bits, the total codeword length is $n = m + r$. The $r$ parity bits generate $2^r$ unique syndrome combinations. Since the syndrome must distinguish between "no error" ($1$ state) and an error occurring in any of the $m + r$ bit positions ($m + r$ states):
$$2^r \ge m + r + 1$$

| Data Bits ($m$) | Min Parity Bits ($r$) | Total Codeword Length ($n = m + r$) | Check Inequality ($2^r \ge m+r+1$) |
| :---: | :---: | :---: | :--- |
| 1 | 2 | 3 | $2^2 = 4 \ge 1+2+1=4$ |
| 4 | 3 | 7 | $2^3 = 8 \ge 4+3+1=8$ (Hamming(7,4)) |
| 7 | 4 | 11 | $2^4 = 16 \ge 7+4+1=12$ |
| 8 | 4 | 12 | $2^4 = 16 \ge 8+4+1=13$ (Hamming(12,8)) |
| 16 | 5 | 21 | $2^5 = 32 \ge 16+5+1=22$ |
| 32 | 6 | 38 | $2^6 = 64 \ge 32+6+1=39$ |
| 64 | 7 | 71 | $2^7 = 128 \ge 64+7+1=72$ |

#### 2. Parity Bit Coverage Sets (1-Indexed):
Any bit position $i$ can be expressed as a unique sum of powers of $2$:
- Parity bit $P_1$ (Position $1 = 001_2$): Checks all bit positions whose binary index has a `1` in the least significant bit:
  $$\text{Positions } \{1, 3, 5, 7, 9, 11, \dots\}$$
- Parity bit $P_2$ (Position $2 = 010_2$): Checks all bit positions whose binary index has a `1` in the second bit:
  $$\text{Positions } \{2, 3, 6, 7, 10, 11, \dots\}$$
- Parity bit $P_4$ (Position $4 = 100_2$): Checks all bit positions whose binary index has a `1` in the third bit:
  $$\text{Positions } \{4, 5, 6, 7, 12, 13, \dots\}$$
- Parity bit $P_8$ (Position $8 = 1000_2$): Checks all bit positions whose binary index has a `1` in the fourth bit:
  $$\text{Positions } \{8, 9, 10, 11, 12, 13, 14, 15, \dots\}$$

### 1.4.3 Comprehensive Step-by-Step Worked Example (Hamming(7,4) Code)
Encode the 4-bit data word $D = 1011_2$ ($d_7 d_6 d_5 d_3$) using Even Parity Hamming Code.

```
Bit Mapping Table:
  Position:   1    2    3    4    5    6    7
  Designator: P1   P2   D3   P4   D5   D6   D7
  Data Value: ?    ?    1    ?    0    1    1
```

**Step 1: Calculate Parity Bits (Even Parity)**
- $P_1$ covers $\{1, 3, 5, 7\} \implies P_1 \oplus D_3 \oplus D_5 \oplus D_7 = 0$
  $$P_1 \oplus 1 \oplus 0 \oplus 1 = 0 \implies P_1 \oplus 0 = 0 \implies P_1 = 0$$
- $P_2$ covers $\{2, 3, 6, 7\} \implies P_2 \oplus D_3 \oplus D_6 \oplus D_7 = 0$
  $$P_2 \oplus 1 \oplus 1 \oplus 1 = 0 \implies P_2 \oplus 1 = 0 \implies P_2 = 1$$
- $P_4$ covers $\{4, 5, 6, 7\} \implies P_4 \oplus D_5 \oplus D_6 \oplus D_7 = 0$
  $$P_4 \oplus 0 \oplus 1 \oplus 1 = 0 \implies P_4 \oplus 0 = 0 \implies P_4 = 0$$

Transmitted Codeword: `0 1 1 0 0 1 1` (Bit positions 1 to 7).

**Step 2: Error Injection and Syndrome Calculation**
Assume noise corrupts bit position $5$ during transmission:
Received Codeword: `0 1 1 0 1 1 1` (Bit 5 flipped from `0` to `1`).

Evaluate check equations (Syndrome bits $C_4 C_2 C_1$):
- $C_1 = \text{Bits}(1, 3, 5, 7) = 0 \oplus 1 \oplus 1 \oplus 1 = 1$
- $C_2 = \text{Bits}(2, 3, 6, 7) = 1 \oplus 1 \oplus 1 \oplus 1 = 0$
- $C_4 = \text{Bits}(4, 5, 6, 7) = 0 \oplus 1 \oplus 1 \oplus 1 = 1$

Assembled Syndrome:
$$\text{Syndrome } S = C_4 C_2 C_1 = 101_2 = 5_{10}$$
The syndrome directly identifies the erroneous bit position! Bit $5$ is flipped to correct the error: $1 \to 0$. Codeword restored.

### 1.4.4 SECDED (Single Error Correction, Double Error Detection)
Standard Hamming code has a minimum Hamming distance $d_{min} = 3$. This allows single-bit error correction ($t = \lfloor(3-1)/2\rfloor = 1$). However, if a 2-bit error occurs, the standard syndrome misinterprets it as a single-bit error elsewhere and corrupts a valid bit!
**SECDED** adds an overall parity bit $P_0$ computed across all bits ($0$ to $n$):
- Minimum Hamming distance becomes $d_{min} = 4$.
- If Syndrome $S = 0$ and Overall Parity $P_0$ is correct: **No error**.
- If Syndrome $S \neq 0$ and Overall Parity $P_0$ is incorrect (odd): **Single-bit error corrected**.
- If Syndrome $S \neq 0$ and Overall Parity $P_0$ is correct (even): **Double-bit error detected** (uncorrectable; generates bus error/crash signal).

---

## 1.5 DIGITAL COMPUTER EVOLUTION & ARCHITECTURAL CLASSIFICATIONS

### 1.5.1 The Five Generations of Computers

| Generation | Era | Primary Switching Technology | Memory Technology | Operating System & Software | Characteristic Machines |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **First Generation** | 1940 - 1956 | **Vacuum Tubes** (Thermionic valves) | Mercury acoustic delay lines, Magnetic drums | Machine language, plugboards, paper tape/punched cards | ENIAC (18,000 tubes), EDVAC, UNIVAC-I, IBM 701 |
| **Second Generation** | 1956 - 1963 | **Discrete Transistors** (Bipolar Junction) | Magnetic ferrite core memories, magnetic tapes | Assembly language, early High-Level Languages (FORTRAN, COBOL), batch OS | IBM 1401, IBM 7090, CDC 1604 |
| **Third Generation** | 1964 - 1971 | **Integrated Circuits (IC)** (SSI & MSI logic) | Semiconductor RAM/ROM emergence, magnetic disks | Time-sharing OS, multiprogramming, standardized architectures | IBM System/360 family, DEC PDP-8 |
| **Fourth Generation** | 1971 - Present | **Microprocessors** (LSI, VLSI, ULSI) | Semiconductor DRAM/SRAM, flash memory, NVMe SSDs | Graphical User Interfaces (GUI), UNIX/Linux, Windows, distributed computing | Intel 4004/8086, Apple II, IBM PC, Modern x86-64 / ARM |
| **Fifth Generation** | Present & Future | **Ultra Large Scale Multi-core, AI Accelerators**, Quantum/Optical | High Bandwidth Memory (HBM3), 3D XPoint, Spin-Torque MRAM | Parallel OS, neural network compilers, autonomous computing systems | Google TPU, NVIDIA H100/B200, Cerebras Wafer-Scale |

### 1.5.2 Classification of Computers

1. **Microcomputers**:
   - Single microprocessor containing CPU on a single silicon die.
   - Lowest cost, personal workstations, laptops, embedded IoT systems.
   - Optimized for interactive human-computer interfaces and energy efficiency.
2. **Minicomputers (Mid-Range Systems)**:
   - Historical multi-user systems supporting 10 to 100 concurrent users.
   - Departmental computing, industrial automation (e.g., DEC VAX, HP 3000).
3. **Mainframe Computers**:
   - Engineered for massive enterprise transaction processing, extreme I/O bandwidth, and 99.999% availability (RAS: Reliability, Availability, Serviceability).
   - Capable of executing thousands of simultaneous disk/network transactions without CPU degradation (e.g., IBM z16).
4. **Supercomputers**:
   - Engineered for maximum floating-point computational throughput (FLOPS - Floating Point Operations Per Second).
   - Massively parallel architectures featuring thousands of heterogeneous compute nodes, vector processors, and high-speed inter-node switches (e.g., Frontier, Summit, Fugaku).

### 1.5.3 Flynn's Architectural Classification (Taxonomy)
Classifies computers based on the multiplicity of hardware instruction streams and data streams:
1. **SISD (Single Instruction, Single Data)**: Classic uniprocessor Von Neumann machine. Instructions executed sequentially on one data item at a time.
2. **SIMD (Single Instruction, Multiple Data)**: One instruction executes simultaneously across multiple data streams in lockstep (Vector processors, modern GPU compute units, AVX-512).
3. **MISD (Multiple Instruction, Single Data)**: Multiple instructions operate on a single data stream concurrently (Rare; used for fault-tolerant space flight computers and systolic arrays).
4. **MIMD (Multiple Instruction, Multiple Data)**: Multiple independent processors execute distinct instruction streams on distinct data sets (Multi-core CPUs, distributed clusters, cloud server farms).

---

## 1.6 FUNCTIONAL UNITS, STORED-PROGRAM CONCEPT, AND REGISTERS

### 1.6.1 Von Neumann vs Harvard Architectures

```
Von Neumann Architecture:
+-------------------------------------------------+
|                      CPU                        |
|  +------------------+    +-------------------+  |
|  |   Control Unit   |    |        ALU        |  |
|  +--------+---------+    +---------+---------+  |
|           |                        |            |
|  +--------+------------------------+---------+  |
|  |           Internal Registers              |  |
|  +--------------------+----------------------+  |
+-----------------------|-------------------------+
                        | Shared System Bus (Address, Data, Control)
+-----------------------+-------------------------+
|                    Memory                       |
|   (Shared: Program Instructions + Program Data) |
+-------------------------------------------------+

Harvard Architecture:
+-------------------------------------------------+
|                      CPU                        |
+-----------+-------------------------+-----------+
            | Instruction Bus         | Data Bus
+-----------+-----------+ +-----------+-----------+
|  Instruction Memory   | |      Data Memory      |
|  (Code / Read-Only)   | |      (Variables)      |
+-----------------------+ +-----------------------+
```

- **Von Neumann Architecture**: Single physical memory holds both instructions and data. Instructions and data share the same address and data buses.
  - **The Von Neumann Bottleneck**: Throughput is strictly bounded because the CPU cannot read an instruction and read/write operand data simultaneously in the same clock cycle.
- **Harvard Architecture**: Separate physical memories and independent buses for instructions and data. Allows simultaneous instruction fetch and operand read/write. Widely used in modern digital signal processors (DSPs) and L1 CPU caches (split instruction and data L1 caches).

### 1.6.2 Primary CPU Registers & Their Functional Roles

| Register | Name | Bit Width | Purpose & Operational Characteristics |
| :--- | :--- | :--- | :--- |
| **PC** | Program Counter | Address bus width ($k$) | Holds the memory address of the next instruction to be fetched. Automatically incremented during instruction fetch. |
| **MAR** | Memory Address Register | Address bus width ($k$) | Connected directly to the system address bus; holds the physical memory address currently being accessed for a read or write operation. |
| **MDR / MBR** | Memory Data Register | Data bus width ($m$) | Connected directly to the system data bus; acts as a two-way electrical buffer holding data fetched from memory or data waiting to be written to memory. |
| **IR** | Instruction Register | Instruction width | Holds the binary opcode and operand fields of the instruction currently being decoded and executed. |
| **AC** | Accumulator | Word width | General-purpose register that holds the intermediate results of ALU arithmetic and logical operations. |
| **TR** | Temporary Register | Word width | Internal CPU scratchpad register used to hold temporary operand values during microoperation sequencing. |

### 1.6.3 Basic Instruction Fetch Sequence (RTL Tracing)
The fundamental instruction fetch sequence executed at the beginning of every CPU cycle:
1. $T_0: \text{MAR} \leftarrow \text{PC}$  
   *(Copy next instruction address from PC to Memory Address Register)*
2. $T_1: \text{MDR} \leftarrow M[\text{MAR}], \quad \text{PC} \leftarrow \text{PC} + 1$  
   *(Read instruction from memory into MDR; concurrently increment PC)*
3. $T_2: \text{IR} \leftarrow \text{MDR}$  
   *(Transfer instruction opcode into IR for decoding)*

---

## 1.7 SYSTEM BUSES, TIMING PROTOCOLS, AND BUS ARBITRATION

### 1.7.1 Bus Definitions and Physical Characteristics
A **bus** is a shared set of electrical conductors that transmits signals between multiple computer functional modules.
The **System Bus** comprises three distinct functional groupings:

```
+--------------------------------------------------------------------------+
|                             CPU (Processor)                              |
+-------+--------------------------+-------------------------+-------------+
        | Address Lines            | Data Lines              | Control Lines
========+==========================+=========================+==============
========|==========================|=========================|============== (System Bus)
        | Address Bus              | Data Bus                | Control Bus
+-------+--------------------------+-------------------------+-------------+
|                          Main Memory (RAM)                               |
+--------------------------------------------------------------------------+
```

1. **Address Bus**:
   - **Directionality**: Unidirectional (CPU drives addresses outward to memory/peripherals).
   - **Width**: An address bus of $k$ bits can uniquely address $2^k$ distinct physical memory locations:
     $$\text{Addressable Locations} = 2^k$$
     *(e.g., a 32-bit address bus addresses $2^{32} = 4,294,967,296 \text{ bytes} = 4 \text{ GiB}$)*.
2. **Data Bus**:
   - **Directionality**: Bidirectional (carries data into CPU during Read, and out of CPU during Write).
   - **Width**: A data bus of $m$ bits transfers $m$ bits of data in a single bus cycle. It defines the word throughput of the architecture (e.g., 64-bit data bus transfers 8 bytes per clock edge).
3. **Control Bus**:
   - **Directionality**: Bidirectional / Individual unidirectional control lines.
   - **Function**: Transmits timing, synchronization, and command signals:
     - Memory Read (`MEMR`) & Memory Write (`MEMW`)
     - I/O Read (`IOR`) & I/O Write (`IOW`)
     - Clock (`CLK`) & Reset (`RST`)
     - Transfer Acknowledge / Ready (`READY`)
     - Bus Request (`BR`) & Bus Grant (`BG`)
     - Interrupt Request (`INTR`) & Interrupt Acknowledge (`INTA`)

### 1.7.2 Synchronous vs Asynchronous Bus Protocols

| Characteristic | Synchronous Bus | Asynchronous Bus |
| :--- | :--- | :--- |
| **Timing Reference** | Common shared bus clock line | No bus clock; uses **Handshaking signals** |
| **Control Signals** | Fixed clock edges govern transfer states | Request (`REQ`) and Acknowledge (`ACK`) lines |
| **Transfer Speed** | Very fast for short, matched-delay buses | Slower per cycle due to handshake round-trip |
| **Device Diversity** | Bound to the slowest device on the bus | Adapts dynamically to devices of arbitrary speeds |
| **Clock Skew Vulnerability** | High over long physical distances | Zero clock skew vulnerability |
| **Circuit Complexity** | Simple control logic | Complex asynchronous state-machine logic |

#### Asynchronous Full Handshaking Timing Protocol (Read Cycle):

```
Master (CPU)                         Slave (Memory)
   |                                       |
   |---- 1. Asserts Valid Address -------->|
   |---- 2. Asserts READ_REQ ------------->|
   |                                       | (Memory decodes address,
   |                                       |  accesses storage cell)
   |<--- 4. Drives DATA onto bus ----------|
   |<--- 3. Asserts ACK (Data Ready) ------|
   |                                       |
   | (CPU latches DATA into MDR)           |
   |---- 5. Deasserts READ_REQ ----------->|
   |                                       |
   |<--- 6. Deasserts ACK -----------------|
   |                                       |
   v                                       v
Cycle Complete                         Cycle Complete
```

### 1.7.3 Bus Arbitration Schemes
When multiple devices (Bus Masters: CPU, DMA Controller, GPU) request control of the shared system bus concurrently, **Bus Arbitration** selects exactly one master to drive the bus, preventing bus contention and electrical collisions.

#### 1. Daisy Chaining (Serial Priority Arbitration)

```
       +------------+
       |   Bus      |
       | Controller |
       +-----+------+
             | Bus Grant (BG)
             |
             v
      +--------------+      +--------------+      +--------------+
      | Bus Master 1 |----->| Bus Master 2 |----->| Bus Master 3 |
      | (Highest)    |  BG1 | (Medium)     |  BG2 | (Lowest)     |
      +-------+------+      +-------+------+      +-------+------+
              |                     |                     |
              +---------------------+---------------------+---- Common Bus Request (BR)
              |                     |                     |
              +---------------------+---------------------+---- Common Bus Busy (BUSY)
```

- **Mechanism**:
  - Any master requesting the bus pulls down the shared open-collector Bus Request line (`BR`).
  - The Bus Controller senses `BR` and asserts the Bus Grant signal (`BG`) to the first device in the chain (Master 1).
  - If Master 1 requested the bus, it intercepts `BG`, asserts `BUSY`, and takes control of the bus.
  - If Master 1 did not request the bus, it propagates `BG` down to Master 2, and so forth.
- **Architectural Trade-Offs**:
  - *Advantages*: Extremely low wire count (only 3 arbitration lines: `BR`, `BG`, `BUSY`); simple to extend by appending devices to the end of the chain.
  - *Disadvantages*:
    - **Fixed Priority**: Device 1 always wins; low-priority devices suffer from **Starvation**.
    - **Propagation Delay**: Grant propagation delay is proportional to the number of devices $O(N)$.
    - **Single Point of Failure**: An electrical failure or disconnect in Master 2 breaks the grant line for all subsequent devices.

#### 2. Polling (Rotating Priority Arbitration)

```
                   +------------------+
                   |  Bus Controller  |
                   +--------+---------+
                            | Poll Lines (k = ceil(log2 N))
            +---------------+---------------+
            |               |               |
            v               v               v
     +--------------+ +--------------+ +--------------+
     | Bus Master 0 | | Bus Master 1 | | Bus Master 2 |
     +-------+------+ +-------+------+ +-------+------+
             |                |                |
             +----------------+----------------+------ Common Bus Request (BR)
             |                |                |
             +----------------+----------------+------ Common Bus Busy (BUSY)
```

- **Mechanism**:
  - The controller senses an active `BR` line and generates a binary count on $k = \lceil \log_2 N \rceil$ poll lines.
  - When the count matches the ID of a requesting device, that device asserts `BUSY` and assumes bus ownership.
  - *Rotating Priority*: The controller can start the next poll sequence from the master immediately following the last granted master, implementing round-robin fairness.
- **Architectural Trade-Offs**:
  - *Advantages*: Eliminates device starvation; failure of an intermediate device does not disable the system; priority sequence is programmable.
  - *Disadvantages*: Slower response time (requires clock cycles to step through poll addresses); requires extra address lines ($k$ lines).

#### 3. Independent Request (Centralized Parallel Arbitration)

```
                   +-----------------------+
                   |  Central Arbiter      |
                   |  - Priority Resolver  |
                   |  - Priority Encoder   |
                   +---+----+----+----+----+
                       |    |    |    |
        +--------------+    |    |    +---------------+
        | BR1               | BG1| BG2                | BR2
        v                   v    v                    v
  +------------+                                +------------+
  |  Master 1  |                                |  Master 2  |
  +------------+                                +------------+
```

- **Mechanism**:
  - Every bus master possesses its own dedicated Bus Request (`BR_i`) and Bus Grant (`BG_i`) lines wired directly to the central arbiter.
  - The arbiter evaluates all active requests simultaneously using internal priority resolver hardware in a single clock cycle.
- **Architectural Trade-Offs**:
  - *Advantages*: Fastest possible arbitration speed ($O(1)$ constant time); fully dynamic priority reconfiguration (LRU, FIFO, Fixed, Fair share).
  - *Disadvantages*: Highest pin count and wiring overhead ($2N$ arbitration lines for $N$ devices); high arbiter circuit complexity.

---

## 1.8 REGISTER TRANSFER LANGUAGE (RTL), TRI-STATE BUFFERS, & TRANSFERS

### 1.8.1 Register Transfer Notation
Register Transfer Language (RTL) is a symbolic notation used to describe the microoperations, data paths, and control states of digital systems:
- $R2 \leftarrow R1$: Denotes simultaneous parallel copy of the contents of register $R1$ into register $R2$ on the active clock edge. The contents of source register $R1$ are unchanged (non-destructive read).
- Conditional Execution:
  $$P: R2 \leftarrow R1$$
  where $P$ is a boolean control signal. Hardware interprets this as:
  $$\text{Clock} \cdot P \implies \text{Load Enable of } R2 = 1$$

### 1.8.2 Common Bus Implementation: Multiplexers vs Tri-State Buffers
Wiring dedicated point-to-point connections between $n$ registers requires $n(n-1)$ direct lines, which is physically impossible on silicon chips. Systems use a **Common Bus**.

#### 1. Common Bus Using Multiplexers:
For $k$ registers of $n$ bits each, $n$ multiplexers of size $k$-to-$1$ are required. The select inputs ($S_1, S_0$) select which register is placed on the bus.

#### 2. Common Bus Using Three-State (Tri-State) Bus Buffers:
A **Tri-State Buffer** possesses three distinct output states:
1. Logic `0` (Low impedance)
2. Logic `1` (Low impedance)
3. **High-Impedance ($Hi-Z$)**: The output acts as an open circuit (disconnected).

```
Tri-State Buffer Symbol & Truth Table:

        Input (A) -------->|------- Output (Y)
                           |
                     Enable (E)

        +---+---+--------+
        | E | A | Output |
        +---+---+--------+
        | 0 | X |  Hi-Z  | (Disconnected)
        | 1 | 0 |   0    | (Driven Low)
        | 1 | 1 |   1    | (Driven High)
        +---+---+--------+
```

```
ASCII Circuit: 4-Register Common Bus via Tri-State Buffers and 2-to-4 Decoder

   Select S1, S0 ---->[ 2-to-4 Decoder ]
                             |  |  |  |
                 E0 ---------+  |  |  |
                 E1 ------------+  |  |
                 E2 ---------------+  |
                 E3 ------------------+

   Register A ---->[ Tri-State Buffer 0 (E0) ]--\
   Register B ---->[ Tri-State Buffer 1 (E1) ]---+
   Register C ---->[ Tri-State Buffer 2 (E2) ]---+=====> COMMON BUS LINES
   Register D ---->[ Tri-State Buffer 3 (E3) ]--/
```
The 2-to-4 decoder guarantees that **strictly one** tri-state buffer is enabled ($E = 1$) at any instant, while all other three buffers remain in high-impedance ($Hi-Z$). This completely eliminates bus contention and allows hundreds of components to share the same physical wires.

### 1.8.3 Memory Transfer Microoperations
1. **Memory Read Operation**:
   $$\text{Read}: \text{DR} \leftarrow M[\text{AR}]$$
   - Hardware sequence: The CPU places the memory address into the Address Register ($	ext{AR}$), applies it to the Address Bus, asserts the $\text{READ}$ control signal, and the memory places the stored data onto the Data Bus, where it is clocked into the Data Register ($	ext{DR}$). Non-destructive operation.
2. **Memory Write Operation**:
   $$\text{Write}: M[\text{AR}] \leftarrow R1$$
   - Hardware sequence: The CPU places the target address into $	ext{AR}$ (Address Bus), places the data from $R1$ onto the Data Bus, and asserts the $\text{WRITE}$ control signal. Memory circuits write the bits into the storage cells, destructively overwriting previous contents.

---

## 1.9 UNIT 1 HIGH-PROBABILITY EXAM QUESTIONS & STEP-BY-STEP SOLUTIONS

### Q1: In an 8-bit 2's complement system, perform $(+50) + (+100)$ and detect if signed overflow occurs using hardware logic.
**Solution**:
1. Convert to 8-bit binary:
   - $+50 = 00110010_2$
   - $+100 = 01100100_2$
2. Perform binary addition:
   ```
     Carry:  0 1 1 0 0 0 0 0
             0 0 1 1 0 0 1 0  (+50)
           + 0 1 1 0 0 1 0 0  (+100)
           -----------------
             1 0 0 1 0 1 1 0
   ```
3. Evaluate Carries and Flags:
   - Carry into MSB ($C_{in}$) = $1$
   - Carry out of MSB ($C_{out}$) = $0$
   - Hardware Overflow: $V = C_{in} \oplus C_{out} = 1 \oplus 0 = 1$ (**Overflow Detected**).
   - Reason: Two positive operands yielded a negative sign bit ($1$). Mathematical value $+150 > +127$.

### Q2: Derive the IEEE 754 single-precision floating-point representation for $-0.125$.
**Solution**:
1. Sign: Negative $\implies S = 1$.
2. Magnitude: $0.125 = 2^{-3} = 1.0_2 \times 2^{-3}$.
3. Biased Exponent: $E = e + 127 = -3 + 127 = 124 = 01111100_2$.
4. Fraction: Normalized significand is $1.0 \implies F = 00000000000000000000000_2$.
5. Assembly: `1 01111100 00000000000000000000000` = `0xBE000000`.

### Q3: Determine the number of parity bits required for 64 data bits under Hamming code.
**Solution**:
Apply $2^r \ge m + r + 1$ with $m = 64$:
- Try $r = 6$: $2^6 = 64 \ge 64 + 6 + 1 = 71$ (False: $64 < 71$).
- Try $r = 7$: $2^7 = 128 \ge 64 + 7 + 1 = 72$ (True: $128 \ge 72$).
Conclusion: Exactly **7 parity bits** are required (Total codeword = 71 bits).

### Q4: Compare Daisy Chaining and Independent Request bus arbitration across speed, line complexity, and fault tolerance.
**Solution**:
- **Speed**: Daisy chaining is slow ($O(N)$ propagation delay); Independent request is ultra-fast ($O(1)$ single-cycle arbitration).
- **Line Complexity**: Daisy chaining requires only 3 lines total; Independent request requires $2N$ dedicated lines.
- **Fault Tolerance**: Daisy chaining fails if any single intermediate node breaks; Independent request isolates faulty masters without impacting others.

---

## 1.10 UNIT 1 COMMON TRAPS, PITFALLS, AND CONCEPT CHECKS

> [!CAUTION]
> **Trap 1: Confusing Carry-Out with Overflow!**  
> In 2's complement, a carry out of the MSB ($C_{out} = 1$) does NOT imply an overflow! Discard $C_{out}$ in signed addition. Overflow occurs **only** when $C_{in} \oplus C_{out} = 1$ or when two numbers of identical sign yield a result of the opposite sign.

> [!WARNING]
> **Trap 2: Stored Exponent $E = 255$ is Not a Finite Exponent!**  
> In IEEE 754 single precision, $E = 255$ ($11111111_2$) is strictly reserved for Infinity ($F = 0$) and NaN ($F \neq 0$). The maximum representable finite normalized exponent is $E = 254$ ($e = 127$).

> [!IMPORTANT]
> **Trap 3: Tri-State Bus vs Multiplexer Bus!**  
> A multiplexer bus selects inputs internally through logic gates and cannot be physically bidirectional. A tri-state bus directly disconnects unused drivers into a high-impedance ($Hi-Z$) open circuit, allowing bidirectional transmission over identical copper traces.

# UNIT 2: CENTRAL PROCESSING UNIT & COMPUTER ARITHMETIC

---

## 2.1 ADDITION & SUBTRACTION HARDWARE: RIPPLE CARRY VS LOOK-AHEAD CARRY

### 2.1.1 Full Adder Logic & Ripple Carry Adder (RCA)
A **Full Adder (FA)** adds three single-bit inputs: operand bits $A_i, B_i$ and carry-in $C_i$.
- **Boolean Formulations**:
  $$S_i = A_i \oplus B_i \oplus C_i$$
  $$C_{i+1} = A_i B_i + C_i (A_i \oplus B_i) = A_i B_i + B_i C_i + A_i C_i$$

```
Truth Table for Full Adder:
+-----+-----+-------+-------+---------+
| A_i | B_i | C_i   |  S_i  | C_{i+1} |
+-----+-----+-------+-------+---------+
|  0  |  0  |   0   |   0   |    0    |
|  0  |  0  |   1   |   1   |    0    |
|  0  |  1  |   0   |   1   |    0    |
|  0  |  1  |   1   |   0   |    1    |
|  1  |  0  |   0   |   1   |    0    |
|  1  |  0  |   1   |   0   |    1    |
|  1  |  1  |   0   |   0   |    1    |
|  1  |  1  |   1   |   1   |    1    |
+-----+-----+-------+-------+---------+
```

#### Ripple Carry Adder Delay Analysis:
In an $n$-bit Ripple Carry Adder, $n$ full adders are cascaded such that the carry-out of stage $i$ feeds directly into the carry-in of stage $i+1$:

```
4-Bit Ripple Carry Adder Architecture:
           A3  B3             A2  B2             A1  B1             A0  B0
            |   |              |   |              |   |              |   |
            v   v              v   v              v   v              v   v
        +-----------+      +-----------+      +-----------+      +-----------+
C4 <----+   FA 3    |<-----+   FA 2    |<-----+   FA 1    |<-----+   FA 0    |<---- C0
        +-----+-----+  C3  +-----+-----+  C2  +-----+-----+  C1  +-----+-----+
              |                  |                  |                  |
              v                  v                  v                  v
              S3                 S2                 S1                 S0
```

- **Propagation Delay Formulation**:
  Let $\Delta$ be the unit gate delay of a 2-input gate (AND/OR/XOR):
  - Generation of $S_i$ requires $2$ gate delays ($A_i \oplus B_i$, then $\oplus C_i$).
  - Generation of carry $C_{i+1}$ from $C_i$ requires $2$ gate delays (AND gate followed by OR gate).
  - For $n$ bits, carry must ripple through all $n$ stages sequentially:
    $$T_{\text{carry}} = 2n \cdot \Delta$$
    $$T_{\text{total}} = 2n \cdot \Delta$$
  For a 32-bit RCA, $T = 2(32)\Delta = 64\Delta$. This linear dependency $O(n)$ creates a severe speed bottleneck in high-frequency ALUs.

---

### 2.1.2 Carry Look-Ahead Adder (CLA)
The Carry Look-Ahead Adder eliminates the serial carry ripple by calculating all carry bits in parallel directly from the input operands.

#### 1. Mathematical Derivation:
Define two intermediate signals for each bit stage $i$:
1. **Carry Generate ($G_i$)**: A carry is generated internally if both inputs are `1`, independent of carry-in:
   $$G_i = A_i \cdot B_i$$
2. **Carry Propagate ($P_i$)**: An incoming carry will propagate through stage $i$ if at least one input is `1`:
   $$P_i = A_i \oplus B_i \quad (\text{or algebraically } A_i + B_i)$$

The carry-out of stage $i$ is:
$$C_{i+1} = G_i + P_i C_i$$

#### 2. Recursive Carry Expansions for a 4-Bit CLA:
Expanding $C_i$ successively:
- Stage 0:
  $$C_1 = G_0 + P_0 C_0$$
- Stage 1:
  $$C_2 = G_1 + P_1 C_1 = G_1 + P_1(G_0 + P_0 C_0) = G_1 + P_1 G_0 + P_1 P_0 C_0$$
- Stage 2:
  $$C_3 = G_2 + P_2 C_2 = G_2 + P_2 G_1 + P_2 P_1 G_0 + P_2 P_1 P_0 C_0$$
- Stage 3:
  $$C_4 = G_3 + P_3 C_3 = G_3 + P_3 G_2 + P_3 P_2 G_1 + P_3 P_2 P_1 G_0 + P_3 P_2 P_1 P_0 C_0$$

Notice that **every carry bit ($C_1, C_2, C_3, C_4$) depends ONLY on the original inputs ($A_i, B_i$) and the initial carry-in $C_0$**! All carries are evaluated simultaneously in two levels of logic.

```
ASCII Logic Diagram: 4-Bit Carry Look-Ahead Generator

     C0 ----------------------------------------+------------------+------------------+
                                                |                  |                  |
     G0, P0 ------------------+                 |                  |                  |
                              v                 v                  |                  |
                         +--------------------------+              |                  |
                         | Carry Logic for C1       |              |                  |
                         | C1 = G0 + P0*C0          |              |                  |
                         +------------+-------------+              |                  |
                                      |                            |                  |
                                      +======> C1                  v                  |
     G1, P1 ------------------------------------+             +--------------------------+
                                                v             | Carry Logic for C3       |
                                           +---------+        | C3 = G2 + P2*G1 +        |
                                           | C2 Logic|======> |      P2*P1*G0 +          |
                                           +---------+   C2   |      P2*P1*P0*C0         |
     G2, P2 ------------------------------------------------->+------------+-------------+
                                                                            |
                                                                            +======> C3
     G3, P3 --------------------------------------------------------------------+
                                                                                v
                                                                      +--------------------+
                                                                      | Carry Logic for C4 |===> C4
                                                                      +--------------------+
```

#### 3. Delay Analysis: CLA vs Ripple Carry Adder
- Generation of all $P_i, G_i$: $1\Delta$ gate delay.
- Generation of all carries ($C_1$ to $C_4$) via 2-level AND-OR logic: $2\Delta$ gate delays.
- Generation of Sum bits ($S_i = P_i \oplus C_i$): $1\Delta$ gate delay.
- **Total 4-Bit CLA Delay**:
  $$T_{\text{CLA}} = 1\Delta + 2\Delta + 1\Delta = 4\Delta$$
  The total delay is constant ($4\Delta$), completely independent of $n$ for that block!

#### 4. Hardware Limitations (Fan-In / Fan-Out Bottleneck):
As word length grows, the gate for $C_n$ requires an AND gate with $n+1$ inputs and an OR gate with $n+1$ inputs. In physical CMOS silicon, logic gates with fan-in $> 4$ or $5$ suffer severe RC propagation delays and voltage degradation. 
Therefore, large adders (32-bit, 64-bit) are constructed as **Hierarchical / Multilevel Carry Look-Ahead Adders** (e.g., eight 4-bit CLA blocks linked by a Block Look-Ahead Carry Generator).

---

## 2.2 2'S COMPLEMENT ADDER-SUBTRACTOR CIRCUIT & OVERFLOW

A single unified combinational circuit performs both signed addition and signed subtraction using controlled XOR inverters.

```
ASCII Schematic: 4-Bit Adder-Subtractor Unit with Overflow Detection

              Mode Control (M: 0=Add, 1=Subtract)
               |
               +----------------------+--------------------+--------------------+
               |                      |                    |                    |
               |       B3             |       B2           |       B1           |       B0
               |        |             |        |           |        |           |        |
               v        v             v        v           v        v           v        v
             +------------+         +------------+       +------------+       +------------+
             |    XOR     |         |    XOR     |       |    XOR     |       |    XOR     |
             +-----+------+         +-----+------+       +-----+------+       +-----+------+
                   |                      |                    |                    |
             A3    |                A2    |              A1    |              A0    |
              |    |                 |    |               |    |               |    |
              v    v                 v    v               v    v               v    v
            +--------+             +--------+           +--------+           +--------+
            |  FA 3  |<------------|  FA 2  |<----------|  FA 1  |<----------|  FA 0  |<--- M (Cin)
            +---+----+   C3        +---+----+   C2      +---+----+   C1      +---+----+
                |  |                   |                    |                    |
         C4 <---+  |                   |                    |                    |
         |         v                   v                    v                    v
         |         S3                  S2                   S1                   S0
         |
         +---------\
                    (XOR) ======> Overflow Flag (V = C4 XOR C3)
         C3 --------/
```

- **Mode Operation**:
  - **Addition ($M = 0$)**:
    - Each XOR gate computes $B_i \oplus 0 = B_i$.
    - Initial carry-in $C_0 = M = 0$.
    - The circuit computes $A + B + 0 = A + B$.
  - **Subtraction ($M = 1$)**:
    - Each XOR gate computes $B_i \oplus 1 = \overline{B}_i$ (1's complement of $B$).
    - Initial carry-in $C_0 = M = 1$.
    - The circuit computes $A + \overline{B} + 1 = A + (-B) = A - B$ (2's complement subtraction).
- **Overflow Detection**:
  $$V = C_n \oplus C_{n-1} = C_4 \oplus C_3$$
  If $V = 1$, an arithmetic overflow has occurred, setting the processor status register overflow flag.

---

## 2.3 MULTIPLICATION ALGORITHMS

### 2.3.1 Unsigned Array Multiplier
For two unsigned 4-bit numbers $A = a_3 a_2 a_1 a_0$ and $B = b_3 b_2 b_1 b_0$:
- 16 partial product bits are generated concurrently using 16 AND gates: $P_{ij} = a_i \cdot b_j$.
- An array of cascaded Adders (Half Adders and Full Adders) sums the partial products in a 2-dimensional grid.
- **Hardware Cost**: For an $m \times n$ array multiplier:
  - $m \times n$ AND gates.
  - $n(m - 2)$ Full Adders and $n$ Half Adders.
  - Critical path delay: $O(m + n)$.

---

### 2.3.2 Booth's Signed Multiplication Algorithm (Radix-2)

#### 1. Mathematical Foundation:
Traditional shift-and-add algorithms require $n$ additions for a multiplier containing $n$ ones. In 2's complement, a sequence of consecutive `1`s from position $m$ to position $k$ ($k > m$) represents:
$$2^k + 2^{k-1} + \dots + 2^{m+1} + 2^m = 2^{k+1} - 2^m$$
Booth's algorithm replaces the $k - m + 1$ additions with **one subtraction** at the lowest-order `1` (transition from `0` to `1`) and **one addition** at the bit position following the highest-order `1` (transition from `1` to `0`).

#### 2. Hardware Register Architecture:
- Multiplicand Register ($M$): $n$ bits.
- Accumulator Register ($A$): $n$ bits, initialized to $00\dots0_2$.
- Multiplier Register ($Q$): $n$ bits.
- Extra 1-bit Flip-Flop ($Q_{-1}$): Initialized to $0$.
- Sequence Counter ($SC$): Initialized to $n$.

#### 3. Booth's Decision Table:

| Current Bit $Q_0$ | Previous Bit $Q_{-1}$ | Algebraic Interpretation | Microoperation Action |
| :---: | :---: | :--- | :--- |
| **0** | **0** | String of zeros | Arithmetic Shift Right ($ASHR$) $[A, Q, Q_{-1}]$ |
| **0** | **1** | End of a run of ones | $A \leftarrow A + M$, then $ASHR [A, Q, Q_{-1}]$ |
| **1** | **0** | Beginning of a run of ones | $A \leftarrow A - M$ (or $A + \overline{M} + 1$), then $ASHR [A, Q, Q_{-1}]$ |
| **1** | **1** | String of ones | Arithmetic Shift Right ($ASHR$) $[A, Q, Q_{-1}]$ |

> **Arithmetic Shift Right ($ASHR$) Definition**:
> Shifts all bits of $A, Q, Q_{-1}$ one position to the right. The MSB of $A$ ($a_{n-1}$) is **replicated** to preserve the algebraic sign bit. The LSB of $A$ enters the MSB of $Q$. The LSB of $Q$ enters $Q_{-1}$. The previous $Q_{-1}$ is discarded.

```
ASCII Flowchart: Booth's Multiplication Algorithm

                   +-------------------------+
                   |  Start: A = 0, Q-1 = 0  |
                   |  M = Multiplicand       |
                   |  Q = Multiplier, SC = n |
                   +------------+------------+
                                |
                                v
                     /---------------------\
                    /  Inspect Q0 and Q-1   \
                    \                       /
                     \---------------------/
                      /       |         \
             Q0 Q-1 =10  Q0 Q-1=00,11  Q0 Q-1 =01
            /                 |                 \
           v                  |                  v
   +---------------+          |          +---------------+
   |   A = A - M   |          |          |   A = A + M   |
   +-------+-------+          |          +-------+-------+
           |                  |                  |
           +----------------> v <----------------+
                     +-----------------+
                     | Arithmetic Shift|
                     |  Right (ASHR)   |
                     |  [A, Q, Q-1]    |
                     +--------+--------+
                              |
                              v
                     +-----------------+
                     |     SC = SC - 1 |
                     +--------+--------+
                              |
                              v
                        /-----------\
                       /   SC == 0?  \---(No)----+
                       \             /          |
                        \-----------/           |
                              | (Yes)            |
                              v                  |
                     +-----------------+         |
                     |  End: Product   |         |
                     |    in [A, Q]    |         |
                     +-----------------+         |
                              ^                  |
                              +------------------+
```

---

### 2.3.3 Comprehensive Worked Examples: Booth's Algorithm

#### Worked Example 1: Multiply $(+7) \times (-5)$ in 5-bit 2's complement
- Multiplicand $M = +7 = 00111_2$
- 2's complement $-M = 11001_2$
- Multiplier $Q = -5 = 11011_2$
- Initial registers: $A = 00000$, $Q = 11011$, $Q_{-1} = 0$, $SC = 5$.

```
+-------+-------+-------+------+----+-----------------------------------------------------+
| Cycle |   A   |   Q   | Q_-1 | SC | Operation Performed                                 |
+-------+-------+-------+------+----+-----------------------------------------------------+
| Init  | 00000 | 11011 |  0   | 5  | Initial Setup                                       |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 1     |       |       |      |    | Q0 Q_-1 = 1 0 -> A = A - M (A + 11001)              |
|       | 11001 | 11011 |  0   |    | A <- 00000 + 11001 = 11001                          |
|       | 11100 | 11101 |  1   | 4  | ASHR [A, Q, Q_-1], SC = 4                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 2     |       |       |      |    | Q0 Q_-1 = 1 1 -> No arithmetic                      |
|       | 11110 | 01110 |  1   | 3  | ASHR [A, Q, Q_-1], SC = 3                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 3     |       |       |      |    | Q0 Q_-1 = 0 1 -> A = A + M (A + 00111)              |
|       | 00101 | 01110 |  1   |    | A <- 11110 + 00111 = 00101                          |
|       | 00010 | 10111 |  0   | 2  | ASHR [A, Q, Q_-1], SC = 2                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 4     |       |       |      |    | Q0 Q_-1 = 1 0 -> A = A - M (A + 11001)              |
|       | 11011 | 10111 |  0   |    | A <- 00010 + 11001 = 11011                          |
|       | 11101 | 11011 |  1   | 1  | ASHR [A, Q, Q_-1], SC = 1                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 5     |       |       |      |    | Q0 Q_-1 = 1 1 -> No arithmetic                      |
|       | 11110 | 11101 |  1   | 0  | ASHR [A, Q, Q_-1], SC = 0 (TERMINATE)               |
+-------+-------+-------+------+----+-----------------------------------------------------+

Final 10-bit Product in [A, Q]:
  [A, Q] = 11110 11101_2
Verification:
  The MSB is 1 (Negative result).
  Take 2's complement of 1111011101:
    Invert: 0000100010
    Add 1:  0000100011_2 = 32 + 2 + 1 = 35_10.
  Value = -35_10.
  Mathematical Check: (+7) * (-5) = -35. PERFECT MATCH!
```

---

#### Worked Example 2: Multiply $(-9) \times (-4)$ in 5-bit 2's complement
- Multiplicand $M = -9 = 10111_2$
- $-M = -(-9) = +9 = 01001_2$
- Multiplier $Q = -4 = 11100_2$
- Initial: $A = 00000$, $Q = 11100$, $Q_{-1} = 0$, $SC = 5$.

```
+-------+-------+-------+------+----+-----------------------------------------------------+
| Cycle |   A   |   Q   | Q_-1 | SC | Operation Performed                                 |
+-------+-------+-------+------+----+-----------------------------------------------------+
| Init  | 00000 | 11100 |  0   | 5  | Initial Setup                                       |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 1     |       |       |      |    | Q0 Q_-1 = 0 0 -> No arithmetic                      |
|       | 00000 | 01110 |  0   | 4  | ASHR [A, Q, Q_-1], SC = 4                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 2     |       |       |      |    | Q0 Q_-1 = 0 0 -> No arithmetic                      |
|       | 00000 | 00111 |  0   | 3  | ASHR [A, Q, Q_-1], SC = 3                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 3     |       |       |      |    | Q0 Q_-1 = 1 0 -> A = A - M (A + 01001)              |
|       | 01001 | 00111 |  0   |    | A <- 00000 + 01001 = 01001                          |
|       | 00100 | 10011 |  1   | 2  | ASHR [A, Q, Q_-1], SC = 2                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 4     |       |       |      |    | Q0 Q_-1 = 1 1 -> No arithmetic                      |
|       | 00010 | 01001 |  1   | 1  | ASHR [A, Q, Q_-1], SC = 1                           |
+-------+-------+-------+------+----+-----------------------------------------------------+
| 5     |       |       |      |    | Q0 Q_-1 = 1 1 -> No arithmetic                      |
|       | 00001 | 00100 |  1   | 0  | ASHR [A, Q, Q_-1], SC = 0 (TERMINATE)               |
+-------+-------+-------+------+----+-----------------------------------------------------+

Final 10-bit Product in [A, Q]:
  [A, Q] = 00001 00100_2
Verification:
  The MSB is 0 (Positive result).
  Value = 0000100100_2 = 32 + 4 = +36_10.
  Mathematical Check: (-9) * (-4) = +36. PERFECT MATCH!
```

---

### 2.3.4 Bit-Pair Recoding (Modified Booth's Algorithm / Radix-4)
Radix-4 multiplication scans **three bits at a time** ($Q_{2i+1}, Q_{2i}, Q_{2i-1}$) with 1 bit of overlap, processing two bits of the multiplier in each clock cycle. This halves the number of required cycles from $n$ to $n/2$.

#### Radix-4 Recoding Table:

| $Q_{2i+1}$ | $Q_{2i}$ | $Q_{2i-1}$ | Multiplier Factor | Hardware Operation on Accumulator |
| :---: | :---: | :---: | :---: | :--- |
| 0 | 0 | 0 | $0$ | Add $0$ |
| 0 | 0 | 1 | $+1$ | Add $1 \times M$ |
| 0 | 1 | 0 | $+1$ | Add $1 \times M$ |
| 0 | 1 | 1 | $+2$ | Add $2 \times M$ (Left shift $M$ by 1 bit, then add) |
| 1 | 0 | 0 | $-2$ | Subtract $2 \times M$ (Left shift $M$ by 1 bit, then subtract) |
| 1 | 0 | 1 | $-1$ | Subtract $1 \times M$ |
| 1 | 1 | 0 | $-1$ | Subtract $1 \times M$ |
| 1 | 1 | 1 | $0$ | Add $0$ |

Each cycle performs: $A \leftarrow A + (\text{Factor} \times M)$, followed by a **2-bit Arithmetic Shift Right ($ASHR2$)** of $[A, Q]$.

---

## 2.4 DIVISION ALGORITHMS

### 2.4.1 Restoring Division Algorithm (Unsigned)
- **Registers**: $A$ (Remainder, $n$ bits, initialized to 0), $Q$ (Dividend, $n$ bits), $B$ (Divisor, $n$ bits), $SC = n$.
- **Operational Procedure (Each Cycle)**:
  1. Shift left $[A, Q]$ by 1 bit (vacating $q_0$).
  2. Subtract Divisor from Accumulator: $A \leftarrow A - B$.
  3. Inspect sign bit of $A$ ($a_{n-1}$):
     - If $A < 0$ (sign is `1`): Subtraction failed. Set quotient bit $q_0 = 0$, and **Restore** $A$: $A \leftarrow A + B$.
     - If $A \ge 0$ (sign is `0`): Subtraction succeeded. Set quotient bit $q_0 = 1$. (No restoration).
  4. Decrement $SC$. Repeat if $SC \neq 0$.

```
ASCII Flowchart: Restoring Division Algorithm

                +-------------------------+
                | Start: A = 0, B = Divisor|
                | Q = Dividend, SC = n    |
                +------------+------------+
                             |
                             v
                +-------------------------+
                | Shift Left [A, Q]       |
                +------------+------------+
                             |
                             v
                +-------------------------+
                |       A = A - B         |
                +------------+------------+
                             |
                             v
                       /------------\
                      /   Is A < 0?  \
                      \  (Sign = 1) /
                       \-----------/
                        /          \
                  (Yes)/            \ (No)
                      v              v
              +---------------+ +---------------+
              |   q0 = 0      | |   q0 = 1      |
              | A = A + B     | +-------+-------+
              | (Restore A)   |         |
              +-------+-------+         |
                      |                 |
                      +-------> v <-----+
                     +-----------------+
                     |     SC = SC - 1 |
                     +--------+--------+
                              |
                              v
                        /-----------\
                       /   SC == 0?  \---(No)----+
                       \             /          |
                        \-----------/           |
                              | (Yes)            |
                              v                  |
                     +-----------------+         |
                     | End: Q=Quotient |         |
                     |     A=Remainder |         |
                     +-----------------+         |
                              ^                  |
                              +------------------+
```

#### Worked Example: Divide $11_{10}$ ($1011_2$) by $3_{10}$ ($0011_2$) using Restoring Division
- Divisor $B = 0011_2$, $-B = 1101_2$
- Initial: $A = 00000_2$ (5-bit width to track sign), $Q = 1011_2$, $SC = 4$.

```
+-------+-------+------+----+--------------------------------------------------------+
| Cycle |   A   |  Q   | SC | Microoperation & Action                                |
+-------+-------+------+----+--------------------------------------------------------+
| Init  | 00000 | 1011 | 4  | Setup registers                                        |
+-------+-------+------+----+--------------------------------------------------------+
| 1     | 00001 | 011_ |    | Shift Left [A, Q]                                      |
|       | 11110 | 011_ |    | A = A - B (00001 + 1101 = 11110)                       |
|       |       |      |    | Sign of A is 1 (Negative) -> Set q0 = 0, Restore A     |
|       | 00001 | 0110 | 3  | A = A + B (11110 + 0011 = 00001), SC = 3               |
+-------+-------+------+----+--------------------------------------------------------+
| 2     | 00010 | 110_ |    | Shift Left [A, Q]                                      |
|       | 11111 | 110_ |    | A = A - B (00010 + 1101 = 11111)                       |
|       |       |      |    | Sign of A is 1 (Negative) -> Set q0 = 0, Restore A     |
|       | 00010 | 1100 | 2  | A = A + B (11111 + 0011 = 00010), SC = 2               |
+-------+-------+------+----+--------------------------------------------------------+
| 3     | 00101 | 100_ |    | Shift Left [A, Q]                                      |
|       | 00010 | 100_ |    | A = A - B (00101 + 1101 = 00010)                       |
|       |       |      |    | Sign of A is 0 (Positive) -> Set q0 = 1, NO RESTORE    |
|       | 00010 | 1001 | 1  | A remains 00010, SC = 1                                |
+-------+-------+------+----+--------------------------------------------------------+
| 4     | 00101 | 001_ |    | Shift Left [A, Q]                                      |
|       | 00010 | 001_ |    | A = A - B (00101 + 1101 = 00010)                       |
|       |       |      |    | Sign of A is 0 (Positive) -> Set q0 = 1, NO RESTORE    |
|       | 00010 | 0011 | 0  | A remains 00010, SC = 0 (TERMINATE)                    |
+-------+-------+------+----+--------------------------------------------------------+

Final Results:
  Quotient  Q = 0011_2 = 3_10
  Remainder A = 00010_2 = 2_10
Mathematical Check: 11 = (3 * 3) + 2. Correct!
```

---

### 2.4.2 Non-Restoring Division Algorithm
Restoring division wastes time adding $B$ back whenever subtraction fails. 
Algebraically:
$$\text{If } A < 0, \text{ Restoring step adds } B: (A + B)$$
$$\text{Next cycle shifts left and subtracts } B: 2(A + B) - B = 2A + 2B - B = 2A + B$$
Thus, we can completely eliminate the restoration step by **adding $B$ in the next cycle** instead of subtracting!

#### Non-Restoring Procedure:
1. If $A \ge 0$: Shift left $[A, Q]$, then subtract $B$: $A \leftarrow 2A - B$.
2. If $A < 0$: Shift left $[A, Q]$, then add $B$: $A \leftarrow 2A + B$.
3. Check sign of new $A$:
   - If $A \ge 0$: set $q_0 = 1$.
   - If $A < 0$: set $q_0 = 0$.
4. Repeat for $n$ cycles.
5. **Post-Correction**: If after the final cycle $A < 0$, perform a single restoration: $A \leftarrow A + B$.

#### Worked Example: Divide $11_{10}$ ($1011_2$) by $3_{10}$ ($0011_2$) using Non-Restoring Division
- $B = 0011_2$, $-B = 1101_2$. Initial: $A = 00000, Q = 1011, SC = 4$.

```
+-------+-------+------+----+--------------------------------------------------------+
| Cycle |   A   |  Q   | SC | Microoperation & Action                                |
+-------+-------+------+----+--------------------------------------------------------+
| Init  | 00000 | 1011 | 4  | Setup                                                  |
+-------+-------+------+----+--------------------------------------------------------+
| 1     | 00001 | 011_ |    | A >= 0 -> Shift Left [A, Q]                            |
|       | 11110 | 011_ |    | Subtract B: A = A - B (00001 + 1101 = 11110)           |
|       | 11110 | 0110 | 3  | A is Negative -> Set q0 = 0 (NO RESTORE), SC = 3       |
+-------+-------+------+----+--------------------------------------------------------+
| 2     | 11100 | 110_ |    | A < 0 -> Shift Left [A, Q]                             |
|       | 11111 | 110_ |    | Add B: A = A + B (11100 + 0011 = 11111)                |
|       | 11111 | 1100 | 2  | A is Negative -> Set q0 = 0 (NO RESTORE), SC = 2       |
+-------+-------+------+----+--------------------------------------------------------+
| 3     | 11110 | 100_ |    | A < 0 -> Shift Left [A, Q]                             |
|       | 00001 | 100_ |    | Add B: A = A + B (11110 + 0011 = 00001)                |
|       | 00001 | 1001 | 1  | A is Positive -> Set q0 = 1, SC = 1                    |
+-------+-------+------+----+--------------------------------------------------------+
| 4     | 00010 | 001_ |    | A >= 0 -> Shift Left [A, Q]                            |
|       | 11111 | 001_ |    | Subtract B: A = A - B (00010 + 1101 = 11111)           |
|       | 11111 | 0010 | 0  | A is Negative -> Set q0 = 0, SC = 0                    |
+-------+-------+------+----+--------------------------------------------------------+
| Post  | 00010 | 0011 |    | Since final A < 0, Restore: A = A + B                  |
| Fix   |       |      |    | A = 11111 + 0011 = 00010. Q[0] is set to 1.            |
|       |       |      |    | Quotient Q = 0011_2 = 3, Remainder A = 00010_2 = 2.   |
+-------+-------+------+----+--------------------------------------------------------+
```

---

## 2.5 FLOATING-POINT ARITHMETIC OPERATIONS

### 2.5.1 Floating-Point Addition and Subtraction
To perform $X \pm Y = (M_X \cdot 2^{E_X}) \pm (M_Y \cdot 2^{E_Y})$:

1. **Check for Zeros**: If $X = 0$, result is $\pm Y$. If $Y = 0$, result is $X$.
2. **Align Significands**:
   - Compute exponent difference: $d = E_X - E_Y$.
   - If $d > 0$: Shift $M_Y$ right by $d$ bit positions; set common exponent $E = E_X$.
   - If $d < 0$: Shift $M_X$ right by $|d|$ bit positions; set common exponent $E = E_Y$.
   - If $d = 0$: Exponents are already aligned.
3. **Add / Subtract Significands**:
   - Perform fixed-point addition or subtraction on the aligned mantissas.
4. **Normalize the Result**:
   - If the addition generated a carry-out (significand overflow $\ge 2.0$): Shift significand right by 1 bit, increment exponent $E \leftarrow E + 1$.
   - If the subtraction generated leading zeros: Shift significand left by $k$ bits until MSB is `1`, decrement exponent $E \leftarrow E - k$.
5. **Round the Result**:
   - Round according to IEEE mode (Round to Nearest Even using Guard, Round, and Sticky bits).
6. **Exception Check**: Check for exponent overflow ($E > 254$) or underflow ($E < 1$).

---

## 2.6 PROCESSOR ORGANIZATION & GENERAL REGISTER ORGANIZATION

### 2.6.1 Multi-Bus General Register Organization (Mano Model)

```
ASCII Architecture: General Register Organization with 7 CPU Registers

   +----+  +----+  +----+  +----+  +----+  +----+  +----+
   | R1 |  | R2 |  | R3 |  | R4 |  | R5 |  | R6 |  | R7 |
   +----+  +----+  +----+  +----+  +----+  +----+  +----+
     |  |    |  |    |  |    |  |    |  |    |  |    |  |
     |  +----+--+----+--+----+--+----+--+----+--+----+--+=====> Bus A (Source 1)
     |       |       |       |       |       |       |
     +-------+-------+-------+-------+-------+-------+========> Bus B (Source 2)
                             |       |
                             v       v
                         +---------------+
                         |      ALU      |<=== OPR (Operation Select)
                         +-------+-------+
                                 |
                                 v
     =========================================================> Bus D (Destination)
                                 |
                                 v
                     [ 3-to-8 Destination Decoder ]
                                 |
             +----+----+----+----+----+----+----+
             | Load Enable Lines for R1 through R7
```

#### Control Word Format (14 Bits):
$$\text{Control Word: } [\text{SELA (3 bits)} \mid \text{SELB (3 bits)} \mid \text{SELD (3 bits)} \mid \text{OPR (5 bits)}]$$

1. **SELA (3 bits)**: Selects source register for Bus A.
2. **SELB (3 bits)**: Selects source register for Bus B.
3. **SELD (3 bits)**: Selects destination register loaded from Bus D.
4. **OPR (5 bits)**: Specifies the ALU microoperation (ADD, SUB, AND, OR, INC, SHL, etc.).

```
Register Selection Encoding:
  Code   SELA (Bus A)   SELB (Bus B)   SELD (Bus D)
  000    Input Data     Input Data     None (No load)
  001    R1             R1             R1
  010    R2             R2             R2
  011    R3             R3             R3
  100    R4             R4             R4
  101    R5             R5             R5
  110    R6             R6             R6
  111    R7             R7             R7
```

**Example Control Word**: Execute $R1 \leftarrow R2 + R3$
- Bus A Source: $R2 \implies \text{SELA} = 010$
- Bus B Source: $R3 \implies \text{SELB} = 011$
- Destination: $R1 \implies \text{SELD} = 001$
- Operation: $\text{ADD} \implies \text{OPR} = 00010$
- Full Binary Control Word: `010 011 001 00010`

---

## 2.7 STACK ORGANIZATION: REGISTER STACK VS MEMORY STACK

A **stack** is a storage structure operating on the Last-In, First-Out (LIFO) principle. Items are added (PUSH) and removed (POP) strictly from the Top of Stack ($TOS$), referenced by the **Stack Pointer ($SP$)**.

### 2.7.1 Register Stack (Hardware CPU Stack)
Constructed from a dedicated register array within the CPU (e.g., 64 words) and a 6-bit $SP$:
- **Push Microoperations**:
  $$SP \leftarrow SP + 1$$
  $$M[SP] \leftarrow DR$$
  $$\text{If } SP = 0 \text{ then } FULL \leftarrow 1$$
  $$EMPTY \leftarrow 0$$
- **Pop Microoperations**:
  $$DR \leftarrow M[SP]$$
  $$SP \leftarrow SP - 1$$
  $$\text{If } SP = 0 \text{ then } EMPTY \leftarrow 1$$
  $$FULL \leftarrow 0$$

### 2.7.2 Memory Stack (RAM Stack)
Allocated within general system RAM. By convention in modern architectures (x86, ARM), the memory stack **grows downward** from high memory addresses toward lower memory addresses:
- **PUSH Microoperations**:
  $$SP \leftarrow SP - 1$$
  $$M[SP] \leftarrow DR$$
- **POP Microoperations**:
  $$DR \leftarrow M[SP]$$
  $$SP \leftarrow SP + 1$$

---

## 2.8 ADDRESSING MODES: EXHAUSTIVE ANALYSIS & EFFECTIVE ADDRESS (EA)

The **Effective Address ($EA$)** is the actual physical memory address that must be applied to the system address bus to fetch or store the operand.

```
Master Comparison Table: All 10 Addressing Modes

+------------------------+-------------------------------+-------------------+---------------------------------------------------+
| Addressing Mode        | Effective Address Formula     | Memory References | Primary Real-World Application                    |
+------------------------+-------------------------------+-------------------+---------------------------------------------------+
| 1. Implied             | None (Implicit in Opcode)     | 0                 | Accumulator/Stack instructions (CLC, INCA, RET)   |
| 2. Immediate           | EA = PC (Operand in IR)       | 0 (Operand fetch) | Initializing constants (MOV R1, #100)             |
| 3. Direct (Absolute)   | EA = Address Field (A)        | 1                 | Global/Static variables (LDA 3000H)               |
| 4. Indirect            | EA = M[A]                     | 2                 | Pointers, parameter passing (LDA @3000H)          |
| 5. Register            | EA = Register (R)             | 0                 | High-speed scratchpad arithmetic (ADD R1, R2)     |
| 6. Register Indirect   | EA = [R]                      | 1                 | Pointer dereferencing (*ptr), dynamic arrays      |
| 7. Relative            | EA = PC + Address Offset      | 1                 | Branching, position-independent code (BR +24)     |
| 8. Indexed             | EA = XR + Address Field       | 1                 | Linear array indexing (A[i])                      |
| 9. Base Register       | EA = BR + Displacement Offset | 1                 | Relocatable programs, segment base offsets        |
| 10. Auto-inc / dec     | EA = [R]; R = R +/- 1         | 1                 | Loop traversal, hardware stack emulation          |
+------------------------+-------------------------------+-------------------+---------------------------------------------------+
```

---

### 2.8.1 Multi-Mode Comprehensive Worked Numerical Problem
Given the processor state and memory map below, calculate the **Effective Address ($EA$)** and the **Operand Value** fetched for each addressing mode.

```
System State:
  PC = 200
  R1 = 400
  XR = 100
  AC = 500

Memory Map:
  Address   Value
  -------   -----
  200       Load Mode (Opcode), Address Field = 500
  201       Next Instruction
  ...
  400       700
  ...
  500       800
  ...
  600       900
  ...
  700       1000
  ...
  800       300
```

```
Calculations for Each Mode (Instruction Address Field A = 500):

1. Immediate Mode:
   - EA = Not Applicable. Operand is the address field itself.
   - Operand Value = 500

2. Direct Addressing Mode:
   - EA = A = 500
   - Operand Value = M[500] = 800

3. Indirect Addressing Mode:
   - EA = M[A] = M[500] = 800
   - Operand Value = M[800] = 300

4. Register Mode:
   - Target Register = R1
   - EA = R1 (No memory reference)
   - Operand Value = Contents of R1 = 400

5. Register Indirect Mode:
   - EA = [R1] = 400
   - Operand Value = M[400] = 700

6. Relative Addressing Mode:
   - Effective Address = PC + A = 201 + 500 = 701  (using updated PC = 201)
   - (If PC not yet incremented: EA = 200 + 500 = 700 -> Operand = M[700] = 1000)

7. Indexed Addressing Mode:
   - EA = XR + A = 100 + 500 = 600
   - Operand Value = M[600] = 900

8. Auto-Increment Mode (using R1):
   - EA = [R1] = 400
   - Operand Value = M[400] = 700
   - Post-operation Register Update: R1 <- R1 + 1 = 401
```

---

## 2.9 UNIT 2 HIGH-PROBABILITY EXAM QUESTIONS & STEP-BY-STEP SOLUTIONS

### Q1: Draw the logic equations and explain why a Carry Look-Ahead Adder is significantly faster than a Ripple Carry Adder.
**Solution**:
1. State the bottleneck of Ripple Carry: carry must sequentially ripple through $n$ stages, yielding delay $T = 2n\Delta$.
2. State the definitions of Carry Generate $G_i = A_i B_i$ and Carry Propagate $P_i = A_i \oplus B_i$.
3. Expand $C_1, C_2, C_3, C_4$ to show that each carry is computed in 2 levels of gates directly from primary inputs and $C_0$.
4. Total delay is $4\Delta$ regardless of word size within the block, achieving an exponential speedup over RCA.

### Q2: Multiply $(-7) \times (+3)$ using Booth's algorithm with 5-bit registers.
**Solution**:
- Multiplicand $M = -7 = 11001_2$, $-M = +7 = 00111_2$.
- Multiplier $Q = +3 = 00011_2$.
- Setup: $A = 00000, Q = 00011, Q_{-1} = 0, SC = 5$.
- Trace:
  - Cycle 1: $Q_0 Q_{-1} = 10 \implies A \leftarrow A - M$ ($00000 + 00111 = 00111$). $ASHR \implies A = 00011, Q = 10001, Q_{-1} = 1, SC = 4$.
  - Cycle 2: $Q_0 Q_{-1} = 11 \implies$ No arithmetic. $ASHR \implies A = 00001, Q = 11000, Q_{-1} = 1, SC = 3$.
  - Cycle 3: $Q_0 Q_{-1} = 01 \implies A \leftarrow A + M$ ($00001 + 11001 = 11010$). $ASHR \implies A = 11101, Q = 01100, Q_{-1} = 0, SC = 2$.
  - Cycle 4: $Q_0 Q_{-1} = 00 \implies$ No arithmetic. $ASHR \implies A = 11110, Q = 10110, Q_{-1} = 0, SC = 1$.
  - Cycle 5: $Q_0 Q_{-1} = 00 \implies$ No arithmetic. $ASHR \implies A = 11111, Q = 01011, Q_{-1} = 0, SC = 0$.
- Result: $[A, Q] = 11111 01011_2$.
- Verification: Negative number. 2's complement of $1111101011$ is $0000010101_2 = 21_{10}$. Result = $-21_{10}$. $(-7) \times 3 = -21$. Correct!

---

## 2.10 UNIT 2 COMMON TRAPS, PITFALLS, AND CONCEPT CHECKS

> [!CAUTION]
> **Trap 1: Booth's Arithmetic Shift Right Must Replicate Sign!**  
> In Booth's algorithm, shifting right is strictly an **Arithmetic Shift Right ($ASHR$)**, NOT a logical shift right! The MSB of $A$ ($a_{n-1}$) must be copied into the new MSB position. Performing a logical shift with zero-fill corrupts signed numbers completely.

> [!WARNING]
> **Trap 2: Restoring vs Non-Restoring Final Step!**  
> In non-restoring division, students often forget the **post-correction step**: if after $n$ cycles the remainder in accumulator $A$ is negative ($A < 0$), one final addition $A \leftarrow A + B$ is strictly mandatory to obtain the true positive remainder!

# UNIT 3: CONTROL UNIT DESIGN & MICROPROGRAMMING

---

## 3.1 INSTRUCTION FORMATS AND MACHINE TYPES

An instruction comprises an **Opcode (Operation Code)** specifying the action to perform, and zero or more **Address Fields** specifying the locations of operands and results:
$$\text{Instruction Format: } [\text{Opcode} \mid \text{Mode} \mid \text{Address Field 1} \mid \text{Address Field 2} \dots]$$

### 3.1.1 Classification by Address Count
Architectures are traditionally categorized by the maximum number of memory/register addresses permitted in an instruction format.

#### 1. Three-Address Instructions:
- **Format**: `OPCODE Dest, Source1, Source2`
- **RTL**: $\text{Dest} \leftarrow [\text{Source1}] \text{ OP } [\text{Source2}]$
- **Characteristics**: Preserves source operands; programs require the smallest instruction count; instruction words are wide (many bits needed to encode 3 addresses).
- **Example Evaluation of $X = (A + B) \times (C + D)$**:
  ```assembly
  ADD R1, A, B     ; R1 <- M[A] + M[B]
  ADD R2, C, D     ; R2 <- M[C] + M[D]
  MUL X, R1, R2    ; M[X] <- R1 * R2
  ```

#### 2. Two-Address Instructions:
- **Format**: `OPCODE Dest, Source`
- **RTL**: $\text{Dest} \leftarrow [\text{Dest}] \text{ OP } [\text{Source}]$
- **Characteristics**: Destructive update (destination register is overwritten); most common in general-purpose commercial architectures (x86).
- **Example Evaluation of $X = (A + B) \times (C + D)$**:
  ```assembly
  MOV R1, A        ; R1 <- M[A]
  ADD R1, B        ; R1 <- R1 + M[B]
  MOV R2, C        ; R2 <- M[C]
  ADD R2, D        ; R2 <- R2 + M[D]
  MUL R1, R2       ; R1 <- R1 * R2
  MOV X, R1        ; M[X] <- R1
  ```

#### 3. One-Address Instructions (Accumulator Architecture):
- **Format**: `OPCODE Address`
- **RTL**: $AC \leftarrow AC \text{ OP } M[\text{Address}]$
- **Characteristics**: The Accumulator register ($AC$) is the implicit source and destination for all ALU operations. Highly compact instruction format.
- **Example Evaluation of $X = (A + B) \times (C + D)$**:
  ```assembly
  LOAD  A          ; AC <- M[A]
  ADD   B          ; AC <- AC + M[B]
  STORE T          ; M[T] <- AC (Save temporary A+B)
  LOAD  C          ; AC <- M[C]
  ADD   D          ; AC <- AC + M[D]
  MUL   T          ; AC <- AC * M[T]
  STORE X          ; M[X] <- AC
  ```

#### 4. Zero-Address Instructions (Stack Architecture):
- **Format**: `OPCODE`
- **RTL**: $TOS \leftarrow TOS \text{ OP } SOS$ *(Top of Stack and Second on Stack)*
- **Characteristics**: All operands are held implicitly on top of a hardware/memory stack. Evaluates expressions using **Reverse Polish Notation (RPN)** / Postfix.
- **RPN Form of $(A + B) \times (C + D)$**: `A B + C D + *`
- **Code**:
  ```assembly
  PUSH A           ; TOS <- M[A]
  PUSH B           ; TOS <- M[B]
  ADD              ; TOS <- (A + B)
  PUSH C           ; TOS <- M[C]
  PUSH D           ; TOS <- M[D]
  ADD              ; TOS <- (C + D)
  MUL              ; TOS <- (A + B) * (C + D)
  POP  X           ; M[X] <- TOS
  ```

---

### 3.1.2 Side-by-Side Comparison of Machine Architectures

| Parameter | Three-Address | Two-Address | One-Address (Accumulator) | Zero-Address (Stack) |
| :--- | :--- | :--- | :--- | :--- |
| **Implicit Operands** | None | Destination = Source1 | Accumulator ($AC$) | Top of Stack ($TOS$) |
| **Instruction Length** | Very Long (3 address fields) | Medium (2 address fields) | Short (1 address field) | Shortest (Opcode only) |
| **Program Length (Instructions)** | Shortest (3 instructions) | Moderate (6 instructions) | Long (7 instructions) | Longest (8 instructions) |
| **Temporary Registers Needed** | Registers $R1, R2$ | Registers $R1, R2$ | Memory temp location $T$ | Stack elements |
| **Typical Machines** | MIPS, ARM, RISC-V | Intel x86, Motorola 68000 | PDP-8, 8085 Microprocessor | Burroughs B5500, JVM |

---

## 3.2 INSTRUCTION CYCLE PHASES, SUBCYCLES, & RTL TRACES

The **Instruction Cycle** is the continuous sequence of hardware states executed by the CPU to process an individual machine instruction.

```
ASCII State Transition Diagram: Complete Instruction Cycle

          +----------------------------------------------------+
          |                                                    |
          v                                                    |
    +-----------+      +------------+      +---------------+   |
--->|   FETCH   |----->|   DECODE   |----->|   EFFECTIVE   |   |
    |   PHASE   |      |   PHASE    |      | ADDRESS (EA)  |   |
    +-----------+      +------------+      +-------+-------+   |
                                                   |           |
                                                   v           |
                                           +---------------+   |
                                           |    EXECUTE    |   |
                                           |     PHASE     |   |
                                           +-------+-------+   |
                                                   |           |
                                                   v           |
                                           +---------------+   |
                                           |   INTERRUPT   |---+
                                           |     CHECK     |
                                           +---------------+
```

### 3.2.1 Detailed Micro-Operations for Each Phase (Basic Computer Model)

#### Phase 1: Fetch Phase ($T_0, T_1, T_2$)
- **Clock $T_0$**:
  $$T_0: AR \leftarrow PC$$
  *(Apply address in Program Counter to the Address Register via common bus)*
- **Clock $T_1$**:
  $$T_1: IR \leftarrow M[AR], \quad PC \leftarrow PC + 1$$
  *(Read instruction word from memory into Instruction Register; increment PC)*
- **Clock $T_2$**:
  $$T_2: D_0, \dots, D_7 \leftarrow \text{Decode } IR(12-14), \quad AR \leftarrow IR(0-11), \quad I \leftarrow IR(15)$$
  *(Opcode decoded by 3-to-8 decoder; address bits 0-11 loaded into AR; addressing mode bit 15 loaded into flip-flop $I$)*

#### Phase 2: Decode & Indirect Address Phase ($T_3$)
The control unit determines the instruction category:
- **Memory-Reference Instruction** ($D_7 = 0$):
  - Direct Addressing ($I = 0$): Nothing to do at $T_3$. Operands ready in memory at address $AR$.
  - Indirect Addressing ($I = 1$):
    $$D_7' I T_3: AR \leftarrow M[AR]$$
    *(Read effective address from pointer location into AR)*
- **Register-Reference Instruction** ($D_7 = 1, I = 0$):
  - Executed entirely at clock pulse $T_3$ using bits $IR(0-11)$.
- **Input-Output Instruction** ($D_7 = 1, I = 1$):
  - Executed entirely at clock pulse $T_3$ using bits $IR(0-11)$.

---

### 3.2.2 Complete Execution Phase for Memory-Reference Instructions

| Opcode | Symbol | Operation Description | Register Transfer Logic (RTL) |
| :---: | :---: | :--- | :--- |
| `000` | **AND** | Logical AND memory word to AC | $D_0 T_4: DR \leftarrow M[AR]$<br>$D_0 T_5: AC \leftarrow AC \land DR, \quad SC \leftarrow 0$ |
| `001` | **ADD** | Add memory word to AC with carry | $D_1 T_4: DR \leftarrow M[AR]$<br>$D_1 T_5: AC \leftarrow AC + DR, \quad E \leftarrow C_{out}, \quad SC \leftarrow 0$ |
| `010` | **LDA** | Load AC from memory | $D_2 T_4: DR \leftarrow M[AR]$<br>$D_2 T_5: AC \leftarrow DR, \quad SC \leftarrow 0$ |
| `011` | **STA** | Store AC into memory | $D_3 T_4: M[AR] \leftarrow AC, \quad SC \leftarrow 0$ |
| `100` | **BUN** | Branch unconditionally | $D_4 T_4: PC \leftarrow AR, \quad SC \leftarrow 0$ |
| `101` | **BSA** | Branch and Save Return Address | $D_5 T_4: M[AR] \leftarrow PC, \quad AR \leftarrow AR + 1$<br>$D_5 T_5: PC \leftarrow AR, \quad SC \leftarrow 0$ |
| `110` | **ISZ** | Increment and Skip if Zero | $D_6 T_4: DR \leftarrow M[AR]$<br>$D_6 T_5: DR \leftarrow DR + 1$<br>$D_6 T_6: M[AR] \leftarrow DR, \; \text{if } (DR = 0) \text{ then } PC \leftarrow PC + 1, \; SC \leftarrow 0$ |

> **Detailed Analysis of BSA (Subroutine Call)**:
> BSA stores the return address (contents of $PC$) into memory at address $AR$, increments $AR$ by 1, and branches to $AR+1$ (the first instruction of the subroutine). The return is executed later via indirect branch `BUN @AR`.

---

## 3.3 HARDWIRED CONTROL UNIT DESIGN

A **Hardwired Control Unit** is a combinational logic circuit that generates control signals directly from hardware flip-flops, decoders, and logic gates without intermediate microcode.

```
ASCII Architecture: Hardwired Control Unit

               Instruction Register (IR)
           +---+-------------------+---------------+
           | I |  Opcode (12-14)   | Address (0-11)|
           +---+---------+---------+---------------+
             |           |
             |       [ 3-to-8 ]
             |     [ Opcode Decoder ]
             |           |
             |           v D0, D1, ..., D7
             |       +------------------------------------+
             +------>|                                    |
                     |    Combinational Control Logic     |=====> Control Outputs
     Clock --------->|             Matrix                 |       (Load, Clear, Read,
                     |          (AND-OR Gates)            |        Write, Bus Select)
     Reset --------->|                                    |
                     +------------------------------------+
                                 ^
                                 | T0, T1, ..., T15
                             [ 4-to-16 ]
                          [ Timing Decoder ]
                                 ^
                                 |
                        +--------+--------+
                        | Sequence Counter|
                        |      (SC)       |
                        +-----------------+
```

### 3.3.1 Hardware Components:
1. **Instruction Register (IR)**: Latches the instruction; presents opcode bits 12-14 to the decoder.
2. **Opcode Decoder (3-to-8)**: Generates 8 mutually exclusive outputs $D_0$ through $D_7$.
3. **Sequence Counter (SC)**: A 4-bit binary counter clocked by the master system clock. Can be incremented (`INR`) or cleared to zero (`CLR`).
4. **Timing Decoder (4-to-16)**: Decodes the count in $SC$ into 16 discrete, sequential timing signals $T_0, T_1, T_2, \dots, T_{15}$.
5. **Logic Gate Matrix**: Synthesized AND-OR logic gates generating physical control lines.

### 3.3.2 Logic Synthesis Example (Control Signal Derivation):
Consider the control signal $x_i$ that loads the Program Counter ($PC$):
- $PC$ is incremented during fetch at $T_1$: $T_1 \implies PC \leftarrow PC + 1$.
- $PC$ is loaded during BUN at $D_4 T_4$: $D_4 T_4 \implies PC \leftarrow AR$.
- $PC$ is loaded during BSA at $D_5 T_5$: $D_5 T_5 \implies PC \leftarrow AR$.
- $PC$ is incremented during ISZ at $D_6 T_6$ if $DR = 0$: $D_6 T_6 (DR == 0) \implies PC \leftarrow PC + 1$.

The hardware Boolean control equation driving the `LD` input of $PC$ is synthesized directly as:
$$\text{Load}(PC) = D_4 T_4 + D_5 T_5$$
$$\text{Increment}(PC) = T_1 + D_6 T_6 (\text{DR\_is\_zero})$$

---

## 3.4 MICROPROGRAMMED CONTROL UNIT DESIGN

Proposed by Maurice Wilkes in 1951, a **Microprogrammed Control Unit** treats control signal generation as executing a software program stored in a specialized fast memory called the **Control Store (Control Memory)**.

### 3.4.1 Fundamental Terminology:
- **Microoperation**: An elementary hardware operation performed on data in registers during a single clock pulse.
- **Microinstruction**: A binary control word stored in control memory specifying one or more simultaneous microoperations and the address of the next microinstruction.
- **Microprogram / Microcode**: A sequence of microinstructions stored in control memory that implements a complete machine instruction (macro-instruction).
- **Control Memory**: High-speed Read-Only Memory (ROM/PROM) internal to the CPU storing the microprograms.

```
ASCII Architecture: Microprogrammed Control Unit (Wilkes Model)

             Instruction Opcode (from IR)
                         |
                         v
               [ Mapping Logic / MUX ]
                         |
                         +--------------------------+
                         |                          |
                         v                          |
             +-----------------------+              |
             | Control Address Reg   |<-------------+
             |        (CAR)          |   Next Address
             +-----------+-----------+      Field
                         |
                         v
             +-----------------------+
             |    Control Memory     |
             |     (ROM / PROM)      |
             +-----------+-----------+
                         |
                         v
             +-----------------------+
             | Control Data Register |
             |     (CDR / MIR)       |
             +---+-------+-------+---+
                 |       |       |   |
                 |       |       |   +--> Next Address Field (AD)
                 |       |       +------> Branch Control Field (BR)
                 |       +--------------> Condition Select Field (CD)
                 v
         Microoperation Fields (F1, F2, F3)
                 |
                 v
        Hardware Control Signals
```

---

### 3.4.2 Address Sequencing Capabilities
The **Microprogram Sequencer** must be capable of generating the next microinstruction address from four distinct sources:
1. **Incrementation**:
   $$CAR \leftarrow CAR + 1$$
   Used for executing sequential microoperations within the same micro-routine.
2. **Conditional and Unconditional Branching**:
   $$CAR \leftarrow \text{Address Field } (AD)$$
   Controlled by testing processor status bits (Sign, Zero, Carry, Overflow).
3. **Instruction Opcode Mapping**:
   Translates the arbitrary binary opcode of an incoming machine instruction into the entry address of its corresponding microprogram in control memory.
4. **Subroutine Call and Return**:
   A dedicated **Subroutine Register (SBR)** saves the return address when calling a microcode subroutine ($SBR \leftarrow CAR + 1$) and restores it on return ($CAR \leftarrow SBR$).

#### Opcode Mapping Logic Example:
Suppose an instruction has a 4-bit opcode ($b_3 b_2 b_1 b_0$) and the Control Memory has 128 words ($7$-bit addresses).
The mapping circuit maps the opcode into the start of a 4-word block in control memory by prefixing a `0` and appending `00`:
$$\text{Mapped Address} = 0 \cdot b_3 b_2 b_1 b_0 \cdot 00_2$$
If opcode is `0101`, the control memory starting address is `0 0101 00` = $20_{10}$.

---

## 3.5 HORIZONTAL VS VERTICAL MICROPROGRAMMING

```
Horizontal Microinstruction Format (Wide, Unencoded):
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
| C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 |C10 | CD | BR | AD |
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
  |<--------------- 1 bit per control line ------------->|

Vertical Microinstruction Format (Narrow, Encoded):
+---------------+---------------+---------------+------+------+-------+
|  Field 1 (3)  |  Field 2 (3)  |  Field 3 (3)  |CD (2)|BR (2)| AD (7)|
+-------+-------+-------+-------+-------+-------+------+------+-------+
        |               |               |
        v               v               v
    [Decoder]       [Decoder]       [Decoder]
        |               |               |
        v               v               v
  8 control lines 8 control lines 8 control lines
```

### 3.5.1 Detailed Architectural Comparison

| Characteristic | Horizontal Microprogramming | Vertical Microprogramming |
| :--- | :--- | :--- |
| **Control Signal Representation** | **1 bit per physical control line** (unencoded or minimally grouped) | **Encoded binary fields** (e.g., 3 bits encode 8 mutually exclusive signals) |
| **Microinstruction Word Width** | **Very Wide** (typically 48 to 128+ bits) | **Narrow** (typically 16 to 32 bits) |
| **Hardware Decoding** | **Zero / Minimal decoding delay**; bits directly drive control lines | **Requires external decoders**; introduces gate propagation delay |
| **Parallel Microoperations** | **Maximum concurrency**; multiple ALU and register transfers per cycle | **Limited concurrency**; at most one operation per encoded field |
| **Control Memory Size** | Large word width $\times$ fewer words | Narrow word width $\times$ more words |
| **Execution Speed** | **Significantly Faster** | **Slower** (due to decoding latency) |
| **Flexibility & Programming** | Difficult to write and optimize manually | Easier to write; closely resembles assembly language |
| **Memory Bit Utilization** | Poor (many bits are `0` / sparse) | High (dense bit packing) |

---

### 3.5.2 Nanoprogramming (Two-Level Control Store)
In horizontal microprogramming, many microinstruction bit patterns are identical across different macro-instructions. 
**Nanoprogramming** decouples control storage into two distinct levels:
1. **Control Memory (Vertical)**: Stores narrow words containing pointers into the Nanostore.
2. **Nanostore (Horizontal)**: Stores wide, unique horizontal control words without duplicates.
- **Trade-off**: Drastically reduces total silicon area at the expense of two sequential memory lookups per microinstruction cycle.

---

## 3.6 ADVANCED CONTROL UNIT CONCEPTS

### 3.6.1 Pre-Fetching Microinstructions (Pipelined Control)
In a non-pipelined control unit, each microinstruction cycle consists of two serial steps:
1. Read microinstruction from Control Memory into $CDR$.
2. Execute the microoperations specified by $CDR$.

**Pre-fetching** introduces a pipeline register: while microinstruction $k$ is being executed by the datapath, microinstruction $k+1$ is concurrently being fetched from Control Memory. This completely hides control memory access latency behind ALU execution.

### 3.6.2 Wide Branch Addressing
Traditional sequencers support only 2-way branches (condition true vs false). **Wide Branch Addressing** inspects multiple status bits simultaneously (e.g., bits $S, Z, C$) to perform an $m$-way branch directly to one of $2^k$ target addresses in a single clock cycle, speeding up complex state-machine routing.

---

## 3.7 MASTER COMPARISON: HARDWIRED VS MICROPROGRAMMED CONTROL

| Comparison Metric | Hardwired Control Unit | Microprogrammed Control Unit |
| :--- | :--- | :--- |
| **Fundamental Architecture** | Combinational logic gates, decoders, state flip-flops | Microcode executed from internal Control ROM |
| **Execution Speed** | **Ultra-Fast** (operates at maximum silicon gate limits) | **Slower** (bounded by Control Store ROM access time) |
| **Flexibility to Modify** | **Extremely Rigid**; modifications require silicon redesign | **Highly Flexible**; modified by reprogramming ROM microcode |
| **Instruction Set Complexity** | Ideal for simple, streamlined instruction sets (**RISC**) | Ideal for large, complex instruction sets (**CISC**) |
| **Chip Area & Cost** | Grows exponentially with instruction set complexity | Scales linearly with instruction set size |
| **Design & Prototyping** | Complex, error-prone, long engineering cycles | Systematic, modular, software-like debugging |
| **Field Upgradability** | Impossible | Possible via writable control store (patching CPU microcode) |

---

## 3.8 UNIT 3 HIGH-PROBABILITY EXAM QUESTIONS & STEP-BY-STEP SOLUTIONS

### Q1: Write the sequence of micro-operations for the instruction BSA (Branch and Save Return Address) in Mano's basic computer. Explain how subroutine return is implemented.
**Solution**:
1. At clock pulse $T_4$:
   $$D_5 T_4: M[AR] \leftarrow PC, \quad AR \leftarrow AR + 1$$
   The address of the next sequential instruction (currently in $PC$) is stored in memory at the address specified by $AR$. $AR$ is incremented to point to the start of the subroutine.
2. At clock pulse $T_5$:
   $$D_5 T_5: PC \leftarrow AR, \quad SC \leftarrow 0$$
   The incremented address is loaded into $PC$, and the Sequence Counter is reset. The next instruction fetched is the first executable instruction of the subroutine.
3. **Subroutine Return**: The subroutine ends with an indirect unconditional branch pointing back to the save location: `BUN @AR_original`. This fetches the stored return address and loads it into $PC$.

### Q2: Compare Horizontal and Vertical Microprogramming across 5 distinct architectural criteria.
**Solution**:
1. **Bit Width**: Horizontal uses wide words (48-128 bits); Vertical uses narrow words (16-32 bits).
2. **Encoding**: Horizontal is unencoded (1 bit per line); Vertical is encoded into binary fields.
3. **Decoding Delay**: Horizontal has zero decoding delay; Vertical requires external decoders adding gate delay.
4. **Concurrency**: Horizontal permits high concurrency of microoperations; Vertical permits one operation per field.
5. **Memory Footprint**: Horizontal has sparse memory bit efficiency; Vertical achieves dense bit packing.

---

## 3.9 UNIT 3 COMMON TRAPS, PITFALLS, AND CONCEPT CHECKS

> [!CAUTION]
> **Trap 1: Microinstruction Address vs Macroinstruction Address!**  
> Do not confuse the memory address in $PC$ with the address in $CAR$! $PC$ points to macro-instructions in Main Memory (RAM). $CAR$ points to micro-instructions in internal Control Memory (ROM).

> [!WARNING]
> **Trap 2: Zero-Address Machines Are Not Operand-Free!**  
> A zero-address instruction has no *explicit* address field in its format, but it operates on two implicit operands popped from the top of the stack and pushes the result back to the stack.

# UNIT 4: MEMORY SYSTEM ORGANIZATION & CACHE ARCHITECTURE

---

## 4.1 MEMORY HIERARCHY, PERFORMANCE BOTTLENECKS, & LOCALITY

### 4.1.1 The Memory Wall & Hierarchy Trade-Offs
In modern computer architecture, processor clock frequencies have scaled exponentially faster than dynamic RAM (DRAM) access latencies. This widening performance disparity is known as the **Memory Wall**.
To bridge this gap without incurring astronomical costs, computer memory is organized into a hierarchical pyramid:

```
ASCII Diagram: Modern Computer Memory Hierarchy Pyramid

                         /\
                        /  \
                       / CPU\            Speed: sub-nanosecond
                      / Regs \           Capacity: < 2 KB
                     +--------+          Cost/bit: Extreme
                    /    L1    \
                   /   Cache    \        Speed: ~1 ns | Capacity: 32-128 KB
                  +--------------+
                 /    L2 Cache    \      Speed: ~3-5 ns | Capacity: 512 KB - 2 MB
                +------------------+
               /      L3 Cache      \    Speed: ~10-20 ns | Capacity: 8 - 64 MB
              +----------------------+
             /       Main Memory      \  Speed: ~50-80 ns | Capacity: 16 - 128 GB
            /        (DRAM RAM)        \ Cost/bit: Moderate
           +----------------------------+
          /      Secondary Storage       \ Speed: 5-50 microseconds (NVMe SSD)
         /     (NVMe / SATA Solid State)  \ Capacity: 512 GB - 4 TB
        +----------------------------------+
       /        Tertiary / Auxiliary        \ Speed: 5-15 milliseconds (HDD)
      /      (Magnetic Disk HDD & Tape)      \ Capacity: Multi-Terabyte / Petabyte
     +----------------------------------------+
```

#### Fundamental Hierarchy Trade-Off Rules:
1. **Access Time ($T_A$)**: Increases by orders of magnitude as we descend the hierarchy.
2. **Storage Capacity**: Increases exponentially as we descend.
3. **Cost per Bit**: Decreases exponentially as we descend.
4. **Access Frequency by Processor**: Decreases as we descend.

---

### 4.1.2 The Principle of Locality of Reference
The memory hierarchy functions effectively because computer programs exhibit **Locality of Reference**, accessing only a small fraction of their total address space during any brief time window.

1. **Temporal Locality (Locality in Time)**:
   - *Principle*: If a memory location is referenced at time $t$, it is highly probable that the exact same location will be referenced again in the near future ($t + \Delta t$).
   - *Causes*: Program loops (`for`, `while`), recursive functions, stack frames, loop counter variables, accumulator accumulation.
2. **Spatial Locality (Locality in Space)**:
   - *Principle*: If a memory location at address $A$ is referenced at time $t$, it is highly probable that memory locations physically adjacent to it ($A \pm 1, A \pm 2$) will be referenced in the near future.
   - *Causes*: Sequential instruction execution (PC increment), linear traversal of one-dimensional arrays, sequential record processing in memory.

---

## 4.2 SEMICONDUCTOR RAM TECHNOLOGIES: SRAM VS DRAM

Semiconductor Random-Access Memory (RAM) provides read and write capability at electronic speeds.

```
ASCII Schematics: SRAM Cell vs DRAM Cell

  Static RAM (6T CMOS Bistable Cell):
          VDD               VDD
           |                 |
         [P1]              [P2]
           |      Node A     |      Node B
   BL -----|--[N1]--+--[N2]--|----- ~BL
           |  (Inv1)|  (Inv2)|
          GND       |       GND
                    |
                 WL (Word Line)

  Dynamic RAM (1T-1C Trench Cell):
                 Bit Line (BL)
                     |
                     v
                   [FET] <----- Word Line (WL)
                     |
                 +---+---+
                 |       |
                --- C_s --- Storage Trench Capacitor (~30 fF)
                ---     ---
                 |       |
                GND     GND
```

### 4.2.1 Static RAM (SRAM)
- **Cell Structure**: 6 CMOS transistors (two cross-coupled CMOS inverters forming a bistable latch, plus two NMOS access pass transistors).
- **Storage Mechanism**: Positive feedback between the two inverters latches the node at either stable Logic `1` (Node A = VDD, Node B = GND) or stable Logic `0`.
- **Read Operation**: Both complementary bit lines ($BL, \overline{BL}$) are pre-charged to $VDD/2$. Asserting Word Line ($WL$) turns on access transistors. The cell pulls one bit line down slightly; a differential sense amplifier amplifies this tiny difference into full logic rails. **Non-destructive read**.
- **Write Operation**: Drivers force $BL$ to `1` and $\overline{BL}$ to `0` (or vice-versa), overpowering the cross-coupled inverters to flip the state.
- **Characteristics**: Sub-nanosecond speeds; low density (6 transistors per bit); high power consumption; high cost per bit. No refreshing required. Used for processor register files and L1/L2/L3 caches.

---

### 4.2.2 Dynamic RAM (DRAM)
- **Cell Structure**: Exactly 1 NMOS access transistor and 1 microscopic storage capacitor (1T-1C cell, $C_s \approx 30 \times 10^{-15} \text{ F}$).
- **Storage Mechanism**: The presence of charge on capacitor $C_s$ represents a `1`; the absence of charge represents a `0`.
- **Destructive Read**: When $WL$ is asserted, the tiny charge on $C_s$ flows out onto the comparatively massive capacitance of the Bit Line ($C_{BL} \approx 10 \times C_s$), causing a minuscule voltage deflection ($\Delta V \approx 100 \text{ mV}$). The sense amplifier detects $\Delta V$ and **must immediately recharge (restore) the capacitor**.
- **Charge Leakage & Memory Refresh**: Charge leaks continuously across the reverse-biased NMOS p-n junctions and dielectric layers. A DRAM cell loses its data within tens of milliseconds unless refreshed.

#### Refresh Mechanisms:
DRAM arrays are organized into rows and columns. A **Refresh Cycle** reads an entire row of storage cells into the row sense amplifiers and automatically writes the full charge back into the capacitors.
- **Burst Refresh**: Normal memory access is suspended; all $R$ rows are refreshed back-to-back in a dedicated burst.
- **Distributed Refresh**: The refresh cycles are evenly spaced across the maximum refresh window $t_{ref}$.
  $$\text{Refresh Interval} = \frac{t_{\text{ref}}}{\text{Number of Rows } R}$$

```
Numerical Example: DRAM Refresh Overhead Calculation
  A 4 Gb DRAM chip has 8,192 rows (2^13 rows).
  The manufacturer specifies a maximum refresh interval t_ref = 64 ms.
  Each refresh cycle takes 50 ns.

  1. Required Refresh Interval per Row:
     Interval = 64 ms / 8192 rows = 64,000,000 ns / 8192 = 7,812.5 ns (~7.81 microseconds).
     A refresh cycle must be triggered every 7.81 microseconds.

  2. Percentage Refresh Overhead:
     Overhead (%) = (Time spent refreshing / Total time) * 100
     Overhead (%) = (8192 * 50 ns / 64 ms) * 100
                  = (409,600 ns / 64,000,000 ns) * 100 = 0.64%
     Only 0.64% of total DRAM memory bandwidth is consumed by refresh operations!
```

---

### 4.2.3 Master Comparison: SRAM vs DRAM

| Parameter | Static RAM (SRAM) | Dynamic RAM (DRAM) |
| :--- | :--- | :--- |
| **Cell Construction** | 6 Transistors (6T CMOS Bistable Latch) | 1 Transistor + 1 Trench Capacitor (1T-1C) |
| **Storage Principle** | Cross-coupled inverter voltage states | Electrical charge stored on capacitor |
| **Access Time** | **0.5 - 2.5 ns (Ultra Fast)** | **50 - 70 ns (Moderate)** |
| **Density (Bits/mm²)** | Low (large 6T footprint) | **Extremely High (compact 1T-1C cell)** |
| **Cost per Bit** | High (~100x DRAM) | Low |
| **Dynamic Refresh** | **None Required** | **Mandatory periodic refresh (~every 64 ms)** |
| **Read Destructiveness**| **Non-Destructive** | **Destructive** (requires automatic write-back) |
| **Power Consumption** | Low standby power; high active power | High standby power (refresh cycles) |
| **Typical Usage** | CPU Registers, L1, L2, L3 Caches | System Main Memory (DDR4 / DDR5 SDRAM) |

---

## 4.3 INTERNAL MEMORY ORGANIZATION: 2D VS 2.5D COINCIDENT DECODING

### 4.3.1 2D Memory Organization (Single Decoder)
In a pure 2D memory organization, a single address decoder of size $k \times 2^k$ is used:
- An input address of $k$ bits selects exactly one of $2^k$ horizontal **Word Lines**.
- When a Word Line is asserted, all $W$ bits of that word are driven onto vertical data lines simultaneously.
- **The Silicon Scalability Crisis**: For a 1 Megabyte memory ($2^{20}$ bytes):
  - Requires a 20-to-$1,048,576$ decoder!
  - Requires $1,048,576$ individual physical word lines running across the chip.
  - The silicon area, gate fan-out, and capacitive propagation delays make this completely impossible to fabricate.

---

### 4.3.2 2.5D / Coincident Decoding Organization
To solve the decoder scaling crisis, the memory cells are arranged as a 2-dimensional square matrix of $2^{k/2}$ rows and $2^{k/2}$ columns, controlled by **two separate, smaller decoders**:
1. **$X$-Decoder (Row Decoder)**: Decodes the upper $k/2$ address bits to select 1 horizontal row line.
2. **$Y$-Decoder (Column Decoder)**: Decodes the lower $k/2$ address bits to select 1 vertical column multiplexer gate.

```
ASCII Architecture: 2.5D Coincident Decoding Memory Array

                    Upper Address Bits (k/2)
                               |
                               v
                     +-------------------+
                     |  X-Decoder (Row)  |
                     +---+---+---+---+---+
                         |   |   |   |
          Row Line 0 ----+---+---+---+---- (Word Row 0)
                         |   |   |   |
          Row Line 1 ----+---+---+---+---- (Word Row 1)
                         |   |   |   |
                         |   |   |   |  Matrix of Cells:
                         |   |   |   |  A cell is selected ONLY
                         |   |   |   |  if BOTH its Row Line AND
                         |   |   |   |  Column Line are active!
                         |   |   |   |
                         v   v   v   v
                        [Column Sense / MUX]
                                 ^
                                 |
                     +-----------+-------+
                     | Y-Decoder (Column)|
                     +-------------------+
                                 ^
                                 |
                    Lower Address Bits (k/2)
```

#### Dramatic Hardware Savings:
For a 1 Megaword memory ($k = 20$ bits):
- **2D Organization**: Requires 1 decoder with $2^{20} = 1,048,576$ word lines.
- **2.5D Coincident Organization**:
  - $X$-Decoder size: 10-to-1024 (1024 row lines).
  - $Y$-Decoder size: 10-to-1024 (1024 column lines).
  - Total selection lines: $1024 + 1024 = 2,048$ lines.
  - **Hardware Reduction**: Reduces decoding lines from **1,048,576 down to 2,048** (a 512-fold reduction in physical wire routing and silicon area!).

---

## 4.4 READ-ONLY MEMORY (ROM) TECHNOLOGIES

| ROM Type | Erasure Mechanism | Programming Method | Erasure Granularity | Volatility | Practical Applications |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Mask ROM** | Non-erasable | Photolithography metallization mask during fabrication | None | Non-volatile | High-volume video game cartridges, factory hardcoded firmware |
| **PROM** | Non-erasable | Electrical fusing of nichrome/polysilicon links (OTP) | None (One-Time) | Non-volatile | Early microcontroller firmware |
| **EPROM** | High-intensity **Ultraviolet (UV) Light** through quartz window | Hot electron injection via high programming voltage ($V_{pp} = 12-25\text{V}$) | **Entire Chip** (20-30 min exposure) | Non-volatile | Legacy 1980s computer BIOS chips |
| **EEPROM** | Electrical field (**Fowler-Nordheim Tunneling**) | In-circuit electrical pulsing byte-by-byte | **Byte-Level** | Non-volatile | Calibration constants, device serial numbers |
| **Flash Memory** | Electrical field (Fowler-Nordheim Tunneling) | In-circuit electrical page programming | **Block-Level** | Non-volatile | Solid-state drives (SSDs), USB drives, smartphone storage |

### 4.4.1 NOR Flash vs NAND Flash Architecture
- **NOR Flash**: Memory cells connected in parallel to bit lines (similar to a NOR gate). Provides random access, byte-level read, fast read speeds, but lower density. Supports **eXecute In Place (XIP)**, allowing CPU to run machine code directly from flash without copying to RAM (used for Motherboard UEFI/BIOS).
- **NAND Flash**: Memory cells connected in series strings of 32 to 128 cells. Eliminates ground contacts, achieving ultra-high density and low cost. Reads and writes strictly in **Pages** (4 KB - 16 KB); erases strictly in **Blocks** (128 - 512 pages). Cannot execute code directly. Powers modern SSDs and smartphone storage.

---

## 4.5 CACHE MEMORY PERFORMANCE & AMAT FORMULATION

The cache is a small, ultra-fast semiconductor memory sitting between the CPU and Main Memory, holding copies of frequently accessed memory blocks.

```
ASCII Block Diagram: CPU Cache Interaction

   +---------------+          +---------------+          +---------------+
   |      CPU      |=========>|     Cache     |=========>|  Main Memory  |
   |   Registers   |<=========|  (SRAM Array) |<=========|  (DRAM Array) |
   +---------------+          +---------------+          +---------------+
                                Hit: ~1 ns                 Miss: ~60 ns
```

### 4.5.1 Cache Performance Formulations
1. **Hit Ratio ($H$)**: Fraction of memory accesses satisfied directly by the cache:
   $$H = \frac{\text{Cache Hits}}{\text{Total Memory Accesses}}$$
2. **Miss Ratio ($M$)**:
   $$M = 1 - H = \frac{\text{Cache Misses}}{\text{Total Memory Accesses}}$$
3. **Hit Time ($T_{hit}$)**: Time required to hit in the cache (including tag lookup, comparison, and data transfer).
4. **Miss Penalty ($T_{miss}$)**: Time required to fetch a complete memory block from Main Memory into the cache, replace an old block, and forward the requested word to the CPU.

### 4.5.2 Average Memory Access Time (AMAT)
$$\text{AMAT} = T_{hit} + (1 - H) \times T_{miss} = T_{hit} + M \times T_{miss}$$

#### Multi-Level Cache AMAT Formulation:
For a 2-level cache hierarchy (L1 and L2):
$$\text{AMAT} = T_{L1} + M_{L1} \times \left[ T_{L2} + M_{L2, \text{local}} \times T_{mem} \right]$$
where $M_{L2, \text{local}}$ is the local miss rate of L2.

```
Comprehensive Worked Numerical Problem: AMAT Calculation
  A processor has:
    - L1 Cache: Hit Time = 1 ns, Hit Ratio = 95% (Miss Ratio = 0.05)
    - L2 Cache: Hit Time = 5 ns, Hit Ratio = 80% (Local Miss Ratio = 0.20)
    - Main Memory Access Time = 60 ns

  Calculate AMAT:
    AMAT = T_L1 + M_L1 * [ T_L2 + M_L2 * T_mem ]
    AMAT = 1 ns + 0.05 * [ 5 ns + 0.20 * 60 ns ]
    AMAT = 1 ns + 0.05 * [ 5 ns + 12 ns ]
    AMAT = 1 ns + 0.05 * [ 17 ns ]
    AMAT = 1 ns + 0.85 ns = 1.85 ns

  Without L2 cache:
    AMAT_no_L2 = 1 ns + 0.05 * 60 ns = 1 ns + 3.0 ns = 4.0 ns.
  Adding L2 improves memory access speed by more than 2x!
```

---

## 4.6 CACHE MAPPING TECHNIQUES IN DEPTH

Main memory is divided into equal-sized blocks of $B = 2^w$ bytes. The cache is divided into cache lines (slots) of identical size $B$.

```
Address Bit Field Breakdown Across All 3 Mapping Techniques:

1. Direct Mapping:
   +----------------------+----------------------+----------------------+
   |      Tag (t)         |    Line Index (s)    |   Word Offset (w)    |
   +----------------------+----------------------+----------------------+

2. Fully Associative Mapping:
   +---------------------------------------------+----------------------+
   |                   Tag (t)                   |   Word Offset (w)    |
   +---------------------------------------------+----------------------+

3. k-Way Set-Associative Mapping:
   +----------------------+----------------------+----------------------+
   |      Tag (t)         |     Set Index (d)    |   Word Offset (w)    |
   +----------------------+----------------------+----------------------+
```

---

### 4.6.1 Direct Mapping Architecture
Each block of main memory maps to **exactly ONE predetermined cache line**:
$$\text{Line Index} = (\text{Block Address}) \pmod{\text{Total Cache Lines } L}$$
- **Bit Fields**:
  - $w = \log_2(\text{Block Size in bytes})$
  - $s = \log_2(\text{Total Cache Lines } L)$
  - $t = \text{Address Width} - s - w$
- **Hardware**: Requires exactly **one tag comparator**.
- **Pros**: Simplest hardware, lowest cost, fastest hit time.
- **Cons**: Severe **Conflict Misses (Thrashing)**. If two active memory blocks map to the identical line index, they continuously evict each other even if all other cache lines are empty!

---

### 4.6.2 Fully Associative Mapping Architecture
Any block of main memory can be placed into **ANY cache line**:
- **Bit Fields**:
  - $w = \log_2(\text{Block Size in bytes})$
  - $t = \text{Address Width} - w$ (No line index bits!).
- **Hardware**: Must compare the incoming address Tag simultaneously against the tags of **ALL $L$ cache lines** in parallel using $L$ hardware comparators or associative Content Addressable Memory (CAM).
- **Pros**: Zero conflict misses; highest possible hit ratio.
- **Cons**: Extremely expensive; hardware comparators become slow and power-hungry for large caches.

---

### 4.6.3 $k$-Way Set-Associative Mapping Architecture
The cache is partitioned into $S$ sets, where each set contains exactly $k$ cache lines ($k$-way):
$$\text{Total Sets } S = \frac{\text{Total Cache Lines } L}{k}$$
A main memory block maps to exactly ONE set, but can occupy **ANY of the $k$ lines within that set**:
$$\text{Set Index} = (\text{Block Address}) \pmod{S}$$
- **Bit Fields**:
  - $w = \log_2(\text{Block Size in bytes})$
  - $d = \log_2(\text{Number of Sets } S)$
  - $t = \text{Address Width} - d - w$
- **Hardware**: Requires exactly $k$ parallel tag comparators and a $k$-to-1 multiplexer.
- **Trade-off**: Bridges the gap between Direct and Associative. $k=2, 4, 8$ captures nearly all the miss-rate benefits of fully associative mapping while maintaining simple hardware.

---

### 4.6.4 Master Multi-Part Worked Numerical Problem

#### Given System Specifications:
- **Processor Address Bus**: 32 bits (Byte-addressable memory, 4 GiB physical space).
- **Cache Size**: 64 KiB ($64 \times 1024 = 65,536$ bytes).
- **Block Size**: 32 bytes.

#### Step 1: Fundamental Calculations:
- Word Offset Bits: $w = \log_2(32) = 5$ bits.
- Total Cache Lines: $L = \frac{\text{Cache Size}}{\text{Block Size}} = \frac{65,536}{32} = 2,048 \text{ lines} = 2^{11} \text{ lines}$.

#### Step 2: Bit Allocations Across All Modes:

```
Case A: Direct Mapping:
  - Offset (w)     = 5 bits
  - Line Index (s) = log2(2048) = 11 bits
  - Tag (t)        = 32 - 11 - 5 = 16 bits
  Address Fields: [ Tag: 16 bits | Line Index: 11 bits | Word Offset: 5 bits ]

Case B: Fully Associative Mapping:
  - Offset (w)     = 5 bits
  - Tag (t)        = 32 - 5 = 27 bits
  Address Fields: [ Tag: 27 bits | Word Offset: 5 bits ]

Case C: 4-Way Set-Associative Mapping (k = 4):
  - Number of Sets S = Total Lines / k = 2048 / 4 = 512 sets = 2^9 sets
  - Set Index (d)  = log2(512) = 9 bits
  - Offset (w)     = 5 bits
  - Tag (t)        = 32 - 9 - 5 = 18 bits
  Address Fields: [ Tag: 18 bits | Set Index: 9 bits | Word Offset: 5 bits ]

Case D: 8-Way Set-Associative Mapping (k = 8):
  - Number of Sets S = Total Lines / k = 2048 / 8 = 256 sets = 2^8 sets
  - Set Index (d)  = log2(256) = 8 bits
  - Offset (w)     = 5 bits
  - Tag (t)        = 32 - 8 - 5 = 19 bits
  Address Fields: [ Tag: 19 bits | Set Index: 8 bits | Word Offset: 5 bits ]
```

---

## 4.7 CACHE REPLACEMENT ALGORITHMS & WRITE POLICIES

### 4.7.1 Cache Replacement Algorithms (Associative / Set-Associative)
When a miss occurs and all $k$ lines in the target set are occupied, a replacement algorithm chooses which victim line to evict:
1. **Least Recently Used (LRU)**:
   - Evicts the block that has not been referenced for the longest period of time.
   - Best empirical hit ratio by exploiting temporal locality.
   - Hardware: Maintained using matrix age counters or small 2-bit timestamp registers.
2. **First-In, First-Out (FIFO)**:
   - Evicts the block that has resided in the cache set the longest, irrespective of recent accesses.
   - Implemented via a simple cyclic counter pointer.
3. **Least Frequently Used (LFU)**:
   - Evicts the block with the lowest reference count.
   - Vulnerable to historical pollution: a block used intensely during initialization may permanently remain in cache even after becoming obsolete (requires decay/aging counters).
4. **Random Replacement**:
   - Randomly selects a victim line using a pseudo-random number generator.
   - Requires zero bookkeeping overhead; surprisingly effective in large $N$-way caches.

---

### 4.7.2 Cache Write Policies

```
+--------------------------------------------------------------------------+
|                            CACHE WRITE POLICIES                          |
+------------------------------------+-------------------------------------+
|         ON A WRITE HIT             |          ON A WRITE MISS            |
+------------------------------------+-------------------------------------+
| 1. WRITE-THROUGH:                  | 1. WRITE-ALLOCATE:                  |
|    Update cache AND main memory    |    Fetch missing block into cache,  |
|    simultaneously. Memory is       |    then perform write.              |
|    always consistent.              |    (Typically paired with           |
|                                    |     Write-Back).                    |
+------------------------------------+-------------------------------------+
| 2. WRITE-BACK (COPY-BACK):         | 2. NO-WRITE-ALLOCATE:               |
|    Update ONLY cache; set Dirty    |    Write directly to Main Memory    |
|    Bit to 1. Write back to RAM     |    without loading block to cache.  |
|    ONLY when line is evicted!      |    (Typically paired with           |
|    Minimizes bus traffic.          |     Write-Through).                 |
+------------------------------------+-------------------------------------+
```

---

## 4.8 AUXILIARY & SECONDARY STORAGE: HARD DISKS & LATENCY FORMULAS

### 4.8.1 Magnetic Hard Disk Drive (HDD) Physical Architecture
- **Platters**: Rigid circular aluminium/glass disks coated with magnetic material spinning on a common spindle.
- **Tracks**: Concentric circular rings on each platter surface where bits are magnetically recorded.
- **Sectors**: Segments of a track (standard: 512 bytes or 4,096 bytes / Advanced Format).
- **Cylinder**: The set of all tracks across all platter surfaces located at identical radial distances from the spindle.
- **Read/Write Heads**: Aerodynamically flying heads suspended on a movable actuator arm.

```
ASCII Diagram: Hard Disk Platter and Track-Sector Layout

                  Track (Concentric Circle)
                       |
               +-------v-------+
             /   Sector (512B)   \
            /       |             \
           |     +--v--+           |
           |    /       \          |
           |   | Spindle |         |
           |    \       /          |
           |     +-----+           |
            \                     /
             \                   /
               +---------------+
```

### 4.8.2 Disk Access Time Mathematical Formulation
The total time to read or write a sector on a magnetic disk is:
$$T_{\text{disk}} = T_{\text{seek}} + T_{\text{rotational}} + T_{\text{transfer}} + T_{\text{controller}}$$

1. **Seek Time ($T_{\text{seek}}$)**: The mechanical time required for the actuator arm to physically move the read/write head to the designated track/cylinder.
2. **Rotational Latency ($T_{\text{rotational}}$)**: The time elapsed while waiting for the requested sector to rotate beneath the read/write head. On average, the disk rotates half a revolution:
   $$T_{\text{rotational}} = \frac{1}{2} \times \left( \frac{60}{\text{RPM}} \right) \text{ seconds}$$
3. **Transfer Time ($T_{\text{transfer}}$)**: The time required to transfer the data bits:
   $$T_{\text{transfer}} = \frac{\text{Bytes to Transfer}}{\text{Data Transfer Rate (Bytes/sec)}}$$
4. **Controller Overhead**: Electronic processing delay imposed by the disk drive controller.

```
Numerical Example: Total Disk Access Time Calculation
  Disk Specifications:
    - Rotational Speed: 7,200 RPM
    - Average Seek Time: 8 ms (0.008 s)
    - Data Transfer Rate: 100 MB/s (100 * 10^6 bytes/s)
    - Controller Overhead: 0.5 ms (0.0005 s)
    - Sector Size to Read: 4,096 bytes (4 KB)

  Step 1: Rotational Latency:
    1 revolution takes: 60 / 7200 = 0.008333 seconds = 8.33 ms.
    Average Latency = 8.33 ms / 2 = 4.17 ms.

  Step 2: Transfer Time:
    Transfer Time = 4096 / (100 * 10^6) = 0.00004096 seconds = 0.041 ms.

  Step 3: Total Average Disk Access Time:
    T_disk = 8.0 ms (seek) + 4.17 ms (latency) + 0.041 ms (transfer) + 0.5 ms (overhead)
    T_disk = 12.711 ms.
  Mechanical motion accounts for over 95% of total disk delay!
```

---

## 4.9 VIRTUAL MEMORY: PAGING, TLB, & PAGE FAULTS

Virtual memory provides an abstract, uniform address space to software processes, completely decoupled from physical DRAM.

### 4.9.1 Address Translation in Paging Systems
The address generated by the CPU is a **Virtual (Logical) Address**:
$$\text{Virtual Address: } [\text{Virtual Page Number (VPN)} \mid \text{Page Offset } (p)]$$
Main memory is partitioned into physical blocks of identical size called **Page Frames**:
$$\text{Physical Address: } [\text{Physical Frame Number (PFN)} \mid \text{Page Offset } (p)]$$
The **Page Table Base Register (PTBR)** holds the physical starting address of the process's page table in DRAM.

```
ASCII Address Translation Diagram:

  Virtual Address (from CPU):
  +-------------------------+----------------------+
  | Virtual Page Number(VPN)|   Page Offset (p)    |
  +------------+------------+----------+-----------+
               |                       |
               | (Index)               |
               v                       |
  Page Table:                          |
  +-----+------------------+           |
  | VPN | PFN | V | D | R  |           |
  +-----+-----+---+---+----+           |
  | ... | ... |   |   |    |           |
  | VPN | PFN | 1 | 0 | 1  |---+       |
  | ... | ... |   |   |    |   |       |
  +-----+-----+---+---+----+   |       |
                               v       v
  Physical Address (to RAM):
  +-------------------------+----------------------+
  |Physical Frame Num (PFN) |   Page Offset (p)    |
  +-------------------------+----------------------+
```

#### Page Table Entry (PTE) Flags:
- **PFN**: The physical frame number in RAM.
- **Valid / Present Bit ($V$)**: `1` = page resides in physical RAM; `0` = page is currently on disk swap space (**Page Fault**).
- **Dirty Bit ($D$)**: `1` = page was modified while in RAM (must be written back to disk on eviction).
- **Referenced / Access Bit ($R$)**: Set whenever page is read or written (used by LRU clock replacement).
- **Protection Bits**: Specify Read, Write, and Execute permissions.

---

### 4.9.2 Translation Lookaside Buffer (TLB) & Effective Access Time
Because the page table resides in main memory, every single CPU memory reference requires **two sequential memory accesses**:
1. Access memory to fetch the Page Table Entry.
2. Access memory to read/write the actual operand.

The **Translation Lookaside Buffer (TLB)** is a small, ultra-fast associative cache in the CPU MMU that caches recent $VPN \to PFN$ translations.

#### Effective Memory Access Time (EMAT) with TLB:
Let $T_{TLB}$ be TLB access time, $T_{mem}$ be main memory access time, and $H_{TLB}$ be the TLB Hit Ratio:
$$\text{EMAT} = T_{TLB} + H_{TLB} \times T_{mem} + (1 - H_{TLB}) \times (2 \times T_{mem})$$

```
Numerical Example: EMAT Calculation
  TLB Hit Ratio H_TLB = 98% (0.98)
  TLB Lookup Time = 2 ns
  Main Memory Access Time = 50 ns

  EMAT = 2 ns + [ 0.98 * 50 ns ] + [ (1 - 0.98) * (2 * 50 ns) ]
  EMAT = 2 ns + 49 ns + [ 0.02 * 100 ns ]
  EMAT = 2 ns + 49 ns + 2 ns = 53 ns.
  Without TLB, access time would be 2 * 50 = 100 ns. The TLB cuts latency nearly in half!
```

---

### 4.9.3 Page Fault Handling Sequence
A **Page Fault** is a precise hardware exception raised by the MMU when a program references a virtual page whose Valid bit in the Page Table is `0`:

```
Step-by-Step Page Fault Handling Flow:

1. CPU references virtual address -> MMU detects Valid Bit = 0 in Page Table.
2. MMU raises Page Fault Trap (Internal Interrupt) to CPU.
3. CPU saves current context (PC, registers) and switches to OS Kernel Mode.
4. OS Page Fault Handler executes; locates missing page on Secondary Disk Swap space.
5. OS selects a victim page frame in RAM (using LRU / Clock algorithm).
6. If victim page is Dirty (D = 1), write victim page back to disk.
7. Issue asynchronous DMA read to transfer requested page from disk into free frame.
8. CPU yields to scheduler (executes other ready processes during disk I/O).
9. DMA transfer completes; disk controller asserts I/O interrupt.
10. OS updates Page Table: sets PFN to new frame, sets Valid bit = 1.
11. OS restarts the faulting instruction from the saved PC.
```

---

### 4.9.4 Segmentation vs Paging Comparative Analysis

| Feature | Paging | Segmentation |
| :--- | :--- | :--- |
| **Programmer Visibility** | **Completely Invisible** (Handled transparently by OS/hardware) | **Visible to Programmer** (Code, Data, Stack organized logically) |
| **Block Size** | **Fixed Size** (e.g., exactly 4 KiB) | **Variable Size** (Length matches segment contents) |
| **Address Structure** | Single linear address divided into $[VPN \mid \text{Offset}]$ | Two-part address: $[\text{Segment Number} \mid \text{Offset}]$ |
| **Internal Fragmentation** | **Suffers from Internal Fragmentation** (average half page per process) | **Zero Internal Fragmentation** |
| **External Fragmentation** | **Zero External Fragmentation** (any frame fits any page) | **Suffers from External Fragmentation** (memory compaction needed) |
| **Protection & Sharing** | Difficult to share logical procedures cleanly | Natural and intuitive (shared libraries, read-only code segments) |

---

## 4.10 UNIT 4 HIGH-PROBABILITY EXAM QUESTIONS & STEP-BY-STEP SOLUTIONS

### Q1: A system has a 32-bit byte-addressable address space, a 128 KiB cache, and a block size of 64 bytes. Calculate the Tag, Index, and Offset bits under (a) Direct Mapping and (b) 4-Way Set-Associative Mapping.
**Solution**:
1. Offset bits: $w = \log_2(64) = 6$ bits.
2. Direct Mapping:
   - Total Cache Lines $L = \frac{128 \times 1024}{64} = 2048$ lines.
   - Index bits $s = \log_2(2048) = 11$ bits.
   - Tag bits $t = 32 - 11 - 6 = 15$ bits.
   - Breakdown: $[Tag: 15 \mid Line: 11 \mid Offset: 6]$.
3. 4-Way Set-Associative Mapping:
   - Sets $S = \frac{2048}{4} = 512$ sets.
   - Set Index bits $d = \log_2(512) = 9$ bits.
   - Tag bits $t = 32 - 9 - 6 = 17$ bits.
   - Breakdown: $[Tag: 17 \mid Set: 9 \mid Offset: 6]$.

### Q2: Compare Write-Through and Write-Back cache policies across bus traffic, consistency, and eviction complexity.
**Solution**:
- **Bus Traffic**: Write-through incurs high bus traffic (every write goes to RAM); Write-back minimizes traffic (writes stay in cache, written back only on dirty eviction).
- **Consistency**: Write-through guarantees RAM is always 100% consistent; Write-back leaves RAM temporarily inconsistent.
- **Eviction Complexity**: Write-through evicts cleanly in 0 memory write cycles; Write-back requires checking the Dirty Bit and writing modified blocks to memory on eviction.

---

## 4.11 UNIT 4 COMMON TRAPS, PITFALLS, AND CONCEPT CHECKS

> [!CAUTION]
> **Trap 1: Byte vs Word Offset!**  
> Always check if the architecture is **Byte-Addressable** or **Word-Addressable**! If memory is byte-addressable and block size is 32 bytes, Offset is $\log_2(32) = 5$ bits. If word-addressable (4 bytes/word), Offset is $\log_2(32/4) = \log_2(8) = 3$ bits.

> [!WARNING]
> **Trap 2: Local Miss Rate vs Global Miss Rate in Multi-Level Caches!**  
> Local miss rate $M_{\text{local}}$ is misses per access to that specific cache. Global miss rate $M_{\text{global}}$ is misses per CPU instruction reference ($M_{\text{global}} = M_{L1} \times M_{L2, \text{local}}$).

# UNIT 5: INPUT / OUTPUT ORGANIZATION & PERIPHERALS

---

## 5.1 PERIPHERAL DEVICES, I/O INTERFACE, & ISOLATED VS MEMORY-MAPPED I/O

### 5.1.1 The Need for an I/O Interface
Peripherals cannot connect directly to the system bus for several fundamental architectural reasons:
1. **Speed Mismatch**: Processor and memory operate at electronic nanosecond speeds (gigahertz clocks), whereas electromechanical peripherals (disks, keyboards, printers) operate at millisecond speeds.
2. **Signal Level & Data Format Mismatch**: CPU internal data is parallel binary logic levels ($0\text{V} / 1.2\text{V}$ TTL/CMOS), while peripherals may use serial bit streams, analog voltages, optical signals, or high-voltage differential levels.
3. **Word Length & Protocol Differences**: Peripherals transmit data in formats (e.g., ASCII characters, network packets) that differ from the processor's word width.

```
ASCII Architecture: Generic I/O Interface Module

                      System Bus
   ==================================================
           | Address Bus   | Data Bus    | Control Bus
           |               |             | (IOR, IOW)
           v               v             v
   +---------------+---------------+---------------+
   |               I/O INTERFACE MODULE            |
   |                                               |
   |  +--------------------+   +----------------+  |
   |  |  Address Decoder   |   | Control Logic  |  |
   |  +---------+----------+   +--------+-------+  |
   |            |                       |          |
   |  +---------v----------+   +--------v-------+  |
   |  |   Data Register    |   | Status Register|  |   Peripheral
   |  |   (Input/Output)   |   | (Ready, Busy)  |  |   Handshake Lines
   |  +---------+----------+   +--------+-------+  |   (Data, Strobe,
   |            |                       |          |    Acknowledge)
   +------------+-----------------------+----------+        |
                | Data                  | Status            |
                v                       v                   v
   +-------------------------------------------------------+
   |                  PERIPHERAL DEVICE                    |
   +-------------------------------------------------------+
```

### 5.1.2 Internal Registers of an I/O Interface:
1. **Data In / Data Out Register**: Buffers parallel data moving between the system bus and the peripheral.
2. **Status Register**: Contains operational flags set by the device (e.g., `DATA_READY`, `BUSY`, `ERROR`, `PARITY_ERR`).
3. **Control (Command) Register**: Configures peripheral operating modes (e.g., baud rate, transfer direction, interrupt enable).

---

### 5.1.3 Isolated I/O (Port-Mapped) vs Memory-Mapped I/O

```
Address Space Comparison:

  Isolated I/O (Intel x86 / 8085):
  +--------------------------+   +--------------------------+
  |    Memory Address Space  |   |     I/O Address Space    |
  |     (0000H to FFFFH)     |   |      (00H to FFH)        |
  |    Accessed via MEMR/W   |   |    Accessed via IN/OUT   |
  +--------------------------+   +--------------------------+

  Memory-Mapped I/O (ARM / MIPS / Motorola):
  +---------------------------------------------------------+
  |             Single Unified Address Space                |
  |  +---------------------------------------------------+  |
  |  | Main RAM Storage Locations (00000000H to DFFFFFFFH)|  |
  |  +---------------------------------------------------+  |
  |  | I/O Device Registers / Ports (E0000000H - FFFFFFFFH)|  |
  |  +---------------------------------------------------+  |
  |         All accessed via standard LOAD / STORE          |
  +---------------------------------------------------------+
```

#### Master Comparative Analysis:

| Architectural Metric | Isolated I/O (Port-Mapped I/O) | Memory-Mapped I/O |
| :--- | :--- | :--- |
| **Address Space** | **Separate address spaces** for Memory and I/O devices | **Single unified address space** shared by Memory and I/O |
| **CPU Instructions** | Requires dedicated I/O instructions (`IN`, `OUT`) | Standard memory instructions (`MOV`, `LOAD`, `STORE`, `ADD`) |
| **Control Bus Signals** | **Distinct control lines**: `MEMR`, `MEMW`, `IOR`, `IOW` | **Unified control lines**: `MEMR`, `MEMW` (or `R/W`) |
| **Address Bus Usage** | Device addresses can overlap memory addresses without conflict | Each I/O register consumes a valid memory address |
| **Addressing Modes** | Very limited (typically register or direct port only) | **Full rich set of addressing modes** applies directly to I/O |
| **Memory Space Impact**| Preserves 100% of physical memory address space | Reduces available memory space by the number of mapped ports |
| **Hardware Decoding** | Simpler decoding (fewer address lines, e.g. 8 or 16 bits) | Full-width address decoding (e.g., 32 or 64 bits) |
| **Typical Processors** | Intel x86, 8085, Z80 | ARM, MIPS, RISC-V, PowerPC, Motorola 68000 |

---

## 5.2 MODES OF DATA TRANSFER

Data transfer between the computer system and I/O peripherals occurs via three primary modes:

```
+--------------------------------------------------------------------------+
|                         MODES OF DATA TRANSFER                           |
+--------------------+--------------------------------+--------------------+
| 1. Programmed I/O  | 2. Interrupt-Initiated I/O     | 3. Direct Memory   |
|    (Polling Loop)  |    (Event-Driven ISR)          |    Access (DMA)    |
+--------------------+--------------------------------+--------------------+
| CPU 100% tied up;  | CPU free for background tasks; | High-speed block   |
| busy-waits for     | peripheral interrupts CPU      | transfer; DMAC     |
| ready flag.        | when ready.                    | moves data to RAM. |
+--------------------+--------------------------------+--------------------+
```

---

### 5.2.1 Programmed I/O (Polling)
- **Mechanism**: The CPU executes an explicit software polling loop, continuously reading the Status Register of the peripheral interface and checking if the `READY` bit is set.
- **Workflow**:
  ```
  POLL: IN   STATUS_PORT       ; Read peripheral status
        TEST READY_BIT         ; Check if data is ready
        JZ   POLL              ; If 0 (not ready), loop back and wait!
        IN   DATA_PORT         ; Read data byte into Accumulator
        MOV  M[DEST], AC       ; Store into RAM
  ```
- **Trade-Off**:
  - *Advantage*: Minimum hardware complexity; requires no interrupt controller or DMA circuitry.
  - *Disadvantage*: **Disastrous CPU Inefficiency**. The CPU spends millions of clock cycles in an idle busy-wait loop, entirely unable to perform productive computation.

---

### 5.2.2 Interrupt-Initiated I/O
- **Mechanism**: The CPU issues a command to the peripheral interface and immediately returns to executing other background applications.
- When the peripheral finishes assembling data, it asserts a hardware **Interrupt Request line ($INTR$)**.
- The CPU suspends the current program at the next instruction boundary, saves its architectural state (Program Counter and Flags) to the stack, and branches to the **Interrupt Service Routine (ISR)**.
- The ISR reads/writes data and executes `IRET` (Interrupt Return) to resume the background application.
- **Trade-Off**: Maximizes CPU utilization, but incurs a software context-switching overhead (saving/restoring registers).

---

### 5.2.3 Direct Memory Access (DMA)
For high-speed block devices (NVMe/SATA SSDs, hard disks, gigabit Ethernet), handling transfers byte-by-byte via CPU interrupts would overload the processor. **DMA** transfers an entire block of data directly between the peripheral and Main Memory without passing through CPU registers!

```
ASCII Architecture: Direct Memory Access Controller (DMAC) Interaction

                    +-----------------------+
                    |          CPU          |
                    +-----+-----------+-----+
                          |           ^
                 Bus Hold | HOLD      | HLDA (Hold Acknowledge /
                 Request  |           |       Bus Grant)
                          v           |
                    +-----+-----------+-----+
                    |     DMA CONTROLLER    |<==== DREQ (DMA Request)
                    |         (DMAC)        |====> DACK (DMA Acknowledge)
                    +-----+-----------+-----+
                          |           |
             Address Bus  |           | Control Bus (MEMR, MEMW, IOR, IOW)
                          v           v
   ========================================================================
   ======================= SHARED SYSTEM BUS ==============================
           |                                       |
           v                                       v
   +---------------+                       +---------------+
   |  Main Memory  |                       |  I/O Device   |
   |    (RAM)      |                       | (Disk / NIC)  |
   +---------------+                       +---------------+
```

#### Internal Architecture of DMA Controller:
1. **Address Register**: Holds the physical RAM memory address for the next byte/word transfer. Automatically incremented after each word transfer.
2. **Word Count Register**: Initialized to the total number of words to transfer. Automatically decremented after each transfer.
3. **Control & Status Registers**: Holds mode configuration, transfer direction, and interrupt status.

#### DMA Handshake & Transfer Protocol:
1. **Initialization**: The CPU programs the DMAC with:
   - Starting physical memory address.
   - Number of words to transfer (Word Count).
   - Transfer direction (Read from memory / Write to memory).
2. **Peripheral Request**: The I/O device asserts `DREQ` (DMA Request) to the DMAC.
3. **Bus Hold Request**: The DMAC asserts `HOLD` (Bus Request `BR`) to the CPU.
4. **Bus Relinquishment**: The CPU finishes the current machine bus cycle, places its address, data, and control lines into a **High-Impedance ($Hi-Z$)** disconnected state, and asserts `HLDA` (Hold Acknowledge / Bus Grant `BG`) to the DMAC.
5. **Direct Data Transfer**: The DMAC asserts `DACK` to the peripheral, drives the Address Bus and Control Bus, and transfers data directly between the I/O interface and RAM.
6. **Cycle Completion**: The DMAC increments Address Register and decrements Word Count.
7. **Termination**: When Word Count reaches `0`, the DMAC deasserts `HOLD` (releasing the system bus back to the CPU) and asserts an **Interrupt Request ($INTR$)** to notify the CPU that block transfer is complete.

---

### 5.2.4 DMA Operating Modes

| DMA Mode | Bus Ownership Behavior | CPU Impact | Ideal Real-World Use Case |
| :--- | :--- | :--- | :--- |
| **Burst Mode** (Block Transfer) | DMAC retains continuous control of system bus until the **entire block** is transferred ($WC = 0$). | CPU is **completely locked out** of the system bus during transfer. | High-speed magnetic disk or SSD page reads. |
| **Cycle Stealing Mode** | DMAC takes control of the bus for **exactly ONE bus cycle**, transfers 1 word, then releases bus back to CPU. | CPU is delayed by only 1 clock cycle; continues processing. | Medium-speed peripherals (keyboards, serial ports, audio). |
| **Transparent Mode** (Hidden DMA) | DMAC transfers data **only during clock phases when the CPU is not using the bus** (e.g. during ALU execution). | **Zero CPU slowdown**; bus contention is eliminated. | Highly specialized real-time DSP systems. |

---

## 5.3 INTERRUPT HARDWARE, PRIORITY RESOLUTION, & THE INTERRUPT CYCLE

### 5.3.1 Classification of Interrupts
1. **External Hardware Interrupts**:
   - Initiated by external I/O devices via electrical pins on the CPU.
   - **Maskable Interrupts**: Can be enabled or disabled via software instructions (`EI`, `DI`).
   - **Non-Maskable Interrupts (NMI)**: Highest priority hardware interrupt that cannot be masked; reserved for catastrophic system events (power failure, memory bus parity error).
2. **Internal Hardware Interrupts (Traps / Exceptions)**:
   - Synchronous events generated internally by the CPU due to illegal program conditions:
     - Division by zero ($x / 0$)
     - Arithmetic overflow
     - Invalid machine opcode
     - Memory protection violation / Page fault
   - Cannot be disabled by software.
3. **Software Interrupts**:
   - Explicit program instructions inserted by the compiler or programmer (e.g., `INT 21H`, `SYSCALL`).
   - Used to execute **System Calls**, switching privilege from User Mode to Kernel Mode.

---

### 5.3.2 The Interrupt Cycle (Microoperations)
At the completion of the execute phase of every instruction, the CPU tests the state of the Interrupt Flip-Flop ($IEN$) and Interrupt Request line ($R$):
If $IEN = 1$ and $R = 1$, the CPU enters the **Interrupt Cycle**:
- $T_0': AR \leftarrow 0, \quad TR \leftarrow PC$  
  *(Reset AR to reserved interrupt vector location 0; save PC into temporary register TR)*
- $T_1': M[AR] \leftarrow TR, \quad PC \leftarrow 0$  
  *(Store return address in memory location 0; reset PC)*
- $T_2': PC \leftarrow PC + 1, \quad IEN \leftarrow 0, \quad R \leftarrow 0, \quad SC \leftarrow 0$  
  *(Set PC to address 1 to begin executing ISR; disable further interrupts)*

---

### 5.3.3 Priority Resolution Schemes
When multiple peripherals request interrupts simultaneously, the CPU must resolve priority:

#### 1. Software Polling:
A single common interrupt line is shared by all devices. When asserted, the CPU branches to a polling routine that tests the status bit of each device sequentially. 
- *Advantage*: Very simple hardware.
- *Disadvantage*: Slow; latency to reach the lowest-priority device is large.

#### 2. Daisy-Chaining Priority (Hardware Serial Vectored)

```
ASCII Architecture: Daisy-Chained Priority Interrupt

                 +-------------------+
                 |        CPU        |
                 +---+-----------+---+
                     |           ^
                INTA |           | INTR (Common Wired-OR line)
                     v           |
              +--------------+   |   +--------------+       +--------------+
              |   Device 1   +---+-->|   Device 2   +------>|   Device 3   |
              |  (Highest)   | PI PO |   (Medium)   | PI PO |   (Lowest)   |
              +-------+------+       +-------+------+       +-------+------+
                      |                      |                      |
                      +----------------------+----------------------+
                                             |
                                    Data Bus (Vector Address)
```

- **Mechanism**:
  - The Interrupt Acknowledge signal ($INTA$) originates from the CPU and is chained in series from Device 1 through Device $N$.
  - Each device has a Priority In ($PI$) input and a Priority Out ($PO$) output.
  - If Device 1 requested an interrupt: it intercepts $INTA$, pulls its $PO = 0$ (blocking all downstream devices), and drives its **8-bit Vector Address** directly onto the Data Bus.
  - If Device 1 did not request an interrupt: it passes $INTA$ through ($PO = 1$) to Device 2.
- **Characteristics**: Fast vectored hardware dispatch; fixed serial priority; downstream devices can starve.

#### 3. Parallel Priority Controller (e.g., Intel 8259A PIC)
- Uses separate, dedicated interrupt request lines ($IR_0$ through $IR_7$) for each peripheral.
- Contains an **Interrupt Request Register (IRR)**, **Priority Resolver logic**, and **In-Service Register (ISR)**.
- Resolves highest-priority active interrupt in a single clock cycle and drives a programmable 8-bit vector address onto the data bus pointing directly into the **Interrupt Vector Table (IVT)**.

---

## 5.4 I/O CHANNELS AND INDEPENDENT I/O PROCESSORS (IOP)

In high-performance mainframe computer systems (IBM zSeries), offloading I/O management from the CPU led to the development of **I/O Channels** and **I/O Processors (IOP)**.

```
ASCII Hierarchy: Progression of I/O Control Architecture

  CPU Direct Control  -->  Interrupt-Driven I/O  -->  DMA Controller  -->  I/O Channel  -->  I/O Processor (IOP)
```

### 5.4.1 I/O Channels
An **I/O Channel** is a specialized hardware execution unit that runs its own dedicated program consisting of **Channel Command Words (CCW)** stored in main memory.
1. **Selector Channel**: Controls multiple high-speed devices, but connects to **only one device at a time** for high-volume block data streaming (e.g. disk storage subsystems).
2. **Multiplexer Channel**:
   - **Byte-Multiplexer**: Interleaves single bytes of data from hundreds of low-speed devices (keyboards, terminals, printers) simultaneously.
   - **Block-Multiplexer**: Interleaves complete blocks of data from multiple medium-to-high speed peripherals concurrently.

### 5.4.2 I/O Processor (IOP)
An **I/O Processor (IOP)** is a fully autonomous computer system with its own CPU instruction set, local memory, and ALU dedicated entirely to handling all system I/O operations, completely decoupling the host CPU from device protocols.

---

## 5.5 SERIAL COMMUNICATION PROTOCOLS & INTERFACES

Data transmission between systems is categorized into **Parallel** (all bits of a word transmitted simultaneously across multiple copper wires) and **Serial** (bits transmitted sequentially one by one over a single pair of wires).

```
ASCII Comparison: Asynchronous Serial Framing vs Synchronous Block Framing

Asynchronous Serial Character Framing:
  Idle (1) | Start (0) | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | Parity | Stop (1) | Stop (1) | Idle (1)
  ---------+-----------+----+----+----+----+----+----+----+----+--------+----------+----------+---------
            |<------------------- One Character Frame ------------------->|

Synchronous Serial Block Framing:
  +---------+---------+----------------------------------------------+---------+
  | SYN (1) | SYN (2) | Data Block Bytes (Hundreds to Thousands)     |   CRC   |
  +---------+---------+----------------------------------------------+---------+
```

### 5.5.1 Asynchronous Serial Transmission (UART)
- **Framing**: Each byte is framed individually by a **Start Bit** (`0`), 5 to 8 **Data Bits**, an optional **Parity Bit**, and 1 or 2 **Stop Bits** (`1`).
- **Clocking**: No clock signal is transmitted. The receiver maintains an independent local oscillator running at $16\times$ the baud rate. The receiver resynchronizes its bit sampling clock on the falling edge of the Start Bit.
- **Overhead**: For an 8-bit character with 1 start bit, 1 parity bit, and 1 stop bit, a total of 11 bits are transmitted to send 8 bits of payload ($27.3\%$ framing overhead).

### 5.5.2 Synchronous Serial Transmission
- **Framing**: Data is transmitted as large continuous blocks (hundreds or thousands of bytes) without individual character start/stop bits.
- **Clocking**: A shared clock line is transmitted alongside the data, or clock pulses are embedded directly into the data stream via Manchester encoding.
- **Synchronization**: The block begins with one or two unique **SYN (Synchronization)** characters (ASCII `16H` = `00010110_2`). Once the receiver matches the SYN pattern, all subsequent bits are grouped into 8-bit words in strict lockstep.
- **Overhead**: Negligible (< 1%), providing maximum bandwidth efficiency for high-speed network communication.

---

### 5.5.3 Baud Rate vs Bit Rate
- **Baud Rate ($B$)**: The number of signal state transitions (modulation symbols) per second transmitted across the physical communication channel.
- **Bit Rate ($R$)**: The actual number of information bits transmitted per second.
  $$R = B \times \log_2(M)$$
  where $M$ is the number of distinct signal states (modulation levels).
  *(When binary signaling is used with 2 voltage levels, $M = 2 \implies \log_2(2) = 1 \implies \text{Bit Rate} = \text{Baud Rate}$)*.

---

### 5.5.4 Standard Communication Interfaces

#### 1. RS-232-C Serial Interface:
- Established standard for point-to-point asynchronous serial data communication.
- **Bipolar Signal Voltages**:
  - Logic `1` (Mark / Idle): $-3\text{V}$ to $-15\text{V}$.
  - Logic `0` (Space): $+3\text{V}$ to $+15\text{V}$.
- **Primary Signals (DB-9 / DB-25 Connector)**:
  - `TXD`: Transmitted Data
  - `RXD`: Received Data
  - `RTS`: Request to Send (from DTE)
  - `CTS`: Clear to Send (from DCE)
  - `DTR`: Data Terminal Ready
  - `DSR`: Data Set Ready
  - `GND`: Signal Ground

#### 2. Universal Serial Bus (USB):
- **Topology**: Tiered Star topology connecting up to 127 devices through a single USB host controller.
- **Signaling**: Half-duplex differential signaling over twisted pair conductors ($D+$ and $D-$):
  - Logic `1`: $D+ > 2.8\text{V}$ and $D- < 0.3\text{V}$.
  - Logic `0`: $D- > 2.8\text{V}$ and $D+ < 0.3\text{V}$.
- **Encoding**: Non-Return-to-Zero Inverted (NRZI) with Bit Stuffing (a `0` is inserted after every six consecutive `1`s to guarantee clock transitions).
- **USB Transfer Types**:
  1. *Control Transfers*: Device enumeration and host configuration.
  2. *Bulk Transfers*: Large, non-time-critical data with error correction (flash drives, printers).
  3. *Interrupt Transfers*: Small, periodic, low-latency polling (mice, keyboards).
  4. *Isochronous Transfers*: Guaranteed real-time bandwidth without retransmission (audio streaming, video webcams).

---

## 5.6 UNIT 5 HIGH-PROBABILITY EXAM QUESTIONS & STEP-BY-STEP SOLUTIONS

### Q1: Differentiate between Isolated I/O and Memory-Mapped I/O across 5 distinct architectural criteria.
**Solution**:
1. **Address Space**: Isolated I/O maintains separate address spaces for memory and I/O; Memory-mapped I/O uses a single unified address space.
2. **Instructions**: Isolated I/O requires dedicated `IN` and `OUT` instructions; Memory-mapped I/O uses standard `LOAD`, `STORE`, and arithmetic instructions.
3. **Control Signals**: Isolated I/O uses dedicated `IOR` and `IOW` control lines; Memory-mapped I/O uses standard `MEMR` and `MEMW` lines.
4. **Addressing Modes**: Isolated I/O supports limited port addressing; Memory-mapped I/O supports all CPU addressing modes (indirect, indexed, base register).
5. **Memory Capacity**: Isolated I/O preserves the full memory address space; Memory-mapped I/O reduces available RAM address space by the number of mapped I/O ports.

### Q2: Explain the step-by-step handshake sequence of a DMA transfer from peripheral to memory.
**Solution**:
1. CPU initializes DMAC registers: Address Register with start address, Word Count Register with byte count, and Control Register with write mode.
2. Peripheral asserts `DREQ` (DMA Request) when data block is ready.
3. DMAC asserts `HOLD` (Bus Request) to the CPU.
4. CPU completes its current bus cycle, floats its address, data, and control lines into high-impedance ($Hi-Z$), and asserts `HLDA` (Hold Acknowledge) to DMAC.
5. DMAC asserts `DACK` to peripheral, drives target address on Address Bus, asserts `MEMW` and `IOR`, causing data to move directly from device to RAM.
6. DMAC decrements Word Count and increments Address Register after each transfer.
7. When Word Count reaches zero, DMAC releases `HOLD` line and asserts an Interrupt line to notify CPU transfer is finished.

---

## 5.7 UNIT 5 COMMON TRAPS, PITFALLS, AND CONCEPT CHECKS

> [!CAUTION]
> **Trap 1: DMA Arbitration vs DMA Transfer Mode!**  
> Bus Arbitration determines *who* gets ownership of the shared system bus (Daisy Chaining, Polling, Independent Request). DMA Transfer Mode determines *how* the DMAC uses the bus once ownership is granted (Burst Mode, Cycle Stealing, Transparent Mode).

> [!WARNING]
> **Trap 2: RS-232 Inverted Logic Levels!**  
> In RS-232-C, a negative voltage ($-3\text{V}$ to $-15\text{V}$) represents Logic `1` (Mark), and a positive voltage ($+3\text{V}$ to $+15\text{V}$) represents Logic `0` (Space). Connecting TTL logic directly to RS-232 without level-shifter transceivers (like the MAX232) will destroy the silicon chip!

# SECTION 6: COMPLETE EXECUTABLE C++ HARDWARE ALGORITHM SIMULATORS

To bridge theoretical computer architecture with concrete hardware execution, this section provides fully self-contained, heavily commented C++ implementations of the core CSA algorithms. These programs can be directly compiled and run with any C++17 compatible compiler (`g++ -std=c++17 program.cpp -o program`).

---

## 6.1 BOOTH'S SIGNED MULTIPLICATION SIMULATOR

```cpp
/**
 * @file booth_multiplication.cpp
 * @brief Bit-Level Hardware Emulation of Booth's Multiplication Algorithm (Radix-2)
 * @course Computer System Architecture (ITDC0209)
 */

#include <iostream>
#include <iomanip>
#include <bitset>
#include <cstdint>

// Display n-bit binary representation of an integer
template<size_t N>
std::string to_binary(int32_t val) {
    std::bitset<N> bits(val);
    return bits.to_string();
}

/**
 * Executes Booth's Algorithm step-by-step for N-bit 2's complement numbers.
 * @param M Multiplicand (signed)
 * @param Q Multiplier (signed)
 * @return 2N-bit signed product in [A, Q]
 */
template<size_t N>
int64_t booth_multiply(int32_t M, int32_t Q) {
    int32_t mask = (1 << N) - 1;
    int32_t A = 0;              // Accumulator initialized to 0
    int32_t Q_reg = Q & mask;   // Multiplier in Q register
    int32_t M_reg = M & mask;   // Multiplicand in M register
    int32_t Q_neg1 = 0;         // Extra bit Q_-1 initialized to 0
    int32_t SC = N;             // Sequence Counter = N

    std::cout << "\n=========================================================================\n";
    std::cout << " BOOTH'S MULTIPLICATION TRACE: M = " << M << ", Q = " << Q << " (" << N << "-bit)\n";
    std::cout << "=========================================================================\n";
    std::cout << std::left << std::setw(6)  << "Step" 
              << std::setw(N + 4) << "A" 
              << std::setw(N + 4) << "Q" 
              << std::setw(6)  << "Q_-1" 
              << std::setw(6)  << "SC" 
              << "Action Description\n";
    std::cout << "-------------------------------------------------------------------------\n";
    std::cout << std::left << std::setw(6)  << "Init" 
              << std::setw(N + 4) << to_binary<N>(A) 
              << std::setw(N + 4) << to_binary<N>(Q_reg) 
              << std::setw(6)  << Q_neg1 
              << std::setw(6)  << SC 
              << "Initial Register Setup\n";

    for (int step = 1; step <= static_cast<int>(N); ++step) {
        int q0 = Q_reg & 1;
        std::string action = "";

        // Decision logic on (Q0, Q_-1)
        if (q0 == 1 && Q_neg1 == 0) {
            // Q0 Q_-1 = 10 -> A = A - M
            A = (A - M) & mask;
            action = "Q0 Q_-1 = 10 -> A = A - M; ";
        } else if (q0 == 0 && Q_neg1 == 1) {
            // Q0 Q_-1 = 01 -> A = A + M
            A = (A + M) & mask;
            action = "Q0 Q_-1 = 01 -> A = A + M; ";
        } else {
            // Q0 Q_-1 = 00 or 11 -> No arithmetic
            action = "Q0 Q_-1 = " + std::to_string(q0) + std::to_string(Q_neg1) + " -> No Op; ";
        }

        // Arithmetic Shift Right (ASHR) of [A, Q, Q_-1]
        // Save LSB of Q as next Q_-1
        int new_Q_neg1 = Q_reg & 1;
        
        // Shift Q right; LSB of A moves to MSB of Q
        int lsb_A = A & 1;
        Q_reg = (Q_reg >> 1) | (lsb_A << (N - 1));
        
        // Arithmetic shift A right: replicate sign bit (bit N-1)
        int sign_A = (A >> (N - 1)) & 1;
        A = (A >> 1) | (sign_A << (N - 1));
        
        Q_neg1 = new_Q_neg1;
        --SC;
        action += "ASHR [A, Q, Q_-1]";

        std::cout << std::left << std::setw(6)  << step 
                  << std::setw(N + 4) << to_binary<N>(A) 
                  << std::setw(N + 4) << to_binary<N>(Q_reg) 
                  << std::setw(6)  << Q_neg1 
                  << std::setw(6)  << SC 
                  << action << "\n";
    }

    // Combine [A, Q] into 2N-bit signed result
    int64_t final_product = (static_cast<int64_t>(A) << N) | Q_reg;
    // Sign-extend if MSB of A is 1
    if ((A >> (N - 1)) & 1) {
        final_product |= ~((1ULL << (2 * N)) - 1);
    }

    std::cout << "-------------------------------------------------------------------------\n";
    std::cout << "Final Result in [A, Q]: " << to_binary<N>(A) << " " << to_binary<N>(Q_reg) 
              << " (" << to_binary<2 * N>(final_product) << "_2)\n";
    std::cout << "Decimal Algebraic Value: " << final_product << "\n";
    std::cout << "Expected Product:        " << static_cast<int64_t>(M) * Q << "\n";
    std::cout << "Verification:            " 
              << (final_product == static_cast<int64_t>(M) * Q ? "SUCCESS [PASS]" : "FAILURE [FAIL]") << "\n";
    std::cout << "=========================================================================\n";

    return final_product;
}

int main() {
    // Test 1: (+7) * (-5) in 5 bits
    booth_multiply<5>(7, -5);

    // Test 2: (-9) * (-4) in 5 bits
    booth_multiply<5>(-9, -4);

    return 0;
}
```

---

## 6.2 RESTORING & NON-RESTORING DIVISION SIMULATOR

```cpp
/**
 * @file division_algorithms.cpp
 * @brief Bit-Level Hardware Emulation of Restoring and Non-Restoring Division
 * @course Computer System Architecture (ITDC0209)
 */

#include <iostream>
#include <iomanip>
#include <bitset>
#include <cstdint>

template<size_t N>
std::string to_bin(uint32_t val) {
    std::bitset<N> b(val);
    return b.to_string();
}

/**
 * Restoring Division Algorithm for Unsigned Integers.
 * @param dividend Value to divide (X)
 * @param divisor  Divisor (Y)
 */
template<size_t N>
void restoring_divide(uint32_t dividend, uint32_t divisor) {
    uint32_t A = 0;              // Remainder register (N+1 bits for sign)
    uint32_t Q = dividend;       // Quotient / Dividend register (N bits)
    uint32_t B = divisor;        // Divisor register (N bits)
    uint32_t mask_A = (1 << (N + 1)) - 1;
    uint32_t mask_Q = (1 << N) - 1;
    int SC = N;

    std::cout << "\n=== RESTORING DIVISION: " << dividend << " / " << divisor << " ===\n";
    std::cout << "Init: A=" << to_bin<N + 1>(A) << ", Q=" << to_bin<N>(Q) << ", B=" << to_bin<N + 1>(B) << "\n";

    for (int step = 1; step <= static_cast<int>(N); ++step) {
        // 1. Shift Left [A, Q]
        uint32_t msb_Q = (Q >> (N - 1)) & 1;
        A = ((A << 1) | msb_Q) & mask_A;
        Q = (Q << 1) & mask_Q;

        // 2. Subtract Divisor: A = A - B
        A = (A - B) & mask_A;

        // 3. Check sign of A (bit N)
        bool is_negative = (A >> N) & 1;
        if (is_negative) {
            // Subtraction failed: Q0 = 0, Restore A = A + B
            Q &= ~1;
            A = (A + B) & mask_A;
            std::cout << "Step " << step << ": Subtract failed -> Restore A, Q0=0 | A=" 
                      << to_bin<N + 1>(A) << " Q=" << to_bin<N>(Q) << "\n";
        } else {
            // Subtraction succeeded: Q0 = 1, No restore
            Q |= 1;
            std::cout << "Step " << step << ": Subtract succeeded -> No restore, Q0=1 | A=" 
                      << to_bin<N + 1>(A) << " Q=" << to_bin<N>(Q) << "\n";
        }
        --SC;
    }

    std::cout << "Final Quotient  Q = " << Q << " (" << to_bin<N>(Q) << ")\n";
    std::cout << "Final Remainder A = " << A << " (" << to_bin<N>(A) << ")\n";
    std::cout << "Check: " << dividend << " = (" << divisor << " * " << Q << ") + " << A << "\n";
}

/**
 * Non-Restoring Division Algorithm for Unsigned Integers.
 */
template<size_t N>
void non_restoring_divide(uint32_t dividend, uint32_t divisor) {
    uint32_t A = 0;              // Remainder register (N+1 bits)
    uint32_t Q = dividend;       // Quotient / Dividend register
    uint32_t B = divisor;        // Divisor register
    uint32_t mask_A = (1 << (N + 1)) - 1;
    uint32_t mask_Q = (1 << N) - 1;
    int SC = N;

    std::cout << "\n=== NON-RESTORING DIVISION: " << dividend << " / " << divisor << " ===\n";
    std::cout << "Init: A=" << to_bin<N + 1>(A) << ", Q=" << to_bin<N>(Q) << "\n";

    for (int step = 1; step <= static_cast<int>(N); ++step) {
        bool A_neg = (A >> N) & 1;

        // 1. Shift Left [A, Q]
        uint32_t msb_Q = (Q >> (N - 1)) & 1;
        A = ((A << 1) | msb_Q) & mask_A;
        Q = (Q << 1) & mask_Q;

        // 2. Add or Subtract based on sign of A
        if (A_neg) {
            A = (A + B) & mask_A;
            std::cout << "Step " << step << ": A was negative -> Shift Left, Add B; ";
        } else {
            A = (A - B) & mask_A;
            std::cout << "Step " << step << ": A was positive -> Shift Left, Sub B; ";
        }

        // 3. Set Q0 based on resulting sign of A
        bool new_A_neg = (A >> N) & 1;
        if (new_A_neg) {
            Q &= ~1;  // Q0 = 0
            std::cout << "Result A < 0 -> Q0=0 | A=" << to_bin<N + 1>(A) << " Q=" << to_bin<N>(Q) << "\n";
        } else {
            Q |= 1;   // Q0 = 1
            std::cout << "Result A >= 0 -> Q0=1 | A=" << to_bin<N + 1>(A) << " Q=" << to_bin<N>(Q) << "\n";
        }
        --SC;
    }

    // Post-Correction Step: If final A < 0, restore once by A = A + B
    if ((A >> N) & 1) {
        A = (A + B) & mask_A;
        std::cout << "Post-Correction: Final A was negative -> A = A + B = " << to_bin<N + 1>(A) << "\n";
    }

    std::cout << "Final Quotient  Q = " << Q << " (" << to_bin<N>(Q) << ")\n";
    std::cout << "Final Remainder A = " << A << " (" << to_bin<N>(A) << ")\n";
}

int main() {
    restoring_divide<4>(11, 3);
    non_restoring_divide<4>(11, 3);
    return 0;
}
```

---

## 6.3 IEEE 754 FLOATING-POINT PACKER, UNPACKER, & INSPECTOR

```cpp
/**
 * @file ieee754_inspector.cpp
 * @brief Bit-Level Bitfield Disassembler for IEEE 754 Floating-Point Numbers
 * @course Computer System Architecture (ITDC0209)
 */

#include <iostream>
#include <iomanip>
#include <bitset>
#include <cstring>
#include <cmath>

void inspect_ieee754_single(float val) {
    uint32_t raw_bits;
    std::memcpy(&raw_bits, &val, sizeof(float));

    uint32_t sign = (raw_bits >> 31) & 1;
    uint32_t exp  = (raw_bits >> 23) & 0xFF;
    uint32_t frac = raw_bits & 0x7FFFFF;

    std::cout << "\n======================================================\n";
    std::cout << " IEEE 754 SINGLE PRECISION INSPECTION: " << val << "\n";
    std::cout << "======================================================\n";
    std::cout << "Hex Representation: 0x" << std::hex << std::uppercase 
              << std::setfill('0') << std::setw(8) << raw_bits << std::dec << "\n";
    std::cout << "Binary Bits:        " << std::bitset<1>(sign) << " "
              << std::bitset<8>(exp) << " "
              << std::bitset<23>(frac) << "\n";
    std::cout << "Sign Bit (S):       " << sign << " (" << (sign ? "Negative [-]" : "Positive [+]") << ")\n";
    std::cout << "Biased Exp (E):     " << exp << " (Binary: " << std::bitset<8>(exp) << ")\n";
    std::cout << "Fraction (F):       0x" << std::hex << frac << std::dec 
              << " (" << std::bitset<23>(frac) << ")\n";

    // Value classification
    if (exp == 255) {
        if (frac == 0) {
            std::cout << "Classification:     INFINITY (" << (sign ? "-Infinity" : "+Infinity") << ")\n";
        } else {
            bool qnan = (frac >> 22) & 1;
            std::cout << "Classification:     NaN (" << (qnan ? "Quiet NaN" : "Signaling NaN") << ")\n";
        }
    } else if (exp == 0) {
        if (frac == 0) {
            std::cout << "Classification:     ZERO (" << (sign ? "-0.0" : "+0.0") << ")\n";
        } else {
            std::cout << "Classification:     SUBNORMAL (Denormalized) NUMBER\n";
            int true_exp = 1 - 127; // -126
            double significand = static_cast<double>(frac) / (1 << 23);
            std::cout << "True Exponent:      " << true_exp << "\n";
            std::cout << "Significand:        0." << significand << "\n";
        }
    } else {
        int true_exp = static_cast<int>(exp) - 127;
        double significand = 1.0 + (static_cast<double>(frac) / (1 << 23));
        std::cout << "Classification:     NORMALIZED FINITE NUMBER\n";
        std::cout << "True Exponent (e):  " << true_exp << " (Stored " << exp << " - Bias 127)\n";
        std::cout << "Significand (1.F):  " << std::setprecision(8) << significand << "\n";
        std::cout << "Mathematical Form:  (-1)^" << sign << " * " << significand << " * 2^(" << true_exp << ")\n";
    }
    std::cout << "======================================================\n";
}

int main() {
    inspect_ieee754_single(-13.75f);
    inspect_ieee754_single(0.125f);
    inspect_ieee754_single(5.0f);
    inspect_ieee754_single(0.0f);
    inspect_ieee754_single(std::numeric_limits<float>::infinity());
    return 0;
}
```

---

## 6.4 CACHE MEMORY MAPPING & AMAT SIMULATOR

```cpp
/**
 * @file cache_simulator.cpp
 * @brief Cache Address Bit-Splitter and AMAT Performance Calculator
 * @course Computer System Architecture (ITDC0209)
 */

#include <iostream>
#include <iomanip>
#include <cmath>

struct CacheConfig {
    uint32_t address_bits;
    uint32_t cache_size_bytes;
    uint32_t block_size_bytes;
    uint32_t associativity; // 1 = Direct, N = N-way, 0 = Fully Associative
};

void analyze_cache(const CacheConfig& cfg) {
    uint32_t offset_bits = static_cast<uint32_t>(std::log2(cfg.block_size_bytes));
    uint32_t total_lines = cfg.cache_size_bytes / cfg.block_size_bytes;

    std::cout << "\n=======================================================\n";
    std::cout << " CACHE CONFIGURATION ANALYSIS\n";
    std::cout << "=======================================================\n";
    std::cout << "Address Space:    " << cfg.address_bits << " bits (" 
              << (1ULL << cfg.address_bits) / (1024 * 1024 * 1024) << " GiB)\n";
    std::cout << "Cache Capacity:   " << cfg.cache_size_bytes / 1024 << " KiB\n";
    std::cout << "Block (Line) Size:" << cfg.block_size_bytes << " Bytes\n";
    std::cout << "Total Cache Lines:" << total_lines << "\n";

    if (cfg.associativity == 1) {
        // Direct Mapped
        uint32_t index_bits = static_cast<uint32_t>(std::log2(total_lines));
        uint32_t tag_bits = cfg.address_bits - index_bits - offset_bits;
        std::cout << "Architecture:     DIRECT MAPPED\n";
        std::cout << "Line Index Bits:  " << index_bits << "\n";
        std::cout << "Tag Bits:         " << tag_bits << "\n";
        std::cout << "Offset Bits:      " << offset_bits << "\n";
        std::cout << "Address Layout:   [ Tag: " << tag_bits << " | Line: " 
                  << index_bits << " | Offset: " << offset_bits << " ]\n";
    } else if (cfg.associativity == 0 || cfg.associativity == total_lines) {
        // Fully Associative
        uint32_t tag_bits = cfg.address_bits - offset_bits;
        std::cout << "Architecture:     FULLY ASSOCIATIVE\n";
        std::cout << "Tag Bits:         " << tag_bits << "\n";
        std::cout << "Offset Bits:      " << offset_bits << "\n";
        std::cout << "Address Layout:   [ Tag: " << tag_bits << " | Offset: " << offset_bits << " ]\n";
    } else {
        // N-Way Set-Associative
        uint32_t num_sets = total_lines / cfg.associativity;
        uint32_t set_bits = static_cast<uint32_t>(std::log2(num_sets));
        uint32_t tag_bits = cfg.address_bits - set_bits - offset_bits;
        std::cout << "Architecture:     " << cfg.associativity << "-WAY SET-ASSOCIATIVE\n";
        std::cout << "Total Sets:       " << num_sets << "\n";
        std::cout << "Set Index Bits:   " << set_bits << "\n";
        std::cout << "Tag Bits:         " << tag_bits << "\n";
        std::cout << "Offset Bits:      " << offset_bits << "\n";
        std::cout << "Address Layout:   [ Tag: " << tag_bits << " | Set: " 
                  << set_bits << " | Offset: " << offset_bits << " ]\n";
    }
    std::cout << "=======================================================\n";
}

double compute_amat(double hit_time, double miss_rate, double miss_penalty) {
    return hit_time + (miss_rate * miss_penalty);
}

int main() {
    // 32-bit address, 64 KB cache, 32 B blocks
    CacheConfig direct_cfg = {32, 64 * 1024, 32, 1};
    analyze_cache(direct_cfg);

    CacheConfig set_assoc_cfg = {32, 64 * 1024, 32, 4};
    analyze_cache(set_assoc_cfg);

    CacheConfig fully_assoc_cfg = {32, 64 * 1024, 32, 0};
    analyze_cache(fully_assoc_cfg);

    std::cout << "\nAMAT Demonstration:\n";
    double L1_hit = 1.0; // 1 ns
    double L1_miss_rate = 0.05; // 5%
    double L2_hit = 4.0; // 4 ns
    double L2_miss_rate = 0.20; // 20%
    double DRAM_penalty = 60.0; // 60 ns

    double L2_penalty = compute_amat(L2_hit, L2_miss_rate, DRAM_penalty);
    double amat = compute_amat(L1_hit, L1_miss_rate, L2_penalty);
    std::cout << "Two-Level Cache AMAT = " << amat << " ns\n";

    return 0;
}
```

---

# SECTION 7: MASTER COMPARATIVE ARCHITECTURAL TABLES & FORMULA CHEAT SHEET

---

## 7.1 COMPREHENSIVE CSA FORMULA CHEAT SHEET

### 1. Data Representation & Fixed-Point
- **Positional Value**: $N = \sum_{i=-m}^{n-1} d_i \cdot r^i$
- **1's Complement**: $K_1 = (2^n - 1) - N$
- **2's Complement**: $K_2 = 2^n - N = \text{1's Comp} + 1$
- **Range of $n$-bit 2's Complement**: $[-2^{n-1}, +2^{n-1} - 1]$
- **Signed Arithmetic Overflow Flag**: $V = C_{in} \oplus C_{out}$ (for sign bit)

### 2. Floating-Point & IEEE 754 Standard
- **Exponent Bias**: $\text{Bias} = 2^{k-1} - 1$ ($k=8 \implies 127$; $k=11 \implies 1023$)
- **Single Precision Value**: $(-1)^S \times (1.F) \times 2^{E - 127}$
- **Subnormal Single Precision Value**: $(-1)^S \times (0.F) \times 2^{-126}$
- **Floating-Point Mult Biased Exponent**: $E_{\text{result}} = E_A + E_B - \text{Bias}$
- **Floating-Point Div Biased Exponent**: $E_{\text{result}} = E_A - E_B + \text{Bias}$

### 3. Error Detection (Hamming Code)
- **Parity Inequality**: $2^r \ge m + r + 1$
- **Syndrome Vector**: $S = C_k \dots C_2 C_1$ (If $S=0$, no error; if $S \neq 0$, $S$ equals erroneous bit position).

### 4. Digital Adders & ALU Timing
- **Ripple Carry Adder Delay**: $T_{\text{RCA}} = 2n \Delta$
- **Carry Generate**: $G_i = A_i \cdot B_i$
- **Carry Propagate**: $P_i = A_i \oplus B_i$
- **Carry Look-Ahead Adder Delay**: $T_{\text{CLA}} = 4 \Delta$ (Constant within block).

### 5. Memory System & Caches
- **2.5D Coincident Decoding Lines**: $2 \times 2^{k/2}$ lines (vs $2^k$ for 2D).
- **DRAM Refresh Interval**: $\text{Interval} = \frac{t_{\text{ref}}}{\text{Number of Rows}}$.
- **Refresh Overhead**: $\text{Overhead} = \frac{\text{Rows} \times t_{\text{cycle}}}{t_{\text{ref}}} \times 100\%$.
- **AMAT (Single Level)**: $\text{AMAT} = T_{hit} + (1 - H) \times T_{miss}$.
- **AMAT (Two-Level)**: $\text{AMAT} = T_{L1} + M_{L1} \times [T_{L2} + M_{L2} \times T_{mem}]$.
- **Cache Offset Bits**: $w = \log_2(\text{Block Size in Bytes})$.
- **Direct Mapped Line Index**: $s = \log_2(\text{Total Cache Lines } L)$.
- **Set-Associative Sets**: $S = L / k \implies d = \log_2(S)$ bits.
- **Tag Bits**: $t = \text{Address Width} - \text{Index Bits} - \text{Offset Bits}$.

### 6. Auxiliary Storage (Disks)
- **Rotational Latency**: $T_{\text{rot}} = \frac{1}{2} \times \frac{60}{\text{RPM}}$ seconds.
- **Transfer Time**: $T_{\text{transfer}} = \frac{\text{Data Bytes}}{\text{Transfer Rate (Bytes/sec)}}$.
- **Total Disk Access Time**: $T_{\text{access}} = T_{\text{seek}} + T_{\text{rot}} + T_{\text{transfer}} + T_{\text{controller}}$.

### 7. Virtual Memory & Paging
- **Virtual Address**: $[\text{VPN} \mid \text{Offset}]$.
- **Physical Address**: $[\text{PFN} \mid \text{Offset}]$.
- **Effective Memory Access Time (EMAT)**:
  $$\text{EMAT} = T_{\text{TLB}} + H_{\text{TLB}} \times T_{mem} + (1 - H_{\text{TLB}}) \times (2 \times T_{mem})$$

### 8. Serial Communication
- **Bit Rate vs Baud Rate**: $\text{Bit Rate} = \text{Baud Rate} \times \log_2(M)$.
- **Asynchronous Framing Overhead**: $\text{Overhead} = \frac{\text{Start} + \text{Parity} + \text{Stop Bits}}{\text{Total Frame Bits}} \times 100\%$.

---

## 7.2 MASTER ARCHITECTURAL COMPARISON MATRIX

| Feature / System | Alternative A | Alternative B | Winner / Trade-Off Insight |
| :--- | :--- | :--- | :--- |
| **Control Unit** | **Hardwired Control** (Fixed gate logic) | **Microprogrammed Control** (Control ROM microcode) | Hardwired wins on **Speed** (RISC); Microprogrammed wins on **Flexibility & Upgradability** (CISC). |
| **Microcode Format** | **Horizontal** (1 bit per line, unencoded) | **Vertical** (Encoded fields, decoders) | Horizontal wins on **Concurrency & Speed**; Vertical wins on **Memory Compactness**. |
| **RAM Cell** | **6T SRAM** (Cross-coupled inverters) | **1T-1C DRAM** (Capacitor charge) | SRAM wins on **Speed (0.5ns)**; DRAM wins on **Density & Low Cost**. |
| **Internal Memory** | **2D Organization** (Single giant decoder) | **2.5D Coincident** (Row + Column decoders) | 2.5D wins overwhelmingly by **reducing pin/wire routing from $2^k$ to $2 \times 2^{k/2}$**. |
| **Cache Write** | **Write-Through** (Writes cache + RAM) | **Write-Back** (Writes cache only, dirty bit) | Write-through wins on **Simplicity & Consistency**; Write-back wins on **Low Bus Traffic**. |
| **Cache Mapping** | **Direct Mapping** (1 line per block) | **Set-Associative** ($k$ lines per set) | Direct wins on **Hit Latency**; Set-Associative wins on **Zero Conflict Thrashing**. |
| **Virtual Memory** | **Paging** (Fixed-size frames) | **Segmentation** (Variable logical blocks) | Paging has **Zero External Fragmentation**; Segmentation has **Natural Code Protection & Sharing**. |
| **I/O Addressing** | **Isolated I/O** (Separate address space, IN/OUT) | **Memory-Mapped I/O** (Unified space, LOAD/STORE) | Isolated preserves **Full RAM space**; Memory-mapped provides **Rich Addressing Modes**. |
| **Data Transfer** | **Programmed I/O** (Polling loop) | **Direct Memory Access** (DMAC block transfer) | DMA wins by **freeing the CPU completely from high-volume block data transfers**. |
| **Bus Arbitration** | **Daisy Chaining** (Serial priority line) | **Independent Request** (Dedicated BR/BG per master) | Daisy chain has **Minimal Wires (3)**; Independent Request has **$O(1)$ Maximum Speed & Starvation Prevention**. |

---
