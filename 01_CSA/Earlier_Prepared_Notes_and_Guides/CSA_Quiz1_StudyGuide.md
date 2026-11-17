# Computer System Architecture (ITPC-209) — Quiz 1 Complete Prep
Covers: Number Representation (fixed/floating point), IEEE 754, Signed Addition/Subtraction, Computer Generations & Classification, Functional Units, Buses & Bus Architecture, Register/Bus/Memory Transfer — plus every extra concept your two PYQ sets actually test (Booth's, Hamming code, adders, addressing modes, instruction cycle).

**PYQ sets referenced:**
- **Set A** = Quiz dated Sept 4, 2025 (your two-page paper, Q1–Q15)
- **Set B** = the other practice paper (Q1–Q20)

---

## 1. Number Representation — Fixed Point

**Decimal → Binary:** split integer and fractional parts.
- Integer part: repeated division by 2, read remainders bottom-to-top.
- Fractional part: repeated multiplication by 2, read carries top-to-bottom, stop when fraction = 0 or you have enough bits.

**Binary ↔ Hex/Octal:** group bits in 4s (hex) or 3s (octal) from the binary point outward, padding with zeros.

### Solved PYQ
**[Set A, Q1]** Binary equivalent of 55.875:
- 55 → 110111
- 0.875×2=1.75→**1**; 0.75×2=1.5→**1**; 0.5×2=1.0→**1** → .111
- **Answer: 110111.111**

### Practice — 5 more
1. Convert (110.6875)₁₀ to binary.
2. Convert (172.25)₁₀ to binary, then to hexadecimal.
3. Convert (0.1101101)₂ to decimal.
4. Convert (2A.C)₁₆ to binary and to decimal.
5. Convert (367.4)₈ to binary and decimal.

---

## 2. Signed Numbers & Signed Addition/Subtraction

| Scheme | Negative –N (n bits) represented as |
|---|---|
| Signed magnitude | MSB=1 (sign) + magnitude bits |
| 1's complement | Invert all bits of +N |
| 2's complement | Invert all bits of +N, then add 1 |

- **Only 2's complement is used in real computer hardware** — it gives a single representation of 0 (no +0/−0 problem) and lets addition/subtraction use the same adder circuit.
- Range for n-bit 2's complement: **−2ⁿ⁻¹ to +2ⁿ⁻¹−1**.
- **Subtraction A − B** = A + (2's complement of B).

**Overflow rule (the one examiners love):**
- Overflow can happen **only when adding two numbers of the same sign**.
- (+) + (+) → overflow if result's sign bit = 1
- (−) + (−) → overflow if result's sign bit = 0
- (+) + (−) → **overflow is impossible** (this is exactly Set B Q6)
- Formal rule: **Overflow = Carry into sign bit XOR Carry out of sign bit**

### Solved PYQ
**[Set A, Q4]** (+50) + (+100), 8-bit two's complement:
```
  00110010   (+50)
+ 01100100   (+100)
-----------
  10010110
```
- Result bit pattern = 10010110. Carry **out** of MSB = 0, Carry **into** MSB = 1.
- **Overflow = 1 (YES)** — two positives produced a bit pattern that reads as negative (150 > 127, the 8-bit signed max), classic overflow.
- **Carry (Cout) = 0** — note this is the trap: students assume overflow needs a carry-out. It doesn't. Overflow ≠ Carry.

**[Set B, Q6]** "Overflow (B) cannot occur when a positive value is added to a negative value" → **TRUE, this is the correct statement.**

### Practice — 5 more
1. Add (+70) and (+90) in 8-bit 2's complement. State carry and overflow.
2. Add (−60) and (−90) in 8-bit 2's complement. State carry and overflow.
3. Compute (45) − (78) using 8-bit 2's complement addition.
4. Represent −38 in 8-bit signed magnitude, 1's complement, and 2's complement.
5. Add (+30) and (−20) in 8-bit 2's complement (this exact example is in your class notes — verify you get +10 = 00001010).

---

## 3. Floating-Point Representation & IEEE 754

**General form:** N = (−1)ˢ × (1.M) × 2^(E − bias) — normalized so there's exactly one non-zero digit before the binary point (implicit leading 1, not stored).

| Format | Sign | Exponent | Mantissa | Bias |
|---|---|---|---|---|
| Single precision | 1 | 8 | 23 | 127 |
| Double precision | 1 | 11 | 52 | 1023 |

**Bias formula:** bias = 2^(k−1) − 1, where k = number of exponent bits.
(Check: k=8 → 127 ✓. k=10 → 511, matches Set A Q10 below.)

**Conversion steps (exactly how your notes do it):**
1. Convert decimal to binary (integer + fraction).
2. Normalize: 1.xxxx × 2^e.
3. Stored exponent = actual exponent + bias.
4. Mantissa = the bits after the binary point in normalized form (pad with 0s to fill the field).

### Solved PYQs
**[Set A, Q2]** Represent 0.125 in IEEE 754 single precision:
- 0.125 = 2⁻³ = 1.0 × 2⁻³
- Sign = 0; Exponent = −3+127 = 124 = `01111100`; Mantissa = 23 zeros
- **Answer: 0 01111100 00000000000000000000000** → hex `0x3E000000`

**[Set A, Q10]** Format (1, 10, 12) — sign, exponent, mantissa. Bias = 2^(10−1)−1 = 2⁹−1 = **511** → **(c)**

**[Set B, Q1]** Max value the (8-bit) exponent field can hold = all 1s = **255, i.e. 11111111 → (C)**

**[Set B, Q5]** Represent +46.5 as a 24-bit float (8-bit exponent, 16-bit mantissa):
- 46.5 = 101110.1 → normalized: 1.011101 × 2⁵
- Exponent (excess-127) = 5+127 = 132 = `10000100`
- Mantissa (sign bit + 15 fraction bits) = `0` `011101000000000`
- **Final: 10000100 0011101000000000**
- *(Note: this format packs the sign as the mantissa's MSB since only 8+16=24 bits are given — flag this assumption to your prof if their notation differs.)*

**[Set B, Q2]** "Default exponent field value for a normalized number" → tests that **bias = 127 for single precision** is the reference/default offset → **(C)**

### Practice — 5 more
1. Represent −13.75 in IEEE 754 single precision (binary + hex).
2. Represent 1.0 in IEEE 754 single precision. What's special about its exponent field?
3. What decimal value does `0 10000001 01000000000000000000000` represent?
4. For format (1, 11, 20), what is the bias?
5. Represent +100.0 as a 24-bit float (1 sign + 8 exponent(excess-127) + 15 mantissa).

---

## 4. Booth's Algorithm & Restoring Division

**Booth's algorithm (signed multiplication):** look at (Qₒ, Q₋₁), the current LSB of Q and the bit just shifted out:

| Qₒ Q₋₁ | Action |
|---|---|
| 00 | No arithmetic op, just arithmetic shift right |
| 01 | Add Multiplicand to partial product (AC), then shift |
| 10 | Subtract Multiplicand from partial product (AC), then shift |
| 11 | No arithmetic op, just arithmetic shift right |

**Restoring division:**
1. Shift dividend/remainder left; subtract divisor.
2. If result (Dividend − Divisor) is **negative** → quotient bit = **0**, and **restore** by adding the divisor back.
3. If result is **positive/zero** → quotient bit = **1**, keep the result, no restore needed.

### Solved PYQ
**[Set A, Q9–Q10]** When Qₒ,Q₋₁ = 10 → **Subtract multiplicand from partial product** (option b).
**[Set A, Q8]** If (Dividend − Divisor) is negative → **(b) Quotient bit = 0, remainder restored by adding divisor back.**

### Practice — 5 more
1. In Booth's algorithm, what operation happens when Qₒ,Q₋₁ = 01?
2. Multiply (+7) × (−3) using Booth's algorithm (show the Qₒ,Q₋₁ sequence) — use 4-bit operands.
3. In restoring division, what happens if the very first subtraction gives a positive result?
4. What's the key hardware difference between restoring and non-restoring division?
5. Multiply (5)₁₀ × (−4)₁₀ using Booth's algorithm with 4-bit representation and trace all 4 steps.

---

## 5. Error Detection — Hamming Code

**Why:** detects *and* corrects single-bit errors using extra parity bits placed at power-of-2 positions (1, 2, 4, 8, …).

**Number of parity bits r needed for m data bits:** smallest r satisfying **2^r ≥ m + r + 1**.

| Data bits (m) | Parity bits (r) | Total bits (n) |
|---|---|---|
| 4 | 3 | 7 |
| 7 | 4 | 11 |
| 8 | 4 | 12 |

**Finding the error (syndrome method):**
- Parity bit at position 2^i checks all positions whose binary form has bit *i* set.
- Compute Cᵢ = XOR of all bits in its group (received value).
- Syndrome = C₈C₄C₂C₁ (binary) → **that number IS the faulty bit position.** If syndrome = 0, no error.

### Solved PYQ
**[Set A, Q3]** 7-bit data → **r = 4** parity bits **[Set B, Q11 confirms this: (c) 4]**, since 2³=8 < 7+3+1=11, but 2⁴=16 ≥ 7+4+1=12. ✓

For the 12-bit received word **100110101110**, walking the syndrome method:
- C1 (positions 1,3,5,7,9,11) → odd parity → 1
- C2 (positions 2,3,6,7,10,11) → odd parity → 1
- C4 (positions 4,5,6,7,12) → odd parity → 1
- C8 (positions 8,9,10,11,12) → odd parity → 1
- Syndrome = 1111₂ = **15**

Since a 12-bit code only has positions 1–12, syndrome 15 falling outside that range is the teaching point itself: it signals **more than one bit is in error**, which single-error-correcting Hamming code cannot pinpoint/fix (it can only guarantee correction of exactly *one* flipped bit). If your professor expects a clean 1–12 answer instead, double-check the exact bit string against your paper — worth confirming before the quiz.

### Practice — 5 more
1. How many parity bits are needed for 11 data bits?
2. For an 8-bit data word, how many parity bits and what's the total codeword length?
3. A 7-bit Hamming code (4 data + 3 parity) is received as 1011001. Find the syndrome and correct it if needed.
4. Which bit positions in a Hamming code are reserved for parity, and why powers of 2?
5. What's the difference between what a single parity bit can do vs. what Hamming code can do?

---

## 6. Digital Computer Generations

| Gen | Years | Primary technology | Example |
|---|---|---|---|
| 1st | 1940s–50s | Vacuum tubes | ENIAC, UNIVAC-I |
| 2nd | 1950s–60s | **Transistors** | **IBM 1401** |
| 3rd | 1960s–70s | Integrated Circuits (ICs) | IBM 360 |
| 4th | 1970s–present | Microprocessors (VLSI) | Apple Macintosh |
| 5th | present onward | AI, ULSI, parallel processing | — |

### Solved PYQs
**[Set A, Q7]** Second-generation computer → **(c) IBM 1401** (transistor-based, 1959).
**[Set B, Q3]** Characteristic of second generation → **(B) used transistors as the primary electronic component.**

### Practice — 5 more
1. Which generation introduced integrated circuits, and what was the major benefit?
2. ENIAC belongs to which generation and why?
3. What distinguishes 4th-generation computers from 3rd-generation ones?
4. Name one defining feature each of Von Neumann and Harvard architecture (both appear in your notes — see Section 8).
5. Which generation is associated with AI and parallel processing?

---

## 7. Computer Types & Classification

| Type | Defining trait |
|---|---|
| Supercomputer | Extreme speed/processing power for scientific computation |
| Mainframe | High reliability, handles large-scale transaction processing (banks, airlines) |
| Minicomputer | Mid-range, multi-user, smaller than mainframe |
| Microcomputer | Single microprocessor-based, designed for personal/individual use |

### Solved PYQs
**[Set A, Q13]** Supercomputer classified based on → **(a) Speed and processing power.**
**[Set B, Q4]** Computer designed for personal use → **(C) Microcomputer.**

### Practice — 5 more
1. What's the key difference between a mainframe and a supercomputer?
2. Give one real-world use case each for mainframe vs. minicomputer.
3. On what basis are computers typically classified (list 2–3 bases beyond speed)?
4. Is a modern smartphone a microcomputer? Justify.
5. Why can't raw clock speed alone classify a computer as a "supercomputer"?

---

## 8. Functional Units, CPU Registers & Instruction Cycle

**Basic functional units:** Input, Output, Memory (Main + Secondary), ALU, Control Unit, Registers — ALU+CU+Registers together = CPU.

**Von Neumann architecture (1945):** single memory stores both instructions and data (stored-program concept).
**Harvard architecture (1939):** instruction memory and data memory are physically separate.

**Key CPU registers:**

| Register | Purpose |
|---|---|
| PC (Program Counter) | Address of the **next** instruction to execute |
| MAR (Memory Address Register) | Holds the memory address currently being accessed |
| MDR/AC (Accumulator) | Holds data being transferred / intermediate ALU results |
| IR (Instruction Register) | Holds the instruction currently being executed |
| SP (Stack Pointer) | Points to top of stack |

**Instruction cycle:** Fetch → Decode → Execute (→ Store/write-back, in the expanded 4-step version).
**Two broad phases:** Instruction Fetch and Instruction Execution.

### Solved PYQs
**[Set A, Q12]** MAR ← PC → **(b) Register to register transfer.**
**[Set A, Q5]** CPU generates a memory address to fetch data: **Address bus** carries the address CPU→memory, **Control bus** carries the Read signal, **Data bus** carries the retrieved data memory→register.
**[Set A, Q14]** Register tracking the address of the next instruction → **(b) Program counter.**
**[Set B, Q11]** CPU consists of → **(D) ALU, Control Unit, Registers and Internal buses.**
**[Set B, Q12]** Unit performing arithmetic ops & comparisons → **(a) ALU.**
**[Set B, Q13]** ALU stores intermediate results in → **(d) Accumulator.**
**[Set B, Q16]** Register holding instruction currently executing → **(c) Instruction register.**
**[Set B, Q17]** Instruction cycle consists of → **(d) fetching, decoding, executing, and storing.**
**[Set B, Q18]** Two phases of executing an instruction → **(b) Instruction fetch and instruction execution.**

### Practice — 5 more
1. What's the difference between MAR and MDR?
2. Trace the register-transfer sequence for a basic instruction fetch (PC, MAR, MDR, IR).
3. Why does Harvard architecture allow faster instruction throughput than Von Neumann?
4. What does the Stack Pointer do during a function call?
5. Name the CPU register that combines with the CU to make all decisions about instruction sequencing.

---

## 9. Buses, Bus Architecture & Bus Arbitration

**System bus = three logical buses:**

| Bus | Direction | Carries |
|---|---|---|
| Address bus | Unidirectional (CPU→Mem/IO) | Memory/IO location to access |
| Data bus | Bidirectional | Actual data being transferred |
| Control bus | Bidirectional | Read/Write, clock, interrupt, ready signals |

**Bus arbitration** (deciding which device gets bus control when several want it — needed because only one device can drive the bus at a time):

| Scheme | How it works |
|---|---|
| Daisy chaining | Devices in a priority chain; Bus Grant passes device-to-device until it reaches the requester |
| Polling (rotating priority) | Controller polls each device in sequence to check who wants the bus |
| Independent request | Each device has its own request/grant lines to the controller — fastest, most hardware |

**DMA-specific transfer modes** (also in your class notes, related but a separate concept from arbitration schemes above):
- **Burst/Block mode:** transfers an entire block in one go, CPU is locked out until done.
- **Cycle stealing:** DMA "steals" one bus cycle at a time between CPU cycles.
- **Transparent mode:** DMA only uses cycles the CPU isn't using — zero CPU delay, slowest transfer.

### Solved PYQ
**[Set A, Q5]** (same as Section 8) — Address bus + Control bus + Data bus, each for a distinct purpose in the fetch operation.

### Practice — 5 more
1. Why is the address bus unidirectional but the data bus bidirectional?
2. Name and briefly explain the three classic bus arbitration techniques.
3. What problem does bus arbitration solve in a multi-device system?
4. Differentiate cycle stealing from burst mode DMA transfer.
5. What signals are exchanged between a device and the bus controller during daisy-chain arbitration (hint: BR/BG)?

---

## 10. Register, Bus & Memory Transfer

**Notation:**
- `R2 ← R1` — register transfer (contents of R1 copied into R2)
- `R3 ← R1 + R2` — arithmetic microoperation via bus/ALU
- `M[MAR] ← MDR` — memory write
- `MDR ← M[MAR]` — memory read

**Memory transfer basics:**
- **Read operation:** Memory content → CPU (non-destructive, memory content unchanged).
- **Write operation:** Processor data → Memory (destroys/overwrites the old content at that location).

A common bus system connects multiple registers through **one shared set of lines** with multiplexers selecting the source, rather than wiring every register to every other register directly — saves massive amounts of wiring as register count grows.

### Practice — 5 more
1. Write the register-transfer notation for "load AC with the contents of memory at the address in MAR."
2. What's the difference between a memory Read and a memory Write operation in terms of data flow?
3. Why is a common bus preferred over direct point-to-point wiring between all registers?
4. Write the microoperation notation for R1 ← R1 − R2.
5. In `MAR ← PC`, which register supplies data and which receives it?

---

## 11. Adders (Combinational Arithmetic Circuits)

| Adder | Inputs | Handles carry-in? | Speed issue |
|---|---|---|---|
| Half adder | A, B | No | — |
| Full adder | A, B, Cin | Yes | — |
| Ripple carry adder (chain of full adders) | n-bit A, B | Yes | **Carry propagation delay** — each stage waits for the previous stage's carry |
| Carry Look-Ahead adder (CLA) | n-bit A, B | Yes | Computes all carries in advance using extra logic → much faster |

### Solved PYQ
**[Set A, Q6]** Which adder suffers from carry propagation delay? → **(c) Ripple Carry Adder.**

### Practice — 5 more
1. Why does a Carry Look-Ahead adder avoid the ripple delay?
2. Write the Sum and Carry Boolean expressions for a Half Adder.
3. Write the Sum and Carry Boolean expressions for a Full Adder.
4. How many full adders are needed to build an 8-bit ripple carry adder?
5. What's the practical trade-off (cost vs. speed) between ripple carry and CLA adders?

---

## 12. Quick-Hit Extras (high-frequency 1-liners from your PYQs)

| Topic | Fact |
|---|---|
| Bytes | 2¹⁰=KB, 2²⁰=MB, 2³⁰=GB, 2⁴⁰=TB, **2⁵⁰=Petabyte** [Set B Q8 → (B)] |
| Memory vs non-memory | Instruction cache, Instruction register, TLB = all memory; **Instruction opcode is NOT memory**, it's just a field of an instruction [Set B Q7 → (C)] |
| Logic vs arithmetic ops | AND/OR/NOT = logic; ADD/MUL/DIV = arithmetic; LOAD/STORE = data transfer; PUSH/POP = stack ops [Set A Q14 → (a) AND, OR, NOT] |
| Floating point addition | First step = **Compare exponents** (then equalize, add mantissas, normalize) [Set A Q15 → (c)] |
| Addressing modes → use case | Indirect addressing → Pointers; Immediate addressing → Constants; Auto-decrement addressing → Loops [Set B Q9] |
| Opcode-bits calc | 16 GPRs (4 bits/reg), 8 addressing modes (3 bits), 2 register fields (8 bits) + 3 bits mode + 16-bit scalar = 27 bits used of 32 → **opcode = 5 bits → 32 unique opcodes** [Set B Q10 → (B) 32] |
| Big-endian | Sign bit lives in the **higher-order byte of the word** — true regardless of endianness, since endianness only affects memory address mapping, not which byte is "most significant" [Set B Q19 → (a)] |
| Arithmetic shift right | MSB (sign) is preserved/copied in, all bits shift right, LSB dropped. Example: 10011100 (=−100) → **11001110 (=−50)**, i.e. signed divide-by-2 [Set B Q20] |
| Buffer register | Used to overcome speed mismatch between devices [Set B Q15 → (c)] |

### Practice — 5 more (mixed)
1. What's 2⁴⁰ bytes called?
2. Is a Translation Look-aside Buffer a form of memory? Why?
3. Classify these as logic/arithmetic/data-transfer/stack ops: XOR, SUB, MOV, PUSH.
4. A processor supports 4 addressing modes and 8 registers with a 16-bit instruction and two register operand fields — how many bits remain for the opcode?
5. An 8-bit register holds 01101100. What's the value after an arithmetic shift right?

---

## Answer Key — New Practice Questions

**§1 Number Representation:** (1) 1101110.1011 (2) 10101100.01 → AC.4₁₆ (3) 0.8515625 (4) 00101010.1100 = 42.75 (5) 11110111.100 = 247.5

**§2 Signed Add/Sub:** (1) 01000000+01011010=10011010; Cout=0, Overflow=1 (2) 11000100+10100110=01101010; Cout=1, Overflow=1 (3) 00101101+10110010(=−78)=11100000+1=11100001→ result reads negative: −33 ✓ (4) SM:00100110→1|0100110; 1's comp: 11011001; 2's comp: 11011010 (5) 00011110+11101100=00001010 = +10 ✓ Cout=1, Overflow=0

**§3 IEEE 754:** (1) 1 10000010 01101100000000000000000 (2) 0 01111111 000...0 — exponent field = exactly the bias (127), since actual exponent = 0 (3) 1.3125 × 2² = 5.25 (4) bias = 2¹⁰−1 = 1023 (5) 100.0=1100100.0=1.1001×2⁶; exp=6+127=133=10000101; mantissa=100100000000000

**§4 Booth's/Division:** (1) Add multiplicand to partial product (2) sequence ends AC=11101101 → −21 ✓ (3) quotient bit=1, no restore, continue (4) non-restoring never adds back immediately — it adjusts on the *next* step based on the sign, saving a step (5) full 4-cycle trace: standard Booth steps yield product = −20

**§5 Hamming Code:** (1) r=4 (2⁴=16≥11+4+1=16) (2) r=4, n=12 (3) syndrome=000 → no error, code is correct (4) powers of 2 give each parity bit a unique, non-overlapping set of positions to check via binary place-value logic (5) single parity bit only *detects* one error; Hamming code *detects and corrects* it by locating the exact position

**§6 Generations:** (1) 3rd gen — smaller size, more reliability, lower cost (2) 1st gen — vacuum tubes (3) 4th gen uses microprocessors (a whole CPU on one chip) vs. 3rd gen's ICs (4) Von Neumann: shared instruction/data memory; Harvard: separate memories (5) 5th generation

**§7 Types/Classification:** (1) mainframe = transaction-heavy business use; supercomputer = raw computational speed for scientific problems (2) mainframe: banking systems; minicomputer: departmental servers (3) speed, memory capacity, cost, portability (4) generally classified as a microcomputer-class device given single-processor personal use (5) "super" is about sustained processing power/throughput for complex tasks, not just clock frequency

**§8 Functional Units/CPU:** (1) MAR holds the address, MDR holds the data at that address (2) MAR←PC; MDR←M[MAR]; IR←MDR; PC←PC+1 (3) separate memories mean instruction fetch and data access can happen simultaneously (4) tracks the top of the stack, adjusted as items are pushed/popped for the call/return addresses (5) Instruction Register (IR), used by CU for decoding

**§9 Buses/Arbitration:** (1) address only needs to flow one way (CPU specifies location); data must flow both ways (read and write) (2) daisy chaining, polling, independent request — as detailed in Section 9 (3) prevents bus conflicts when multiple devices want control simultaneously (4) cycle stealing takes one cycle at a time between CPU ops; burst takes the whole block at once, blocking the CPU (5) Bus Request (BR) from device, Bus Grant (BG) passed along the chain

**§10 Register/Memory Transfer:** (1) AC ← M[MAR] (2) Read: Memory→CPU, non-destructive; Write: CPU→Memory, destructive/overwrites (3) avoids n² wiring complexity as more registers are added (4) R1 ← R1 − R2 (5) PC supplies data (source), MAR receives it (destination)

**§11 Adders:** (1) it pre-computes carries directly from inputs using extra gates instead of waiting for the ripple (2) Sum=A⊕B, Carry=AB (3) Sum=A⊕B⊕Cin, Carry=AB+BCin+ACin (4) 8 full adders (5) CLA is faster but uses more gates/area/cost; ripple carry is cheaper but slower for wide words

**§12 Quick-Hit:** (1) Terabyte (2) Yes — it's a cache for page-table entries, so it is a memory structure (3) XOR=logic, SUB=arithmetic, MOV=data transfer, PUSH=stack (4) 16-bit instr − 2×3-bit reg fields − 2-bit mode field = 8 bits for opcode (5) 00110110 (=+108→+54, arithmetic shift preserves sign 0)

---

*Good luck for the quiz, Sam. Focus extra time on §2 (overflow rule) and §3 (IEEE 754 conversion) — both quizzes lean heavily on those two.*
