import emoji

def main():
    user_input = input()
    emojized_text = emoji.emojize(user_input , language="alias")
    print(f"Output: {emojized_text}")

if __name__ == "__main__":
    main()
