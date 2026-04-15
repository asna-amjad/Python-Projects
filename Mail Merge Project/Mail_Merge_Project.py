# TODO: Create a letter using starting_letter.docx for each name in invited_names.txt

with open("./Input/Names/invited_names.txt") as invited_names:
    name_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()

    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
