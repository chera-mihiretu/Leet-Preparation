from typing import *


class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
    def __str__(self):
        return f'{self.name},{self.time},{self.amount},{self.city}'
    def formatted(self):
        return f'{self.name},{self.time},{self.amount},{self.city}'
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_class = []
        transactions_hash = defaultdict(lambda: defaultdict(set))
        for tr in transactions:
            value = Transaction(*tr.split(','))
            transactions_class.append(value)
            transactions_hash[value.name][value.time].add(value.city)

        result = []
        for i in transactions_class:
            if i.amount > 1000:
                result.append(i.formatted()) 
                continue
            for time_range in range(i.time - 60, i.time + 61):
                if time_range in transactions_hash[i.name]:
                    if len(transactions_hash[i.name][time_range]) > 1 or i.city not in transactions_hash[i.name][time_range]:
                        result.append(i.formatted())
                        break
        return result
