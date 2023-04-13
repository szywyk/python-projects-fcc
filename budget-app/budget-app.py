class Category:

    def __init__(self, n):
        self.name = n
        self.ledger = []

    def __str__(self):
        string_to_return = ""
        asterisk_num = 30 - len(self.name)
        if asterisk_num % 2 == 0:
            asterisk_left = int(asterisk_num / 2)
            asterisk_right = asterisk_left
        else:
            asterisk_left = int(asterisk_num / 2)
            asterisk_right = int(asterisk_num - asterisk_left)
        ast_left = "*" * asterisk_left
        ast_right = "*" * asterisk_right
        string_to_return = string_to_return + ast_left + self.name + ast_right + "\n"
        for record in self.ledger:
            if len(record["description"]) > 23:
                desc_len = 23
            else:
                desc_len = len(record["description"])
            amount_string = "%.2f" % record["amount"]
            if len(amount_string) > 7:
                amount_len = 7
            else:
                amount_len = len(amount_string)
            spaces_num = 30 - desc_len - amount_len
            string_to_return = string_to_return + record["description"][
                0:23] + " " * spaces_num + amount_string[0:7] + "\n"
        total = self.get_balance()
        string_to_return = string_to_return + "Total: " + "%.2f" % total
        return string_to_return

    def deposit(self, amount, *args):
        description = ""
        if len(args) > 0:
            description = args[0]
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, *args):
        description = ""
        if len(args) > 0:
            description = args[0]
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0.0
        for record in self.ledger:
            balance = balance + record["amount"]
        return balance

    def transfer(self, amount, category):
        destination = "Transfer to " + category.name
        source = "Transfer from " + self.name
        if self.check_funds(amount):
            self.withdraw(amount, destination)
            category.deposit(amount, source)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    output = "Percentage spent by category\n100| "
    withdrawal_sums = []
    dots_nums = []
    overall = 0
    names = []

    for category in categories:
        names.append(category.name)
        withdrawal_sum = 0
        for record in category.ledger:
            if record["amount"] < 0:
                withdrawal_sum = withdrawal_sum - record["amount"]
        withdrawal_sums.append(withdrawal_sum)

    for value in withdrawal_sums:
        overall = overall + value

    for value in withdrawal_sums:
        percent = (value * 100) / overall
        if percent < 10:
            dots_nums.append(1)
        elif percent < 20:
            dots_nums.append(2)
        elif percent < 30:
            dots_nums.append(3)
        elif percent < 40:
            dots_nums.append(4)
        elif percent < 50:
            dots_nums.append(5)
        elif percent < 60:
            dots_nums.append(6)
        elif percent < 70:
            dots_nums.append(7)
        elif percent < 80:
            dots_nums.append(8)
        elif percent < 90:
            dots_nums.append(9)
        elif percent < 100:
            dots_nums.append(10)
        else:
            dots_nums.append(11)

    n = 90
    for i in range(11, 0, -1):
        if n > 0:
            for dots in dots_nums:
                if dots >= i:
                    output = output + "o" + " " * 2
                else:
                    output = output + " " * 3
            output = output + "\n " + str(n) + "| "
            n = n - 10
        elif n == 0:
            for dots in dots_nums:
                if dots >= i:
                    output = output + "o" + " " * 2
                else:
                    output = output + " " * 3
            output = output + "\n" + " " * 2 + str(n) + "| "
            n = n - 10
        else:
            for dots in dots_nums:
                if dots >= i:
                    output = output + "o" + " " * 2
                else:
                    output = output + " " * 3
            output = output + "\n" + " " * 4 + "-"
            for dots in dots_nums:
                output = output + "---"

    longest_name = 0
    for name in names:
        if len(name) > longest_name:
            longest_name = len(name)

    for i in range(longest_name):
        output = output + "\n" + " " * 5
        for name in names:
            if i < len(name):
                output = output + name[i] + " " * 2
            else:
                output = output + " " * 3

    return output
