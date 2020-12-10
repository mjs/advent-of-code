import sys


def run(program):
    ip = 0
    acc = 0
    length = len(program)

    repeat = [False] * length

    while True:
        if repeat[ip]:
            return acc, False
        repeat[ip] = True

        op, arg = program[ip]
        if op == "nop":
            ip += 1
        elif op == "acc":
            acc += arg
            ip += 1
        elif op == "jmp":
            ip += arg
        else:
            ValueError(f"unknown op: {op}")

        if ip == length:
            # normal termination, hooray
            return acc, True
        if ip > length:
            # jumped past the end
            return None, False


def parse_instruction(raw):
    op, arg = raw.strip().split(" ", 1)
    return op, int(arg)


def fix(program):
    for i, (op, arg) in enumerate(program):
        new_op = swap_op(op)
        if new_op:
            new_program = program.copy()
            new_program[i] = (new_op, arg)
            acc, terminated = run(new_program)
            if terminated:
                return acc
    raise ValueError("couldn't fix")


def swap_op(op):
    if op == "nop":
        return "jmp"
    if op == "jmp":
        return "nop"
    return None


def main():
    program = [parse_instruction(x) for x in sys.stdin]
    print("part 1:", run(program)[0])
    print("part 2:", fix(program))


if __name__ == "__main__":
    main()
