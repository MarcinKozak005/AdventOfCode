from sortedcontainers import SortedList # part2

data_file = open('01data.txt','r')

max_calories = 0
current_elf_calories_count = 0

sorted_elfs = SortedList() # part2


for line in data_file:
    if line == '\n':
        max_calories = max(max_calories, current_elf_calories_count)
        sorted_elfs.add(current_elf_calories_count) # part2
        current_elf_calories_count = 0
    else:
        current_elf_calories_count += int(line)
print(max_calories)
print(sum(sorted_elfs[-3:])) # part2

