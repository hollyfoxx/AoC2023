def get_lines(input: str):
    lines = input.split('\n')
    for line in lines:
        if not line.strip():
            continue

        yield line
