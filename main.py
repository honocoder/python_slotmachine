import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# this is a dictionary
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



def deposit():
    while True:
        amount = input("Combien aimeriez-vous déposer? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Le montant doit être supérieur à 0.")
        else:
            print("Merci d'entrer un chiffre.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Sur combien de lignes souhaitez-vous voulez parier (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Entrez un nombre de lignes valide.")
        else:
            print("Merci d'entrer un chiffre.")

    return lines

def get_bet():
    while True:
        amount = input("Combien aimeriez-vous parier sur chaque ligne? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Le montant doit être entre {MIN_BET}€ et {MAX_BET}€.")
        else:
            print("Merci d'entrer un chiffre.")
        
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Vous n'avez pas assez d'argent pour parier cette somme. Votre solde est de {balance}€.")
        else:
            break

    print(f"Vous pariez {bet}€ sur {lines} lignes. Votre pari total est égal à {total_bet}€.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)


main()