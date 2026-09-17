def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    total_true_count = 0
    total_love_count = 0
    print(combined_name)
    for letter in "true":
        count_true = combined_name.lower().count(letter)
        total_true_count = total_true_count + count_true
    for letter in "love":
        count_love = combined_name.lower().count(letter)
        total_love_count = total_love_count + count_love
    print(f"{total_true_count}{total_love_count}")



calculate_love_score("Kanye West", "Kim Kardashian")