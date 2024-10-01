import random
from datetime import datetime
from colorama import Fore

class CC:
    '''Individual card info and methods.'''

    CCDATA = {
        'amex': {'len_num': 15, 'len_cvv': 4, 'pre': [34, 37], 'remaining': 13},
        'discover': {'len_num': 16, 'len_cvv': 3, 'pre': [6011, 64, 65], 'remaining': 12},
        'mc': {'len_num': 16, 'len_cvv': 3, 'pre': [51, 52, 53, 54, 55], 'remaining': 14},
        'visa13': {'len_num': 13, 'len_cvv': 3, 'pre': [4], 'remaining': 12},
        'visa16': {'len_num': 16, 'len_cvv': 3, 'pre': [4], 'remaining': 15},
    }

    def __init__(self, mm=None, yy=None):
        self.mm = mm
        self.yy = yy
        self.cc_type = None
        self.cc_num = None
        self.cc_cvv = None
        self.cc_exp = None
        self.cc_prefill = []

    def generate_cc_exp(self):
        '''Manually generate expiration date between next year and next three years.'''
        current_year = datetime.now().year
        exp_year = random.randint(current_year + 1, current_year + 3)  # Between next year and next three years
        exp_month = random.randint(1, 12)  # Random month between 1 and 12
        self.cc_exp = f"{exp_month:02d}-{exp_year}"  # Format as mm-YYYY

    def generate_cc_cvv(self):
        length = self.CCDATA[self.cc_type]['len_cvv']
        self.cc_cvv = ''.join(str(random.randint(0, 9)) for _ in range(length))

    def generate_cc_prefill(self):
        self.cc_prefill = random.choices(self.CCDATA[self.cc_type]['pre'])

    def generate_cc_num(self):
        remaining = self.CCDATA[self.cc_type]['remaining']
        working = self.cc_prefill + [random.randint(1, 9) for _ in range(remaining - 1)]
        check_offset = (len(working) + 1) % 2
        check_sum = 0

        for i, n in enumerate(working):
            if (i + check_offset) % 2 == 0:
                n_ = n * 2
                check_sum += n_ - 9 if n_ > 9 else n_
            else:
                check_sum += n

        temp = working + [10 - (check_sum % 10)]
        self.cc_num = "".join(map(str, temp))

    def print_new_card(self):
        exp_month, exp_year = self.cc_exp.split('-')
        print("-----------------------------------------------------")

        if self.is_valid():
            validity_message = "Card number is valid."
            str_to_save = f'{self.cc_num}|{exp_month}|{exp_year}|{self.cc_cvv}'
            with open('validCc.txt','a') as f:
                f.write(str_to_save)
                f.write('\n')
        else:
            validity_message = "Card number is not valid."

        validity_color = Fore.GREEN if self.is_valid() else Fore.RED
        print(f'\nType: {self.cc_type}\nCard: {self.cc_num}|{exp_month}|{exp_year}|{self.cc_cvv}\n{validity_color}{validity_message}{Fore.RESET}\n\n')
        print("-----------------------------------------------------")

    def is_valid(self):
        working = [int(d) for d in self.cc_num]
        check_offset = (len(working) + 1) % 2
        check_sum = 0

        for i, n in enumerate(working):
            if (i + check_offset) % 2 == 0:
                n_ = n * 2
                check_sum += n_ - 9 if n_ > 9 else n_
            else:
                check_sum += n

        return check_sum % 10 == 0

def check_card(card_num, mm, yy):
    cc = CC(mm, yy)
    cc.cc_num = card_num

    for card_type, data in cc.CCDATA.items():
        for pre in data['pre']:
            if card_num.startswith(str(pre)):
                cc.cc_type = card_type
                break
        else:
            continue
        break
    else:
        print("Card type not recognized.")
        return

    cc.generate_cc_exp()
    cc.generate_cc_cvv()
    cc.print_new_card()

def begin():
    with open('allcc.txt', 'r') as file:
        for line in file:
            user_input = line.strip()
            ccn, mm, yy, cvc = user_input.split('|')
            check_card(ccn, mm, yy)

begin()
