class TextProcessor:
    def __init__(self, text):
        """Initialize the text processor with User input"""
        self.text = text

    def to_upper(self):
        return self.text.upper()

    def to_lower(self):
        return self.text.lower()

    def capitalize_text(self):
        return self.text.capitalize()

    def title_case(self):
        return self.text.title()

    def swap_case(self):
        return self.text.swapcase()

    def reverse_text(self):
        return self.text[::-1]

    def remove_space(self):
        return self.text.strip()

    def count_occurrences(self, sub_string):
        return self.text.count(sub_string)

    def replace_text(self, old, new):
        return self.text.replace(old, new)

    def check_if_digit(self):
        return self.text.isdigit()

    def check_if_alpha(self):
        return self.text.isalpha()

    def check_if_alnum(self):
        return self.text.isalnum()

    def split_text(self, separator=' '):
        return self.text.split(separator)

    def join_text(self, word_list, separator=' '):
        return separator.join(word_list)

    def get_text(self):
        return self.text


def main():
    user_text = input("Enter your text: ")
    processor = TextProcessor(user_text)

    while True:
        print('\n TEXT PROCESSOR MENU')
        print('1. Convert to UPPERCASE')
        print('2. Convert to lowercase')
        print('3. Capitalize first letter')
        print('4. Capitalize Text')
        print('5. Swap case')
        print('6. Reverse Text')
        print('7. Remove Space')
        print('8. Count Substring Occurrences')
        print('9. Replace Text')
        print('10. Check if Digit')
        print('11. Check if Alphabetic')
        print('12. Check if Alphanumeric')
        print('13. Split Text')
        print('14. Join List into Text')
        print('15. Show Original Text')
        print('0. Exit')

        choice = int(input('Enter your choice (0-15):'))
        if choice == 0:
            print('Goodbye!')
            break

        elif choice == 1:
            print('Result:', processor.to_upper())

        elif choice == 2:
            print('Result:', processor.to_lower())

        elif choice == 3:
            print('Result:', processor.capitalize_text())

        elif choice == 4:
            print('Result:', processor.title_case())

        elif choice == 5:
            print('Result:', processor.swap_case())

        elif choice == 6:
            print('Result:', processor.reverse_text())

        elif choice == 7:
            print('Result:', processor.remove_space())

        elif choice == 8:
            substring = input('Enter substring to count: ')
            print('Result:', processor.count_occurrences(substring))

        elif choice == 9:
            old = input('Enter old substring:')
            new = input('Enter new substring:')
            print('Result:', processor.replace_text(old, new))

        elif choice == 10:
            print('Is Digit?:', processor.check_if_digit())

        elif choice == 11:
            print('Is alphabetic?:', processor.check_if_alpha())

        elif choice == 12:
            print('Is alphanumeric?:', processor.check_if_alnum())

        elif choice == 13:
            sep = input('Enter separator: ')
            print('Result:', processor.split_text(sep))

        elif choice == 14:
            words = input('Enter words separated by space:').split()
            sep = input('Enter separator:') or ' '
            print('Result:', processor.join_text(words, sep))

        elif choice == 15:
            print('Original Text:', processor.get_text())

        else:
            print('Invalid choice. Please try again')


main()
