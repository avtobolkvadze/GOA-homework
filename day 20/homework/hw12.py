colors = ["თეთრი", "შავი", "ნარინჯისფერი", "ვარდისფერი"]

index = int(input("Enter the index (0 to 3): "))
new_color = input("Enter the new color: ")

if 0 <= index < len(colors):
    colors[index] = new_color  
    print("Updated list of colors:", colors)
else:
    print("Invalid index! Please enter an index between 0 and 3.")