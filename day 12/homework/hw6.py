read_pages = int(input("რამდენი გვერდი წაიკითხე: "))
free_time = bool(input("გქონდა თავისუფალი დრო? (true/false): "))
productive = read_pages >= 20 and free_time
print(productive)