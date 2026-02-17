from app.operations import Operations

HELP_TEXT = (
    "Commands:\n"
    "  add a b        -> adds a + b\n"
    "  subtract a b   -> subtracts a - b (shortcut: sub)\n"
    "  multiply a b   -> multiplies a * b (shortcut: mul)\n"
    "  divide a b     -> divides a / b (shortcut: div)\n"
    "  help           -> show this message\n"
    "  exit           -> quit the program\n"
)

SHORTCUT = {
    "sub": "subtract",
    "mul": "multiply",
    "div": "divide",
}

ERROR_MSG = "Invalid input. Please follow the format: <operation> <num1> <num2>"

def calculator():
    print("Welcome to the Calculator REPL! Type 'help' for commands, 'exit' to quit.")

    while True:
        user_input = input("> ").strip()

        if not user_input:
            continue

        cmd_parts = user_input.split()
        cmd = cmd_parts[0].lower()

        if cmd == "help":
            print(HELP_TEXT)
            continue

        if cmd in ("exit", "quit"):
            print("Exiting calculator...")
            break

        cmd = SHORTCUT.get(cmd, cmd)

        if len(cmd_parts) != 3:
            print(ERROR_MSG)
            continue

        try:
            a = float(cmd_parts[1])
            b = float(cmd_parts[2])

        except ValueError:
            print(ERROR_MSG)
            continue

        try:
            if cmd == "add":
                print(f"Result: {Operations.add(a, b)}")
            elif cmd == "subtract":
                print(f"Result: {Operations.subtract(a, b)}")
            elif cmd == "multiply":
                print(f"Result: {Operations.multiply(a, b)}")
            elif cmd == "divide":
                print(f"Result: {Operations.divide(a, b)}")
            else:
                print("Invalid operation. Type 'help' for a list of commands.")

        except ValueError as e:
            print(e)