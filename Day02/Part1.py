def is_invalid_id(n):
    """Check if a number is made of a sequence of digits repeated twice."""
    s = str(n)
    length = len(s)
    
    # Must have even length to be a repeated pattern
    if length % 2 != 0:
        return False
    
    half = length // 2
    # Check if first half equals second half
    return s[:half] == s[half:]


def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs in a given range."""
    invalid_ids = []
    
    # Instead of iterating through all numbers, we can generate candidates
    # by looking for repeated patterns that fall within the range
    
    # Determine the digit lengths we need to consider
    min_digits = len(str(start))
    max_digits = len(str(end))
    
    # For each even digit length, generate all possible repeated patterns
    for total_digits in range(2, max_digits + 1, 2):  # Only even lengths
        half_digits = total_digits // 2
        
        # The pattern must have half_digits digits (no leading zeros)
        pattern_start = 10 ** (half_digits - 1) if half_digits > 1 else 1
        pattern_end = 10 ** half_digits - 1
        
        for pattern in range(pattern_start, pattern_end + 1):
            # Create the invalid ID by repeating the pattern
            pattern_str = str(pattern)
            invalid_id = int(pattern_str + pattern_str)
            
            # Check if it falls within our range
            if start <= invalid_id <= end:
                invalid_ids.append(invalid_id)
    
    return invalid_ids


def solve(input_text):
    """Solve the puzzle."""
    # Parse the input - ranges separated by commas
    ranges_str = input_text.strip()
    ranges = ranges_str.split(',')
    
    total = 0
    
    for range_str in ranges:
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        invalid_ids = find_invalid_ids_in_range(start, end)
        total += sum(invalid_ids)
    
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_text = f.read()
    
    result = solve(input_text)
    print(f"Sum of all invalid IDs: {result}")
