import emoji
while True:
    user_text = input("do you know python? ")
    if user_text == "stop":
        print("program was stopped")
        break

    if user_text == "yes":
        print(emoji.emojize('you are :thumbs_up:'))
    elif user_text == "no":
        print(emoji.emojize('you are :thumbs_down:'))
    else:
        print('you have to text only (yes, no)')