def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        # Reverse the direction if top or bottom is reached
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        # Move up or down
        current_row += 1 if going_down else -1

    return ''.join(rows)
