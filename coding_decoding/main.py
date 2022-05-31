alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def structure(text, shifts,namefn):
    answer = ""
    for i in text:
        index = alphabet.index(i)
        if namefn=='decoded':
            index -= shifts
        else:
            index += shifts
        answer += alphabet[index]    
    print(f"The {namefn} text is {answer}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if direction == "encode":
            structure(text,shift,'encoded')
        elif direction == "decode":
            structure(text,shift,'decoded')

        yn = input('Do you want to continue(y/n)').lower()
        if yn == 'n':
            break
    else:
        print("You enter wrong direction please try again..")
