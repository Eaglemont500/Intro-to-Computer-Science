## Function: Block of reusable code that runs when called
## Syntax: Define with def name(): and indent body underneath; Call with name()
## Arguments vs Parameters: Arguments are values passed in when calling; Parameters are variables in the definition receiving them
## Order and Count: Number and Order of arguments must match parameters
## Return: Ends function and sends a value back to the caller

## Recursion: Function calling itself to break a problem into smaller steps
## Base Condition: Stop condition (like if n == 0: return) to prevent infinite recursion
## Call Stack: Each call adds a frame and resolves top-down after base condition; Too deep gives RecursionError
## Recursion vs Iteration: Loops are usually faster and avoid stack depth limits; Recursion can be cleaner for things like factorials or trees/algorithms