# Addressing Modes — Semester Exam Revision Sheet
**COA / CSA — Unit 2: Processor Organization & Addressing Modes**

## Definition (write this first in any answer)

> Addressing mode specifies the method of finding the **effective address (EA)** of the operand referenced by an instruction. It determines how the CPU interprets the address field of an instruction.

## The 10 Modes

| # | Mode | Definition | Example | Advantage | Disadvantage |
|---|------|------------|---------|-----------|---------------|
| 1 | Implied | Operand specified implicitly by the instruction itself; no address field needed. | `CMA` (complement accumulator) | Shortest instruction, no address bits needed | No flexibility — operand fixed |
| 2 | Immediate | Operand value is given directly within the instruction. | `MOV R1, #5` | No memory reference — fastest | Operand size limited by instruction length |
| 3 | Direct / Absolute | Address field contains the effective address of operand directly. | `MOV R1, [200]` | Simple, only 1 memory access | Limited address range (bound by address field size) |
| 4 | Indirect | Address field gives address of a memory location that holds the effective address. | `MOV R1, [[200]]` | Large address range (full memory word used as pointer) | 2 memory accesses — slower |
| 5 | Register | Operand is held in a register; register number given in instruction. | `MOV R1, R2` | Zero memory access — very fast | Limited by number of available registers |
| 6 | Register Indirect | Register holds the address of memory location containing the operand. | `MOV R1, [R2]` | Full memory address range, faster than Indirect | Needs an extra register to hold address |
| 7 | Auto-increment / Auto-decrement | Same as Register Indirect, but register content is automatically incremented/decremented after (or before) access. | `MOV R1,[R2]+` (then R2++) | Ideal for array/loop traversal — no separate increment instruction | Needs extra hardware control logic |
| 8 | Indexed | EA = Index Register content + Offset (given in instruction). | `MOV R1, [R2+4]` | Efficient for array element access | Extra addition needed to compute EA |
| 9 | PC-Relative | EA = Program Counter (PC) + Offset given in instruction. | Branch/Jump instructions | Enables position-independent code | Limited range (small offset field) |
| 10 | Base Register | EA = Base Register content + Offset. | `MOV R1, [BR+8]` | Useful for relocatable programs & structures | Needs an extra dedicated base register |

## Computable vs Non-Computable Modes

- **Non-computable (1–6):** Implied, Immediate, Direct, Indirect, Register, Register Indirect — EA is given directly or needs no arithmetic.
- **Computable (7–10):** Auto-incr/decr, Indexed, PC-Relative, Base Register — EA requires an addition/subtraction (Index+Offset, PC+Offset, Base+Offset, Register±step).

## Memory Accesses Needed for Operand (used in numericals)

| Mode | Accesses |
|------|----------|
| Immediate / Register | 0 |
| Direct / Register Indirect / Indexed / Base | 1 |
| Indirect | 2 |

## Common Exam Questions — Ready Answers

**Q: Differentiate between Direct and Indirect addressing mode.**
A: Direct: address field gives operand's address directly (1 memory access). Indirect: address field gives address of a location containing the operand's address (2 memory accesses). Indirect allows a larger effective address range since the full memory word (not just the instruction's address field) holds the address.

**Q: Differentiate between Indexed and Base Register addressing mode.**
A: Both compute EA = Register + Offset. Index register typically holds a variable offset (used in loops for array traversal); Base register typically holds a fixed starting address of a program/data block, with the offset locating elements relative to it.

**Q: Why is Register mode faster than Direct mode?**
A: Register mode needs zero memory accesses (data already in a CPU register); Direct mode needs one memory access to fetch the operand from memory. Register access time is much less than memory access time.

**Q: Numerical — Indexed addressing, Index register R1 = 1000, offset = 20. Find EA and operand.**
A: EA = R1 + offset = 1000 + 20 = 1020. Operand = Memory[1020].

---
*Diagram tip: For Indirect / Register-Indirect, always draw — `Instruction[Address A] → Memory[A] = B (pointer) → Memory[B] = Operand`. Drawing this scores an extra mark in most university exams.*
