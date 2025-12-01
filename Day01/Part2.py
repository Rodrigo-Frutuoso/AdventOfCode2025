test_input = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

position = 50
zero_count = 0

for line in test_input:
    if line[0] in ("L", "R") and line[1:].isdigit():
        direction = line[0]
        distance = int(line[1:])
        
        old_pos = position
        times_hit = 0
        times_passed = 0
        
        if direction == "R":
            # Quantas vezes passamos pelo 0?
            times_passed = (position + distance) // 100
            zero_count += times_passed
            
            # Nova posição
            position = (position + distance) % 100
        
        else:
            # Movimento à esquerda
            new_position = (position - distance) % 100
            if new_position < 0:
                new_position += 100
            
            # Contar hits no zero ao ir para trás
            first_hit = position
            if first_hit == 0:
                first_hit = 100
            
            if first_hit <= distance:
                times_hit = ((distance - first_hit) // 100) + 1
                zero_count += times_hit
            
            position = new_position
        
        print(f"{line} : {old_pos} -> {position} (hits: {times_hit or times_passed})")

print(f"\nTotal zeroCount = {zero_count}")
