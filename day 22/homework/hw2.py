vegetables = ["კარტოფილი", "ბადრიჯანი", "პომიდორი", "ხახვი"]

unwanted_vegetables = ["ბადრიჯანი", "ხახვი"]

new_vegetables = ["გოგრა", "პომიდორი"]

for i, veg in enumerate(vegetables):
    if veg in unwanted_vegetables:
        vegetables[i] = new_vegetables.pop(0)

print(vegetables)