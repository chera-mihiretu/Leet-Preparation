def main(text):
    text = text.split()
    return '_'.join(text) + '.py'

if __name__ == '__main__':
    text = input().strip()
    print(main(text))