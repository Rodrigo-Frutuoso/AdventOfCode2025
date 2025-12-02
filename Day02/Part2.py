def is_invalid_id(n):
    """Check if a number is made of a sequence of digits repeated at least twice."""
    s = str(n)
    length = len(s)
    
    for pattern_len in range(1, length // 2 + 1):
        if length % pattern_len != 0:
            continue
        
        repetitions = length // pattern_len
        if repetitions < 2:
            continue
        
        pattern = s[:pattern_len]
        
        if pattern[0] == '0':
            continue
        
        if pattern * repetitions == s:
            return True
    
    return False


def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs in a given range by generating candidates."""
    invalid_ids = set()
    
    max_digits = len(str(end))
    
    for total_digits in range(1, max_digits + 1):
        for pattern_len in range(1, total_digits // 2 + 1):
            if total_digits % pattern_len != 0:
                continue
            
            repetitions = total_digits // pattern_len
            if repetitions < 2:
                continue
            
            pattern_start = 10 ** (pattern_len - 1) if pattern_len > 1 else 1
            pattern_end = 10 ** pattern_len - 1
            
            for pattern in range(pattern_start, pattern_end + 1):
                pattern_str = str(pattern)
                invalid_id = int(pattern_str * repetitions)
                
                if start <= invalid_id <= end:
                    invalid_ids.add(invalid_id)
    
    return invalid_ids


def solve(input_text):
    """Solve the puzzle."""
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
