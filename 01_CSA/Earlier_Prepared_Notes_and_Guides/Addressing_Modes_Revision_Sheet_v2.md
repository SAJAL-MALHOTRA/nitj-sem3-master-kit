# Addressing Modes — Semester Exam Revision Notes
**COA / CSA — Unit 2: Processor Organization & Addressing Modes**

## Definition (write this first in any answer)

> Addressing mode specifies the method of finding the **effective address (EA)** of the operand referenced by an instruction. It determines how the CPU interprets the address field of an instruction.

---

## 1. Implied Mode
- **Definition:** Operand specified implicitly by the instruction itself; no address field needed.
- **Example:** `CMA` (complement accumulator)
- **Advantage:** Shortest instruction, no address bits needed
- **Disadvantage:** No flexibility — operand fixed

## 2. Immediate Mode
- **Definition:** Operand value is given directly within the instruction.
- **Example:** `MOV R1, #5`
- **Advantage:** No memory reference — fastest
- **Disadvantage:** Operand size limited by instruction length

## 3. Direct / Absolute Mode
- **Definition:** Address field contains the effective address of the operand directly.
- **Example:** `MOV R1, [200]`
- **Advantage:** Simple, only 1 memory access
- **Disadvantage:** Limited address range (bound by address field size)

## 4. Indirect Mode
- **Definition:** Address field gives the address of a memory location that holds the effective address.
- **Example:** `MOV R1, [[200]]`
- **Advantage:** Large address range (full memory word used as pointer)
- **Disadvantage:** 2 memory accesses — slower

## 5. Register Mode
- **Definition:** Operand is held in a register; register number given in instruction.
- **Example:** `MOV R1, R2`
- **Advantage:** Zero memory access — very fast
- **Disadvantage:** Limited by number of available registers

## 6. Register Indirect Mode
- **Definition:** Register holds the address of the memory location containing the operand.
- **Example:** `MOV R1, [R2]`
- **Advantage:** Full memory address range, faster than Indirect
- **Disadvantage:** Needs an extra register to hold the address

## 7. Auto-increment / Auto-decrement Mode
- **Definition:** Same as Register Indirect, but register content is automatically incremented/decremented after (or before) access.
- **Example:** `MOV R1, [R2]+` (then R2++)
- **Advantage:** Ideal for array/loop traversal — no separate increment instruction needed
- **Disadvantage:** Needs extra hardware control logic

## 8. Indexed Mode
- **Definition:** EA = Index Register content + Offset (given in instruction).
- **Example:** `MOV R1, [R2+4]`
- **Advantage:** Efficient for array element access
- **Disadvantage:** Extra addition needed to compute EA

## 9. PC-Relative Mode
- **Definition:** EA = Program Counter (PC) + Offset given in instruction.
- **Example:** Used in branch/jump instructions
- **Advantage:** Enables position-independent code
- **Disadvantage:** Limited range (small offset field)

## 10. Base Register Mode
- **Definition:** EA = Base Register content + Offset.
- **Example:** `MOV R1, [BR+8]`
- **Advantage:** Useful for relocatable programs & structures
- **Disadvantage:** Needs an extra dedicated base register

---

## Computable vs Non-Computable Modes

**Non-computable (1–6):** Implied, Immediate, Direct, Indirect, Register, Register Indirect
→ EA is given directly or needs no arithmetic.

**Computable (7–10):** Auto-incr/decr, Indexed, PC-Relative, Base Register
→ EA requires an addition/subtraction (Index+Offset, PC+Offset, Base+Offset, Register±step).

---

## Memory Accesses Needed for Operand (used in numericals)

- **0 accesses:** Immediate, Register
- **1 access:** Direct, Register Indirect, Indexed, Base Register
- **2 accesses:** Indirect

---

## Common Exam Questions — Ready Answers

**Q: Differentiate between Direct and Indirect addressing mode.**
A: Direct — address field gives operand's address directly (1 memory access). Indirect — address field gives address of a location containing the operand's address (2 memory accesses). Indirect allows a larger effective address range since the full memory word (not just the instruction's address field) holds the address.

**Q: Differentiate between Indexed and Base Register addressing mode.**
A: Both compute EA = Register + Offset. Index register typically holds a variable offset (used in loops for array traversal); Base register typically holds a fixed starting address of a program/data block, with the offset locating elements relative to it.

**Q: Why is Register mode faster than Direct mode?**
A: Register mode needs zero memory accesses (data already in a CPU register); Direct mode needs one memory access to fetch the operand from memory. Register access time is much less than memory access time.

**Q: Numerical — Indexed addressing, Index register R1 = 1000, offset = 20. Find EA and operand.**
A: EA = R1 + offset = 1000 + 20 = 1020. Operand = Memory[1020].

---

**Diagram tip:** For Indirect / Register-Indirect, always draw:
`Instruction[Address A] → Memory[A] = B (pointer) → Memory[B] = Operand`
Drawing this scores an extra mark in most university exams.
