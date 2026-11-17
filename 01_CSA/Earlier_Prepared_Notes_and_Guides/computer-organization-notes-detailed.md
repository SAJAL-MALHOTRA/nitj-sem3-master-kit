# Computer Organization — Detailed Notes

---

## 1. Division — Restoring Method / Hardware Algorithm (Unsigned Binary Division)

### Why this algorithm exists
Computers can't do division the way we do it on paper directly in hardware — division is implemented as repeated **subtract-and-shift** operations, mimicking long division but using registers and shifts instead of "guessing" digits. The restoring method is one of the simplest hardware division algorithms.

### Registers involved
- **A** — accumulator register, initially 0. Holds the running remainder.
- **M** — holds the divisor.
- **Q** — holds the dividend at the start, and holds the quotient bits by the end.
- **count** — a counter initialized to n (number of bits), used to control how many iterations to run.

### Step-by-step algorithm
1. **Initialize:** A ← 0, M ← divisor, Q ← dividend, count ← n
2. **Repeat n times:**
   a. **Shift left** A and Q together as if they were one combined register (this brings the next bit of the dividend into play, similar to "bringing down the next digit" in manual long division).
   b. **Subtract:** A ← A − M
   c. **Check the sign of A:**
      - **If A ≥ 0 (YES branch):** the subtraction was valid, meaning M "fit" into that part of the dividend. Set Q₀ (the bit just shifted into Q) to 1.
      - **If A < 0 (NO branch):** the subtraction was invalid (M doesn't fit). **Restore** A by adding M back: A ← A + M. Set Q₀ to 0 (this is where the name "restoring" comes from — you restore A to what it was before the failed subtraction).
   d. **count ← count − 1**
3. **Repeat until count = 0**, then stop.

### Result
- **Quotient** ends up sitting in register **Q**.
- **Remainder** ends up sitting in register **A**.

### Rules / assumptions
- Both divisor and dividend are assumed **positive** (this is an *unsigned* division algorithm).
- The quotient must be smaller than the dividend (standard division property).
- The remainder always takes the **same sign as the dividend** (a convention used when this algorithm is extended to signed numbers).

### Worked example: 13 ÷ 5
Given:
- Dividend = 13, Divisor = 5
- C (count) = 5 (this example works with 5-bit registers)
- M = 5 → binary 00101
- −M (2's complement of M) = 11011
- Q initialized = 01101 (binary for 13)

**Trace (each row is one iteration):**

| A (before) | Q | Operation | C (count) |
|---|---|---|---|
| 00000 | 01101 | init | 5 |
| 00000 | 11010 | Shift left A,Q | 5 |
| 11011 | 11010 | A ← A − M → A<0 (Q₀=0) | 4 |
| 00000 | 11010 | A+M → 00000 11010 | 4 |
| 00001 | 10100 | Shift left | 4 |
| 11100 | 10100 | A ← A − M → A<0 (Q₀=0) | 3 |
| 00001 | 10100 | A+M restore | 3 |
| 00011 | 01000 | Shift left | 3 |
| 11110 | 01000 | A ← A − M → A<0 (Q₀=0) | 2 |
| 00011 | 01000 | A+M restore | 2 |
| 00110 | 10000 | Shift left | 2 |
| 00001 | 10001 | A ← A − M → A≥0 (Q₀=1) | 1 |
| 00011 | 00010 | Shift left | 1 |
| 11110 | 00010 | A ← A − M → A<0 (Q₀=0) | 0 |
| 00011 | 00010 | A+M restore | 0 |

**Final result:**
- Q = 00010 (binary) = **2** → quotient
- A = 00011 (binary) = **3** → remainder

**Verification:** 13 = 5 × 2 + 3 ✓

---

## 2. Bus Arbitration

### The core problem
In a computer system, multiple devices (CPU, DMA controllers, I/O processors) may all want to use the same shared system bus at the same time. Since only **one device can control the bus at a time**, there must be a mechanism to decide who gets access — this is called **bus arbitration**.

- The device that currently controls the bus is called the **bus master**.
- A special hardware unit — the **bus arbiter** — decides which device becomes the bus master, based on some priority scheme.
- Once a device finishes its bus operation, it releases the bus so another device can use it.

### Key handshaking signals
- **BGT / BG (Bus Grant)** — signal sent from the controller/arbiter to a master, granting it access to the bus.
- **BRQ / BR (Bus Request)** — signal sent by a device to the controller, requesting bus access.
- **SACK (Select Acknowledge)** — an acknowledgment signal confirming that a particular device has been selected.

### Method 1: Daisy Chaining
**How it works:** All the bus masters (M1, M2, ..., Mn) are connected in a serial chain. There is a single shared BR line used by all masters to request the bus. When the controller grants the bus (BG), the grant signal is passed serially — first to M1, and if M1 doesn't need the bus, M1 passes the grant on to M2, and so on, until it finds a master that is actively requesting. That master "catches" the grant signal and does not pass it further, so it becomes the bus master.

**Advantages (A):**
- Simple and inexpensive circuitry
- Scalable — you can add more devices anywhere along the chain without much extra hardware

**Disadvantages (D):**
- Priority is fixed by physical position in the chain (devices closer to the controller always have higher priority)
- There's propagation delay as the grant signal ripples through each device in the chain
- If one device in the chain fails or malfunctions, it can block the grant signal from reaching devices further down — the whole system can fail

### Method 2: Rotating Priority / Polling Method
**How it works:** A central controller actively generates and cycles through the addresses of each master, checking each one to see if it's requesting the bus. Each master is only checked when the controller's address lines "point" to it.

**Advantages (A):**
- Doesn't structurally favor one device permanently — priority can "rotate"
- Relatively simple

**Disadvantages (D):**
- As the number of masters grows, more address lines are needed to enumerate/address them, making the controller more complex and slower to poll through all devices

### Method 3: Fixed Priority / Independent Request Method
**How it works:** Every single master gets its **own dedicated pair** of BR and BG lines connected directly to the controller. The controller has a built-in **priority decoder/encoder** that looks at all incoming requests simultaneously and grants the bus to whichever requesting device has the highest assigned priority.

**Advantages (A):**
- Fastest method — no serial delay, no polling delay; decision is essentially immediate
- Priorities can be reconfigured easily since they're resolved logically, not physically

**Disadvantages (D):**
- Most expensive in terms of hardware — needs a separate pair of wires for every single master, so wiring complexity grows quickly with the number of devices

### Starvation
A potential problem in bus arbitration: a low-priority (or unlucky-positioned) device might request the bus repeatedly but **never actually get it**, because higher-priority devices keep winning. This is called **starvation**. Daisy chaining is especially prone to this since priority is fixed by position — a device at the end of the chain could starve if the devices ahead of it are constantly busy. A good arbitration scheme tries to guarantee fairness so this doesn't happen indefinitely.

---

## 3. DMA (Direct Memory Access)

### Why DMA exists
Normally, if the CPU wants to transfer a block of data (say, from a disk to memory), it would have to execute instructions to move each word one at a time — this wastes CPU cycles on a task that is fundamentally just "copy data from A to B." **DMA** solves this by giving I/O devices the ability to transfer data directly to/from memory **without the CPU being involved in every single word transferred**.

### System layout
- The CPU, memory, and the DMA controller are all connected via three buses: **address bus**, **data bus**, and **control bus**.
- The **DMA controller** sits as an intermediary between the I/O device and memory.

### Internal registers of the DMA controller
- **Address register** — holds the memory address where the next word should be read from or written to.
- **Word count register** — holds the number of words still left to transfer; decrements after each word transferred.
- **Control register** — specifies the mode of transfer (read/write) and other control information.

### How a DMA transfer happens (step by step)
1. The CPU initializes the DMA controller's registers (start address, word count, direction of transfer) via the address/data/control buses, then continues executing its own program.
2. When the I/O device is ready to transfer data, the DMA controller issues a **Bus Request (BR)** to the CPU.
3. The CPU, at a convenient point (usually at the end of a bus cycle), releases control of the buses and asserts **Bus Grant (BG)**.
4. The DMA controller now directly manages the address/data/control buses and moves data between the I/O device and memory — this path is shown as the "I/O data" flow to/from the I/O block.
5. Handshaking with the I/O device itself uses:
   - **DMA Request (DRQ)** — signal from the I/O device to the DMA controller saying it's ready to send/receive data
   - **DMA Acknowledge (DACK)** — signal from the DMA controller back to the I/O device confirming the transfer is happening
6. Once the word count register reaches zero, the transfer is complete, and the DMA controller releases the bus back to the CPU (often interrupting the CPU to signal completion).

### Key benefit
Because the CPU only sets up the transfer and is notified when it's done, it is **free to do other work** during the actual data movement — this dramatically improves system efficiency for large data transfers (disk I/O, network I/O, etc.).

---

## 4. Unsigned Multiplication — Hardware Multiplication Algorithm

### Concept
Just like division, multiplication in hardware is implemented via repeated **shift-and-add** operations rather than a single multiply circuit doing everything at once (in simple designs). This mimics how multiplication is done by hand: for each bit of the multiplier, you either add a shifted copy of the multiplicand or not, depending on whether that bit is 1 or 0.

### Registers involved
- **C** — a carry/overflow bit, extends the accumulator so sums that overflow beyond A can be captured.
- **A** — accumulator, initially 0. Accumulates partial sums.
- **M** — holds the multiplicand.
- **Q** — holds the multiplier initially, and receives the lower half of the product bits as the algorithm shifts.
- **count** — counts down from n (number of bits), controlling loop iterations.

### Step-by-step algorithm
1. **Initialize:** C,A ← 0, M ← multiplicand, Q ← multiplier, count ← n
2. **Repeat n times:**
   a. **Check Q₀** (the least significant bit of Q, i.e., the current bit of the multiplier being processed):
      - **If Q₀ = 1:** perform C,A ← A + M (add the multiplicand into the accumulator; C captures any carry out)
      - **If Q₀ = 0:** do nothing (skip the addition this round)
   b. **Shift right** C, A, and Q together as a single combined unit — this moves the next bit of the multiplier into Q₀ for the next iteration, and also shifts the accumulated partial product down.
   c. **count ← count − 1**
3. **Repeat until count = 0**, then stop.

### Result
The final product (which can be up to 2n bits for two n-bit numbers) is found in the concatenation of registers **A** and **Q** (A holds the upper/more-significant half, Q holds the lower/less-significant half).

### Worked example
Using M = 1011 (multiplicand), the notes trace C, A, Q through each cycle — each row shows whether an addition happened (based on Q₀) followed by a right shift, gradually building up the product bit by bit across the iterations until count reaches 0.

---

## 5. Booth's Algorithm — Signed Multiplication

### Why Booth's algorithm exists
The straightforward shift-and-add multiplication algorithm works for **unsigned** numbers, but doesn't directly handle **signed (2's complement)** numbers correctly, and it can also be inefficient — every 1-bit of the multiplier forces an addition. Booth's algorithm:
1. Correctly handles **signed multiplication** directly in 2's complement form.
2. Can be more efficient in the special case where the multiplier has long runs of consecutive 1s (since it only needs to add/subtract at the *boundaries* of the run rather than at every bit).

### Registers involved
- **A** — accumulator, initially 0.
- **Q₋₁** — an extra bit placed just to the right of Q, initialized to 0. This is the "history" bit representing what the previous Q₀ was.
- **M** — holds the multiplicand.
- **Q** — holds the multiplier.
- **count** — counts down from n (number of bits).

### The Booth recoding rule
At each step, look at the pair **(Q₀, Q₋₁)** — the current LSB of Q, together with the bit that was the LSB just before the last shift:

| Q₀ | Q₋₁ | Meaning | Action |
|---|---|---|---|
| 0 | 1 | end of a run of 1s (transitioning from 1s back to 0) | **A ← A + M** |
| 1 | 0 | start of a run of 1s (transitioning from 0s into 1s) | **A ← A − M** |
| 0 | 0 | inside a run of 0s | No operation |
| 1 | 1 | inside a run of 1s | No operation |

### Step-by-step algorithm
1. **Initialize:** A = 0000, Q₋₁ = 0, M = multiplicand, Q = multiplier, count = n
2. **Repeat n times:**
   a. Look at (Q₀, Q₋₁) and perform the corresponding action from the table above (add M, subtract M, or nothing).
   b. **Arithmetic shift right** A, Q, and Q₋₁ together as one combined unit (arithmetic shift preserves the sign bit, which is essential since we're working with signed numbers).
   c. **count ← count − 1**
3. **Repeat until count = 0**, then stop.

### Result
The final signed product is found in the combined A,Q registers.

### Why it can be more efficient
Consider a multiplier like `011110` (a run of four 1s surrounded by 0s). A naive algorithm would perform 4 separate additions (one per 1-bit). Booth's algorithm instead recognizes the entire run as a single "block": it does **one subtraction at the start** of the run and **one addition at the end** of the run, replacing 4 additions with just 2 operations total.

---

## 6. System Bus (Address / Data / Control)

A **bus** is a communication system that transfers data between components inside a computer, or between computers. It's essential for minimizing the number of physical connections needed — instead of every component having a dedicated wire to every other component, they all share a common set of lines (the bus).

Physically, buses consist of wires, circuits, and cables. The CPU, memory, and I/O devices are all connected via buses, and the bus specifies how data transfer and interfacing happen.

### Address Bus
- A collection of wires used to identify a **particular location** in main memory (or an I/O device) that a transfer should occur with.
- It is **unidirectional** — the CPU always sends addresses out; addresses don't flow back into the CPU.
- Info sent on the address bus describes the memory location a data transfer will target.
- Transports the memory addresses which the processor uses to access read/write data.
- Its **width** (number of lines) directly determines how many unique memory locations can be addressed (an n-bit address bus can address 2ⁿ locations).

### Data Bus
- A collection of wires through which data is actually transferred from one part of the computer to another.
- Highway on which data travels within a computer, or between a computer and peripheral devices.
- The main purpose is to transfer data between the microprocessor and I/O devices/memory.
- **Bidirectional** — data can flow from CPU to memory (write) and from memory to CPU (read).
- Also transfers instructions being fetched from memory to the processor.
- Its **width** (e.g., 8-bit, 16-bit, 32-bit, 64-bit) determines how much data can be moved in a single bus cycle — a wider data bus generally means faster data transfer.

### Control Bus
- Carries **control and timing signals** needed to manage and coordinate all the other activities within a computer configuration.
- Main purpose: to transmit control signals from the CPU to memory and I/O devices, and to receive status/response signals back from them.
- Lines can be **unidirectional or bidirectional** depending on the type of control signal (e.g., a "read" signal goes from CPU outward, while an "interrupt request" signal comes from a device into the CPU).
- Used to manage and coordinate all the read/write and interrupt requests between CPU and peripherals.

---

## 7. Carry Lookahead Adder (Overview)

### The problem it solves
A simple **ripple carry adder** (built by chaining full adders) is slow for wide numbers because each bit's sum depends on the carry from the previous bit — the carry has to "ripple" through every stage before the final sum is known.

### How carry lookahead works (as sketched in the notes)
Using **generate (G)** and **propagate (P)** signals for each bit position, carry-lookahead logic computes each carry (C₀, C₁, C₂, C₃, ...) directly using AND/OR gate combinations of the input bits, rather than waiting for the carry to propagate stage by stage. This is combined with half-adder (HA) circuits to produce the sum bits and carry-out for each stage in parallel, dramatically speeding up wide additions compared to a pure ripple-carry design.

### Bit-width note
If you want to add a **J-bit** number and a **K-bit** number together, you need an adder that is **(max(J,K) + 1) bits wide** — the extra bit accommodates the possibility of a carry-out/overflow from the addition.

---

## 8. Instruction Formats & Addressing Architectures

### Setup
Consider the expression:

```
F = C × (A + B) − (D / E)
```

This single computation is used to illustrate how the exact same logic looks different depending on how many operand addresses an instruction format allows.

### Zero-Address Instructions (Stack-Based Architecture)
- Operands are **never explicitly named** in the instruction — everything is implicit, based on a stack.
- Only **PUSH** and **POP** instructions actually touch memory; all arithmetic instructions operate purely on whatever is currently on top of the stack.
- This is also called a "stack-based" architecture.

```
PUSH A        ; Stack: A
PUSH B        ; Stack: A, B
ADD           ; Stack: (A+B)
PUSH C        ; Stack: (A+B), C
MUL           ; Stack: (A+B)×C
STORE T1      ; T1 = (A+B)×C ; stack empties
PUSH D        ; Stack: D
PUSH E        ; Stack: D, E
DIV           ; Stack: (D/E)
STORE T2      ; T2 = D/E
PUSH T1       ; Stack: T1
PUSH T2       ; Stack: T1, T2
SUB           ; Stack: T1 − T2
STORE F       ; F = T1 − T2  = C(A+B) − D/E
```
- Memory location `[X]` here effectively corresponds to "top of stack" conceptually — the stack itself holds intermediate values instead of named registers/memory locations.

### One-Address Instructions (Accumulator-Based Architecture)
- Uses a single **implicit** register — the **accumulator (AC)** — for one operand and the result of every operation.
- Every instruction implicitly reads from AC and/or writes back into AC.

```
LOAD A      ; AC ← M[A]
ADD B       ; AC ← AC + M[B]
MUL C       ; AC ← AC × M[C]
STORE T1    ; T1 ← AC
LOAD D      ; AC ← M[D]
DIV E       ; AC ← AC / M[E]
STORE T2    ; T2 ← AC
LOAD T1     ; AC ← T1
SUB T2      ; AC ← AC − T2
STORE F     ; F ← AC
```
- Format: `[opcode | operand]` — only one explicit memory address per instruction; the other operand and the destination are always AC implicitly.

### Two-Address Instructions (Register/Memory-Based Architecture)
- The **first address** acts as **both a source and the destination** — it gets overwritten with the result.
- Format: `[opcode | dest/source1 | source2]`

```
MOV R1,A    ; R1 ← M[A]
ADD R1,B    ; R1 ← R1 + M[B]
MOV R2,C    ; R2 ← M[C]
ADD R2,D    ; R2 ← R2 + M[D]
MUL R1,R2   ; R1 ← R1 × R2
MOV X,R1    ; M[X] ← R1
```
- **Important caveat:** because the first operand's original value is destroyed after operations like `ADD R1,R2`, if you need that original value again later, you'd have to reload it from memory — which costs an extra instruction. This tradeoff is one motivation for moving to a 3-address format.

### Three-Address Instructions (General Register-Based Architecture)
- Also called "quadruple" format since it can specify an opcode plus three separate address fields, keeping all source operands intact (nothing gets destructively overwritten unless explicitly stored).
- Format: `[opcode | addr1 | addr2 | addr3]`

```
LOAD  R1,A
LOAD  R2,B
ADD   R1,R2
LOAD  R3,C
LOAD  R4,D
SUB   R3,R4
MUL   R1,R3
STORE E,R1
```

### Key architectural principle
Across all these formats, note that **LOAD, MOV, and STORE are the only instructions that touch memory** (these are called *data transfer* operations). ALU operations (ADD, SUB, MUL, DIV) operate purely on registers/accumulator, never directly on memory. This strict separation — where only dedicated load/store instructions move data between memory and registers, and all computation happens register-to-register — is exactly the foundational principle of **RISC (Reduced Instruction Set Computer) / load-store architecture**.

---

## 9. Processor Organization — General Overview of the CPU

### What the CPU actually is
The CPU (Central Processing Unit) is the part of the computer that **fetches instructions from memory, decodes them, and executes them**. To carry out this job, it needs three main hardware sections:

1. **Register Set** — a collection of small, extremely fast storage locations located directly inside the CPU (examples: AC — accumulator, PC — program counter, IR — instruction register, GPRs — general purpose registers).
2. **ALU (Arithmetic Logic Unit)** — performs all arithmetic (add, subtract, multiply, etc.) and logical (AND, OR, NOT, comparisons, etc.) operations.
3. **Control Unit** — generates the timing and control signals that tell every other part of the computer *what to do* and *when to do it*, orchestrating the fetch-decode-execute cycle.

### Organization Types

| Organization | Description |
|---|---|
| **Single Accumulator Organization** | One special register (the accumulator, AC) always supplies one operand for an operation and always receives the result. |
| **General Register Organization** | Several registers (R0, R1, R2, ...) can each hold operands; individual instructions specify exactly which register(s) to use for each operation. |
| **Stack Organization** | Operands are pushed onto a stack; operations pop their operands off the stack and push the result back on. No register names ever appear explicitly in the instructions at all. |

### Problem with Single-Accumulator Design
Using only a single AC to hold intermediate results is architecturally simple, but it's **slow**: every intermediate result computed during a multi-step calculation must be written back out to memory before the AC is free to be used for the next sub-computation, because there's nowhere else inside the CPU to "park" a value temporarily. This creates a lot of unnecessary memory traffic.

### General Register Organization (Solving that problem)
Modern CPUs solve the single-accumulator bottleneck by providing an entire **bank of registers**. Since all these registers live inside the CPU, moving data between them is dramatically faster than going all the way out to main memory. Instructions can explicitly name **which register** should act as the source and which as the destination for any given operation, avoiding unnecessary round-trips to memory.

### Internal Structure — "Bus-Organized" CPU
A common way to physically wire up a general-register CPU internally:
- **Register array** = R0, R1, R2, ..., Rn (the GPR bank). Each register has both an input connection and an output connection to the internal buses.
- **3 internal buses**: Bus A and Bus B each feed one of the ALU's two input ports; the ALU's output is sent back over a third path/port so that it can be written into *any* register in the array.
- **MUX (multiplexer)**: selects which register's output is currently placed onto Bus A and which is placed onto Bus B (i.e., picks the ALU's two operands).
- **Decoder**: on the destination/write side, decides which specific register should receive and store the ALU's output result.

**Diagram concept:**
```
   A ─┐
      ├─► ALU ─► O/P register ─► C ─► back into a register
   B ─┘
    ↑     ↑
 Register file (R0 ... Rn)
```

### Control Word Fields
Every single micro-operation carried out by this internal datapath is governed by a **control word**, which has separate fields for:
- **SELA(x)** — selects which register supplies operand A
- **SELB(x)** — selects which register supplies operand B
- **SELD(x)** — selects which register receives (is the destination of) the result
- **OPR(x)** — selects which operation the ALU should perform

**Worked example:** `R1 ← R2 + R3`

```
SELA = R2      (feed R2 into ALU input A)
SELB = R3      (feed R3 into ALU input B)
SELD = R1      (write ALU result into R1)
OPR  = ADD     (ALU performs addition)
```

### Why this matters
This bus-based register file design with a control-word-driven ALU is essentially the internal skeleton of how real CPUs execute register-to-register operations, and it directly supports the load-store / RISC philosophy discussed in Section 8 — since data only needs to be pulled from memory into a register once (via LOAD), and can then be reused freely across many register-to-register ALU operations before finally being written back (via STORE).

---

## 10. Stack Organization

### What a stack is
A **stack** is a data structure that follows **LIFO** order — **Last In, First Out**. The most recently added item is always the first one removed.

### Core operations
- **PUSH** — adds ("inserts") a new item at the top of the stack.
- **POP** — removes ("deletes") the item currently at the top of the stack (this involves reading the value out, and then freeing/adjusting the top-of-stack position).

### Stack Pointer (SP)
A dedicated register, the **Stack Pointer**, always holds the memory address of the current top-of-stack element. Every PUSH and POP operation updates SP.

### Operation details
```
PUSH:
    SP ← SP + 1          ; move pointer up to the next free slot
    M[SP] ← DR            ; write the data register's value into that slot

POP:
    DR ← M[SP]             ; read the value at the current top-of-stack address
    SP ← SP − 1            ; move pointer back down, "freeing" that slot
```
(Note: depending on convention, some systems increment/decrement SP in the opposite order — i.e., decrement-then-store for PUSH — but the core mechanics are the same: SP always tracks the top.)

### Stack status flags
Two flags are used to detect edge conditions:
- **FULL** — set when SP reaches the maximum address allocated to the stack. If a PUSH is attempted while FULL, this causes a **stack overflow** condition.
- **EMPTY** — set when SP returns to the base/starting address of the stack (i.e., nothing left to pop). If a POP is attempted while EMPTY, this causes a **stack underflow** condition.

### Register Stack
A **small, dedicated hardware stack** built from a limited number of registers *inside the CPU itself*, used purely for stack operations. It's very fast (since it's on-chip), but its size is fixed and small by nature — it cannot grow beyond however many registers were physically dedicated to it.

### Memory Stack
Instead of using a small dedicated register file, a **portion of main memory** is reserved to act as the stack, and the Stack Pointer is simply a normal CPU register that points into that reserved memory region.

**Advantage:** This allows an effectively **much larger (almost unlimited) stack size**, limited only by how much memory is actually available — this is what real, practical computer systems actually use for their runtime call stacks, rather than relying on a small fixed on-chip register stack.

---

## Summary Table — Instruction Format Comparison

| Format | Explicit Operands | Implicit Storage | Example (ADD) |
|---|---|---|---|
| Zero-address | 0 | Stack (top two elements) | `ADD` |
| One-address | 1 | Accumulator | `ADD B` → AC ← AC + M[B] |
| Two-address | 2 | First operand is also destination | `ADD R1,R2` → R1 ← R1+R2 |
| Three-address | 3 | None — separate destination | `ADD R1,R2,R3` → R1 ← R2+R3 |

## Summary Table — Multiplication/Division Algorithms

| Algorithm | Purpose | Core operation per bit | Handles signed numbers? |
|---|---|---|---|
| Restoring Division | Unsigned division | Shift, subtract, restore if negative | No |
| Shift-and-Add Multiplication | Unsigned multiplication | Shift, add if bit=1 | No |
| Booth's Algorithm | Signed multiplication | Shift, add/subtract based on bit-pair transitions | Yes |
