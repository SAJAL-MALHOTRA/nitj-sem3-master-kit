# CSA Notes — Registers, Computer Architecture, Bus, and Memory Organization

Detailed explanatory notes based on your class notes (the 5 pages you just shared). Written to be read start-to-finish, not just crammed.

---

## 1. Registers

A **register** is a small, extremely fast storage location built directly inside the CPU. Registers exist because going all the way to main memory for every single value the processor touches would be far too slow — so the CPU keeps whatever it's actively working with in these tiny on-chip slots instead.

**Types of registers and what each one is for:**

- **Address Register** — stores an address (a location), not a value. When the CPU needs to point at somewhere in memory, this is where that pointer lives.
- **Data Register** — stores the actual data or variable being worked on, as opposed to an address.
- **Accumulator (AC)** — the register the ALU uses to hold **temporary/intermediate values** during a computation. If you're computing `c = a + b`, the running result sits in the accumulator before it's written anywhere permanent.
- **Program Counter (PC)** — holds the address of the instruction to execute **next**, not the one currently executing. This trips people up: PC always points *ahead*. After each fetch, PC auto-increments to keep pointing at the next instruction in sequence.
- **Instruction Register (IR)** — holds the instruction that is *currently* being decoded/executed (this is the complement to PC — PC looks forward, IR holds the present).
- **Temporary Register** — holds an intermediate value mid-operation that isn't the final answer yet — a scratch space during multi-step microoperations.
- **Input Register / Output Register** — buffer data flowing in from, or out to, I/O devices, so the CPU and slower I/O hardware don't have to move data at exactly the same speed.

**Why you sometimes need more than one register for what looks like a simple line of code:**
Your notes give a clean example — for `a = 5`, `b = 6`, `c = a + b`, you actually need **three registers**, not one:
```
R1 ← 5        (holds a)
R2 ← 6        (holds b)
R3 ← R1 + R2  (holds c — the destination is separate from the sources)
```
The sum can't just overwrite R1 or R2 in place inside a clean register-transfer model — the result needs its own destination register. This is exactly the "register transfer" notation you'll see in Unit 1 (`R2 ← R1`, `R3 ← R1 + R2`, `MOV` = the informal shorthand for "move/transfer").

**Recommended reference books** (as noted on your page): Morris Mano (*Computer System Architecture*), Hennessy & Patterson, and William Stallings — Mano is your primary text; the other two are good for cross-checking definitions if a topic feels unclear.

---

## 2. Von Neumann vs. Harvard Architecture

Both describe **how instructions and data are organized in memory relative to each other** — this is a structural/organizational distinction, separate from what the registers above actually do.

**Von Neumann Architecture (1945, J. V. Neumann):**
- Instructions and data are stored in the **same memory**.
- Introduced the **stored-program concept** — the idea that a program's instructions live in memory just like data does, instead of being hardwired — which is what makes general-purpose computing possible at all.
- Almost every general-purpose computer you use today is fundamentally Von Neumann.

**Harvard Architecture (1939, H. Aiken):**
- Instruction memory and data memory are **physically separate**.
- Because the two memories are independent, the CPU can fetch an instruction and access data **at the same time**, instead of competing for the same memory bus — this is the main performance advantage over Von Neumann.
- Common in DSPs and some embedded microcontrollers where predictable, fast instruction fetch matters more than flexibility.

**A simple way to remember the CPU + memory picture underneath both:**
```
Input  →  [ CPU: ALU + CU + Registers (R1, R2, R3, ...) ]  →  Output
                         ↕
                  Main Memory (MM)
                         ↕
                Secondary Memory (SM)
```
- Registers inside the CPU are called **General Purpose Registers (GPR)** when they're not dedicated to one specific role like PC or IR.
- **Reading** memory = Main Memory content → CPU (content is preserved, nothing is destroyed).
- **Writing** memory = Processor data → Main Memory (this **overwrites** whatever was at that location before).

---

## 3. The Three Major Components of a Computer & the Bus

Every computer, at the block-diagram level, is three components wired together:

1. **Processor (CPU)** — contains the ALU (Arithmetic Logic Unit, does the actual computing) and CU (Control Unit, sequences everything and issues control signals) plus its registers.
2. **I/O** — input and output devices.
3. **Memory** — RAM and beyond.

**These three are connected by the Bus** — literally just a bundle/combination of wires that data and control signals travel across. There is no other path between them; every byte that moves between CPU, memory, and I/O moves over this bus.

**The bus splits into three logical buses**, each with a different job and a different direction:

| Bus | Direction | What travels on it |
|---|---|---|
| **Address Bus** | Unidirectional — CPU → Memory/I/O only | The location the processor wants to access. Only the CPU generates addresses, so this bus only ever needs to carry information one way. |
| **Data Bus** | Bidirectional | The actual data itself — flows CPU→memory on a write, memory→CPU on a read. |
| **Control Bus** | Bidirectional | Control/status signals — read/write, clock, interrupt, HOLD, ready, etc. |

**Why the Control Unit issues a HOLD signal:** when a DMA transfer or an interrupt needs the bus, the CU can release control of the bus to that device by asserting HOLD — this is how the CPU "steps back" and lets another device drive the bus temporarily (ties directly into bus arbitration, covered in the main study guide).

---

## 4. Memory Size Calculation

The core formula, and the one thing every "how big is this memory" question boils down to:

> **Total memory size = Number of addressable locations × size of each addressable location**

If the address bus/address field has **n bits**, the memory has **2ⁿ** distinct addressable locations (0 through 2ⁿ−1).

**Standard capacity prefixes** (know these cold):
| Power of 2 | Name |
|---|---|
| 2¹⁰ | Kilobyte (KB) |
| 2²⁰ | Megabyte (MB) |
| 2³⁰ | Gigabyte (GB) |
| 2⁴⁰ | Terabyte (TB) |
| 2⁵⁰ | Petabyte (PB) |

**Worked example from your notes — a 32 GB memory, expandable up to 256 GB:**
```
256 GB = 2⁸ × 2³⁰ bytes = 2³⁸ bytes
```
So a memory that needs to address up to 256 GB, byte by byte, needs **38 address bits** — because 2³⁸ is the smallest power of 2 that covers 256 GB worth of individually-addressable bytes.

**Worked example — 5-bit address, byte-addressable:**
```
2⁵ = 32 memory cells, each cell = 1 byte → 32 bytes total memory
```
General pattern: **number of cells × cell size = total memory size**. If you're told the address width, you get the cell count (2^bits); if you're told cell size too, multiply straight through.

---

## 5. Byte-Addressable vs. Word-Addressable Memory

This distinction is about **what one single address actually points to**.

**Byte-addressable memory:** each memory cell holds exactly 1 byte (8 bits), and each address refers to exactly one of those bytes. This is the default assumption unless a question says otherwise.

**Word-addressable memory:** each address refers to one entire **word** — and a word is *not necessarily* 1 byte. If the word size is, say, 32 bits (4 bytes):
```
Address 0  →  bytes 0, 1, 2, 3
Address 1  →  bytes 4, 5, 6, 7
Address 2  →  bytes 8, 9, 10, 11
```
Each address jump moves 4 bytes ahead in physical memory, not 1.

**Why this matters:** for the exact same physical byte capacity, word-addressable memory needs **fewer address bits** than byte-addressable memory, because each address is "covering" more bytes at once. The trade-off is you lose the ability to point at an individual byte directly — you can only ever grab a whole word.

---

## 6. Memory Hierarchy

Memory isn't one uniform thing — it's a **pyramid**, trading speed against size and cost:

```
                Registers          ← fastest, smallest, most expensive/byte
               Cache (L1, L2)      ← SRAM, very fast
            Primary Memory (RAM)   ← moderate speed, moderate size
          Secondary Memory (SSD/HDD) ← slowest, largest, cheapest/byte
```

**Primary memory** (directly accessible by the CPU without going through I/O):
- **RAM** — volatile (loses all content the instant power is cut). This is the "working" memory a running program actually uses.
- **ROM** — non-volatile, typically holds firmware/boot instructions.
- **Cache** — sits between registers and RAM, holds recently/frequently used data so the CPU doesn't have to wait on full RAM access every time. Split into levels — **L1 is smaller and faster, closer to the core; L2 is larger and slightly slower.**

**Secondary memory** (non-volatile, holds data long-term, accessed through I/O):
- SSD, HDD, USB/pendrive.
- Typical scale in your notes: Primary memory ≈ 8 GB/16 GB; Secondary memory ≈ 256 GB/512 GB — secondary is an order of magnitude bigger, which is exactly the trade-off the pyramid describes.

**Why registers win on speed:** they sit physically inside the CPU core itself, so there's no bus transaction, no memory-controller round trip — just a direct wire to the ALU. Every step down the pyramid adds distance and protocol overhead, which is why the hierarchy exists at all: keep the *hottest* data as close to the ALU as physically possible, and only pay the slow-memory cost for what doesn't fit closer in.

---

*These notes pair with your `CSA_Quiz1_StudyGuide.md` — that file has the PYQ-solved versions and fresh practice questions for all of this; this one's for reading through the concepts cleanly before you get there.*
