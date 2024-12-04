from typing import List, Optional


def process_file(
    filename: str,
    num_col: int = 1,
    split: bool = False,
    delim: Optional[str] = None
) -> List[List[str]]:
    """
    Processes a file line-by-line, either keeping lines as-is, splitting them by
    whitespace or a custom delimiter.
    If `num_col > 1`, processes the file into columns.
    
    :param filename: Path to the file to be processed.
    :param num_col: Number of columns to split the line into (if > 1).
    :param split: Whether to split the line into parts (True or False).
    :param delim: The delimiter to split on (default is whitespace).
    :return: A list of processed lines or columns.
    """
    lines = []
    with open(f"../aoc-inputs/2024/{filename}") as f:
        for line in f:
            line = line.strip()

            # Split the line if needed
            if split:
                # Split by delimiter or whitespace
                split_line = line.split(delim) if delim else line.split()
            else:
                split_line = [line]  # Keep the whole line intact
            
            # If num_col > 1, we process by columns
            if num_col > 1:
                # Ensure we have enough columns by padding with empty strings
                split_line = (
                    split_line[:num_col] + [''] * (num_col - len(split_line))
                )
                if len(lines) < num_col:
                    lines.extend([[] for _ in range(num_col - len(lines))])
                for i in range(num_col):
                    lines[i].append(split_line[i])
            else:
                # Otherwise, just add the line (or the split line) to the output
                lines.append(split_line[0])  # For single column, keep as a line
    
    return lines
