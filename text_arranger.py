def main(text):
    text = text.split()
    return '_'.join(text) + '.py'

if __name__ == '__main__':
    text = input().strip()
    result = main(text)
    with open(result, 'w') as file:
        file.writelines(['from typing import *'])
    print(result)