# list can change but tuple cannot change 
# list is mutable but tuple is immutable
# list uses [] but tuple uses ()

tea_varieties = ("black", "green", "oolong", "white")
print(tea_varieties)
print(tea_varieties[0])
print(tea_varieties[-1])    
#tea_varieties[3] = "herbal" # it will give error because tuple is immutable
print(len(tea_varieties)) # it will give total number of items in tuple

more_tea = ("masala", "chamomile")
all_teas = tea_varieties + more_tea # concatenation of tuples
print(all_teas)

if "green" in tea_varieties:    
    print("Green tea is available")

print(more_tea.count("chamomile")) # it will count how many times chamomile is present in tuple
print(all_teas.index("oolong")) # it will give index of oolong in all

snacks = ("biscuits", "parantha")
print(snacks)
snacks = ("samosa", "pakora", "jalebi") 
print(snacks)# reassigning a new tuple to the same variable name it will give 2 different tuples


