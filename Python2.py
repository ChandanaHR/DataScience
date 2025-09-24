| Operator | Description                   | Example (`a=10, b=3`) | Result     |
| -------- | ----------------------------- | --------------------- | ---------- |
| `+`      | Addition                      | `a + b`               | `13`       |
| `-`      | Subtraction                   | `a - b`               | `7`        |
| `*`      | Multiplication                | `a * b`               | `30`       |
| `/`      | Division (float result)       | `a / b`               | `3.333...` |
| `//`     | Floor Division (integer part) | `a // b`              | `3`        |
| `%`      | Modulus (remainder)           | `a % b`               | `1`        |
| `**`     | Exponentiation (power)        | `a ** b`              | `1000`     |


Comparison/Relational operators in python
| Operator | Description              | Example (`a=10, b=3`) | Result  |
| -------- | ------------------------ | --------------------- | ------- |
| `==`     | Equal to                 | `a == b`              | `False` |
| `!=`     | Not equal to             | `a != b`              | `True`  |
| `>`      | Greater than             | `a > b`               | `True`  |
| `<`      | Less than                | `a < b`               | `False` |
| `>=`     | Greater than or equal to | `a >= b`              | `True`  |
| `<=`     | Less than or equal to    | `a <= b`              | `False` |


Logical operators 
| Operator | Description                                          | Example (`a = True, b = False`) | Result  |
| -------- | ---------------------------------------------------- | ------------------------------- | ------- |
| `and`    | Returns `True` if **both** conditions are true       | `a and b`                       | `False` |
| `or`     | Returns `True` if **at least one** condition is true | `a or b`                        | `True`  |
| `not`    | Reverses the result (True → False, False → True)     | `not a`                         | `False` |


Bitwise operators
| Operator | Description                                            | Example                                 | Binary Operation          | Result |        |                    |      |
| -------- | ------------------------------------------------------ | --------------------------------------- | ------------------------- | ------ | ------ | ------------------ | ---- |
| `&`      | Bitwise AND → 1 if both bits are 1                     | `a & b`                                 | `1010 & 0100 = 0000 0100` | `4`    |        |                    |      |
| \`       | \`                                                     | Bitwise OR → 1 if at least one bit is 1 | \`a                       | b\`    | \`1010 | 0100 = 0000 1110\` | `14` |
| `^`      | Bitwise XOR → 1 if bits are different                  | `a ^ b`                                 | `1010 ^ 0100 = 0000 1010` | `14`   |        |                    |      |
| `~`      | Bitwise NOT → Inverts all bits (1→0, 0→1)              | `~a`                                    | `~1010 = -(a+1)`          | `-11`  |        |                    |      |
| `<<`     | Left Shift → Shifts bits left (adds zeros at right)    | `a << 2`                                | `1010 << 2 = 101000`      | `40`   |        |                    |      |
| `>>`     | Right Shift → Shifts bits right (drops rightmost bits) | `a >> 2`                                | `1010 >> 2 = 0010`        | `2`    |        |                    |      |


Identity operators
| Operator | Description                                                               | Example      | Result           |
| -------- | ------------------------------------------------------------------------- | ------------ | ---------------- |
| `is`     | Returns `True` if both variables **refer to the same object** in memory   | `a is b`     | `True` / `False` |
| `is not` | Returns `True` if both variables **refer to different objects** in memory | `a is not b` | `True` / `False` |
Example1:            a = 5
            b = 5
            print(a is b)      # True (small integers are cached in memory)
            print(a is not b)  # False
== → compares values.
is → compares memory location (identity).


Membership operators in python
These are used to test whether a value is present in a sequence (string, list, tuple, set, dict, etc.).
| Operator | Description                                                  | Example              | Result |
| -------- | ------------------------------------------------------------ | -------------------- | ------ |
| `in`     | Returns `True` if the value is **found** in the sequence     | `"a" in "apple"`     | `True` |
| `not in` | Returns `True` if the value is **not found** in the sequence | `"x" not in "apple"` | `True` |
                # String example
                text = "python"
                print("p" in text)        # True
                print("z" not in text)    # True
                
                # List example
                fruits = ["apple", "banana", "mango"]
                print("apple" in fruits)      # True
                print("grape" not in fruits)  # True
                
                # Tuple example
                numbers = (1, 2, 3, 4)
                print(2 in numbers)       # True
                print(5 not in numbers)   # True
                
                # Set example
                colors = {"red", "blue", "green"}
                print("red" in colors)        # True
                print("yellow" not in colors) # True
                
                # Dictionary example (checks only keys by default)
                student = {"name": "Chandana", "age": 22}
                print("name" in student)         # True
                print("Chandana" in student)     # False (checks keys, not values)
                print("Chandana" in student.values())  # True



Assignment operators
| Operator | Description                    | Example (`a = 10`)    | Equivalent To | Result           |         |     |                  |
| -------- | ------------------------------ | --------------------- | ------------- | ---------------- | ------- | --- | ---------------- |
| `=`      | Assigns value                  | `a = 10`              | –             | `a = 10`         |         |     |                  |
| `+=`     | Add and assign                 | `a += 5`              | `a = a + 5`   | `15`             |         |     |                  |
| `-=`     | Subtract and assign            | `a -= 3`              | `a = a - 3`   | `7`              |         |     |                  |
| `*=`     | Multiply and assign            | `a *= 2`              | `a = a * 2`   | `20`             |         |     |                  |
| `/=`     | Divide and assign              | `a /= 2`              | `a = a / 2`   | `5.0`            |         |     |                  |
| `//=`    | Floor divide and assign        | `a //= 3`             | `a = a // 3`  | `3`              |         |     |                  |
| `%=`     | Modulus and assign             | `a %= 4`              | `a = a % 4`   | `2`              |         |     |                  |
| `**=`    | Exponent and assign            | `a **= 3`             | `a = a ** 3`  | `1000`           |         |     |                  |
| `&=`     | Bitwise AND and assign         | `a &= 2`              | `a = a & 2`   | Depends on value |         |     |                  |
| \`       | =\`                            | Bitwise OR and assign | \`a           | = 2\`            | \`a = a | 2\` | Depends on value |
| `^=`     | Bitwise XOR and assign         | `a ^= 2`              | `a = a ^ 2`   | Depends on value |         |     |                  |
| `>>=`    | Bitwise right shift and assign | `a >>= 1`             | `a = a >> 1`  | Shifts bits      |         |     |                  |
| `<<=`    | Bitwise left shift and assign  | `a <<= 1`             | `a = a << 1`  | Shifts bits      |         |     |                  |

