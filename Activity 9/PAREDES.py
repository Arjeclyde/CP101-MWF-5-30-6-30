def word_bank():
    # List of words you don't want to be entered
    forbidden_words = ["apple", "banana", "cherry"]

    words = []
    
    while True:
        word = input("Enter a word: ")

        # Check if the word is in the forbidden list
        if word.lower() in forbidden_words:
            print("This word is not allowed. Try again.")
            continue
        
        words.append(word)

        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
        if try_again.lower() != 'y':
            break

    print(f"\nTotal number of words: {len(words)}")
    print("Words entered:", ", ".join(words))

word_bank()
