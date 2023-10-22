
digit_count = 0

with open("mydefaults.ini.txt") as ini_file:
    letters = ini_file.read()
    print(letters)
    print("Number of letters:", len(letters))
    for line in ini_file:
        for char in ini_file:
            if char.isdigit():
                digit_count += 1
print("Number of Digits:",digit_count)
    
    

    

    