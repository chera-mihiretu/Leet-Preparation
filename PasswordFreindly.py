from typing import *
class UserAuth:
    def __init__(self):
        self.current_string=0
        self.P = 131
        self.MOD = pow(10, 9) + 7
        self.chars = {}
        for i in range(ord('a'), ord('z') + 1):
            self.chars[i]= 0
        for i in range(ord('A'), ord('Z') + 1):
            self.chars[i]= 0
        for i in range(ord('0'), ord('9') + 1):
            self.chars[i]= 0
        self.content = {}
        
    def setPassword(self, string):
        hashed = self.hashIt(string)

        self.current_string = hashed
        self.bruteForce(hashed)

       

    def bruteForce(self, number):
        back_up = (number * self.P) % self.MOD
        self.content = {}
        for i in self.chars:
            self.content[(back_up + i) % self.MOD] = 0

    def hashIt(self, string):
        count = 1
        answer = 0
        for i in string:
            answer += (pow(self.P, len(string) - count, self.MOD) * ord(i) ) % self.MOD
            count += 1
        # print(answer)
        return answer % self.MOD
    def authorize(self, number):
        number = int(number)
        
        if number == self.current_string:
            return 1
        if number in self.content:
            return 1
        return 0
def authEvents(events) -> List[int]:
    myAuth = UserAuth()
    pair = {'setPassword':myAuth.setPassword, 'authorize':myAuth.authorize}
    answer = []
    for command, param in events:
        run = pair[command](param)
        
        if run is not None:
            answer.append(run)
    
    return answer

if __name__ == '__main__':
    
    

    events_rows = int(input().strip())
    events_columns = int(input().strip())

    events = []

    for _ in range(events_rows):
        events.append(input().rstrip().split())

    result = authEvents(events)
    print(result)

