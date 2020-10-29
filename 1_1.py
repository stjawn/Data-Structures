
def find_mismatch(text):
    opening_brackets_stack = []
    pos_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            pos_stack.append(i)
            pass
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            top = opening_brackets_stack.pop()
            pos = pos_stack.pop()
            if (top == '(' and next != ')') or (top == '[' and next != ']') or (top == '{' and next != '}'):
                return i + 1
            pass
    if len(pos_stack) != 0:
        return pos_stack[0] + 1
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
