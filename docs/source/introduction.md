# Introduction

Human-readable ULR IL (UIL) read much like an assembly language, with opcode mnemonics followed by operands. Sections of code are separated by method declarations contained withing type declarations.

The UIL environment does not contain any registers like an assembly environment would, rather, volatile data (which ends its lifetime at the end of UIL sections/scopes and methods) is stored on an evaluation stack, function-volatile data (which reaches the end of its lifetime at the end of a method) is stored in local variables (and argument-passed local variable storage locations), and nonvolatile data (data attached to objects or static field data) is stored in ULR instance or static fields.

All ULR operations take non-compile-time operands from the evaluation stack. All UIL program data lives on the evaluation stack at some point and can then be transferred to a more permanent storage location via a `StXXX` instruction.

All values/operands read off of the evaluation stack by an operation are also popped off of the evaluation stack.