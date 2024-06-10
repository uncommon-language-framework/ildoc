# Arithmetic Operations

## Numerical Data Manipulation

### `ldnc` - Load Numerical Constant
`ldnc <type> <constant>`

Takes two operands, the numerical type identifier and the constant expression. Pushes the value of the constant to the evaluation stack with the designated numerical type.

### `cstnv` - Cast Numerical Value
`cstnv <from_type> <to_type>`

Takes two operands, the source type identifier ('from') and the destination type identifier ('to'). Casts the last value on the evaluation stack from type `from_type` to type `to_type`.

### Numerical Type Identifiers
- `i8`, int8
- `i16`, int16
- `i32`, int32
- `i64`, int64
- `u8`, uint8
- `u16`, uint16
- `u32`, uint32
- `u64`, uint64
- `f32`, float32
- `f64`, float64

## Arithmetic Operations

### `add` - Add Two Numbers
`add <type>`

Takes one operand, the numerical type identifier specifying the size and type of the operation. Takes the last two values off of the evaluation stack as numbers of type `type` and adds them, pushing the result to the evaluation stack. Both stack operands **must** be of type `type`.

### `add` - Subtract Two Numbers
`sub <type>`

Takes one operand, the numerical type identifier specifying the size and type of the operation. Takes the last value off of the evaluation stack and subtracts it from the next value off of the evaluation stack, pushing the result to the evaluation stack. Both stack operands **must** be of type `type`.

### `mul` - Multiply Two Numbers
`mul <type>`

Takes one operand, the numerical type identifier specifying the size and type of the operation. Takes the last two values off of the evaluation stack as numbers of type `type` and multiplies them, pushing the result to the evaluation stack. Both stack operands **must** be of type `type`.

### `div` - Divide Two Numbers
`div <type>`

Takes one operand, the numerical type identifier specifying the size and type of the operation. Takes the last value off of the evaluation stack and divides the next value off of the evaluation stack by the aformentioned value, pushing the result to the evaluation stack. Both stack operands **must** be of type `type`. Effectively, the last value on the evaluation stack is the divisor, the next value is the dividend, and the quotient is pushed to the evaluation stack.