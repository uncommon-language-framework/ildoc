# Object Model Interaction

This page contains all information about object model interaction using UIL. Operations that deal with locals are also documented here.

## Loading Data

### `ldstr` - Load String
`ldstr "string"`

Takes one compile-time operand, the C-escape sytle string in double quotes to load to the evaluation stack. The native standard library MUST be loaded for this opcode to be compiled. Pushes a `[System]String` instance to the evaluation stack holding the specified value.

NOTE: `ldstr` is not compiled to assembly which generates a string when the program is run, rather, when the JIT compiler encounters the ldstr opcode, it generates the `[System]String` object during compilation. When the program is run, the pointer to the `[System]String` object is pushed to the stack.

This also means the string could be garbage collected accidentally between method calls and a method could reference an invalid object on a subsequent call. This is a known bug with `ldstr` and is currently being fixed.

### `ldfld` - Load Field
`ldfld {static|instance} <name>`

Takes two compile time operands, the first of which can either be `static` or `instance`, specifying the storage type of the field. The next operand is the field name. If the field is static, the name given should be the fully-qualified name to the field in ULR notation, such as `[System]String.Empty`. If the field is instance, the name given should just be the name of the field. For example, to access `A.B`, just give the name `B`. The last object on the evaluation stack will be popped off, assumed to be of type `A`, and the value of field `B` will be retrieved.

The value retrieved for a field is pushed to the evaluation stack.

### `ldloc` - Load Local
`ldloc <num>`

Loads a local of the current method and pushes its value to the evaluation stack. Takes one compile-time operand, which is the number of the local. Local numbers are automatically assigned from 0-255 in the order that local variables were declared in for the function.

### `ldapl` - Load Argument-Passed Local
`ldapl <num>`

Loads an argument-passed local (a function argument) of the current method and pushes its value to the evaluation stack. Takes one compile-time operand, which is the number of the argument-passed local. Argument-passed local numbers are automatically assigned in the same way as normal local numbers, ranging from 0-255 in the order that the arguments were declared in for the function.

### `ldelem` - Load Element
`ldelem <elem_type>`

Takes a compile-time operand of the array element type. Pops the last value off of the evaluation stack, reading it as a 32-bit integer. Pops the next value to the evaluation stack, assuming it is an array of `elem_type`, e.g. a `elem_type[]`. The array is indexed with the integer value popped off of the stack and the result of the indexing operation (the desired array element) is pushed to the stack.

### `ldito` - Load Internal Type Object
`ldito <type_name>`

Takes the type name of the type that should be loaded and pushes the desired type object to the stack. Note that this object is **not** a `[System.Reflection]Type` object, rather, it is the pointer to the C++ type object. To laod the `[System.Reflection]Type` equivalent, see [`ldeto`](#ldeto---load-external-type-object).

### `ldeto` - Load External Type Object
`ldeto <type_name>`

Takes the type name of the type that should be loaded and pushes the desired type object to the stack. The type object pushed to the stack is of type `[System.Reflection]Type`.

May never be implemented.

### `box` - Box Value Type
`box <type_name>`

Pops the last value off of the evaluation stack as a `type_name` and boxes it, pushing the boxed `[System]Object` version to the stack.

### `unbox` - Unbox Value Type
`unbox <type_name>`

Pops the last value off the evaluation stack as a reference object and unboxes it to recieve an object of `type_name`, pushing the `type_name` instance to the stack.

### `stfld` - Store Field
`stfld {static|instance} <name>`

Takes two compile time operands, the first of which can either be `static` or `instance`, specifying the storage type of the field. The next operand is the field name. If the field is static, the name given should be the fully-qualified name to the field in ULR notation, such as `[System]String.Empty`. The last value on the evaluation stack will be popped off and stored in the specified field destination. If the field is instance, the name given should just be the name of the field. For example, to store `A.B`, just give the name `B`. The last object on the evaluation stack will be popped off, assumed to be of type `A`, and the next value on the stack will be stored in that object's `B` field.

### `stelem` - Store Element
`stelem <elem_type>`

Takes a compile-time operand of the array element type. Pops the last value off of the evaluation stack, reading it as a 32-bit integer (the array index). Pops the next value to the evaluation stack, assuming it is an array of `elem_type`, e.g. a `elem_type[]`. The array is indexed with the aforementioned integer value and the next value on the evaluation stack is stored at that index location.

### `new` - Create New Object
`new <object_type>(<ctor_arg1_type>, <ctor_arg2_type>, ...)`

Create a new object of type `object_type` using the constructor with the specified signature. Arguments are popped in reverse order off of ths stack and after the constructor has initialized the object, the newly created object is pushed to the evaluation stack.

### `newarr` - Create New Array
`newarr <elem_type>`

Creates a new array of `elem_type`, e.g. an `elem_type[]`. The desired length of the array is popped off of the evaluation stack as a 32-bit integer. Once a new array is created with this element type and length, the array's reference is pushed to the evaluation stack.