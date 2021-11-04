# Write your code here
import io
import os.path
import random
import sys


def add_cards(flash_cards):
    print_log('The card:')
    while True:
        card = input_log()
        if card in flash_cards.keys():
            print_log(f'The card "{card}" already exists. Try again:')
        else:
            break
    print_log(f"The definition for card:")
    while True:
        definition = input_log()
        if definition in [flash_cards[card]['def'] for card in flash_cards]:
            print_log(f'The definition "{definition}" already exists. Try again:')
        else:
            break
    print_log(f'The pair ("{card}":"{definition}") has been added.')
    flash_cards.update({card: {'def': definition, 'score': '0'}})

    return flash_cards


def check(flash_cards: dict):
    communicate = ''
    for term, definition in flash_cards.items():
        answer = input_log(f'Print the definition of "{term}":\n')
        if answer == definition:
            print_log("Correct!")
        else:
            communicate = (f'Wrong. The right answer is "{definition}"')
            if answer in flash_cards.values():
                defi = list(flash_cards.keys())[list(flash_cards.values()).index(answer)]
                list(flash_cards.keys())
                communicate += f'but your definition is correct for{defi}.'
            else:
                communicate += '.'
            print_log(communicate)


def export_cards(flash_cards,file_name=None):
    if file_name == None:
        print_log('File name:')
        file_name = input_log()
    with open(file_name, 'w') as f:
        counter = 0
        for term in flash_cards:
            f.write(f"{term}::{flash_cards[term]['def']}::{flash_cards[term]['score']}\n")
            counter += 1
        print_log(f"{counter} cards have been saved.")


def import_cards(flash_cards,file_name=None):
    if file_name == None:
        print_log('File name:')
        file_name = input_log()
    if os.path.isfile('./' + file_name):
        counter = 0  # ints counter
        with open(file_name, 'r') as f:
            for line in f.read().splitlines():
                term, definition, score = line.split('::')
                flash_cards.update({term: {'def': definition, 'score': int(score)}})
                counter += 1
        print_log(f'{counter} cards have been loaded.')
    else:
        print_log('File not found.')
        return False


def remove_card(flash_cards):
    print_log('Which card?')
    card = input_log()
    if card in flash_cards.keys():
        flash_cards.pop(card)
        print_log('The card has been removed.')
    else:
        print_log(f'Can\'t remove "{card}": there is no such card.')


def ask(flash_cards):
    if len(flash_cards) > 0:
        print_log('How many times to ask?')
        while True:
            no_of_cards = input_log()
            if no_of_cards.isdigit():
                no_of_cards = int(no_of_cards)
                break
        for i in range(no_of_cards):
            rand_choice = random.choice(list(flash_cards.keys()))
            print_log(f'Print the definition of "{rand_choice}":')
            answer = input_log()
            if answer == flash_cards[rand_choice]['def']:
                print_log("Correct!")
            else:
                correct = flash_cards[rand_choice]['def']
                flash_cards[rand_choice]['score'] = int(flash_cards[rand_choice]['score']) + 1
                communicate = (f'Wrong. The right answer is "{correct}"')
                if answer in [el['def'] for el in list(flash_cards.values())]:
                    index = [el['def'] for el in list(flash_cards.values())].index(answer)
                    defi = list(flash_cards.keys())[index]
                    communicate += f', but your definition is correct for {defi}.'
                else:
                    communicate += '.'
                print_log(communicate)


def hardest_card(flash_cards):
    if len(flash_cards) > 0:
        max_score = max([int(el['score']) for el in list(flash_cards.values())])
        if max_score > 0:
            hardest_cards = []
            for card in flash_cards:
                if flash_cards[card]['score'] == max_score:
                    hardest_cards.append(card)
            print_log(f"The hardest {'cards are ' if len(hardest_cards) > 1 else 'card is'} \"{','.join(hardest_cards)}\". "
                  f"You have {max_score} errors answering {'them' if len(hardest_cards) > 1 else 'it'}.")
        else:
            print_log('There are no cards with errors.')
    else:
        print_log('There are no cards with errors.')


def reset_stats(flash_cards):
    for card in flash_cards:
        flash_cards[card]['score'] = '0'
    print_log('Card statistics have been reset.')

def print_log(str):
    if str is not None:
        log_buffer.write(str+'\n')
        print(str)
def input_log():
    input_ = input()
    log_buffer.write('>>'+input_+'\n')
    return input_
def log():
    # TODO
    print_log('File name:')
    file_name = input_log()
    with open(file_name,'w') as f:
        f.write(log_buffer.getvalue())
        print_log('The log has been saved.')

def menu(flash_cards = {}):
    while True:
        actions = 'add, remove, import, export, ask, exit, log, hardest card, reset stats'
        print_log(f"Input the action ({actions}):")
        input_ = input_log()
        if input_ == 'add':
            add_cards(flash_cards)
        if input_ == 'remove':
            remove_card(flash_cards)
        if input_ == 'import':
            import_cards(flash_cards)
        if input_ == 'export':
            export_cards(flash_cards)
        if input_ == 'ask':
            ask(flash_cards)
        if input_ == 'exit':
            if save_on_exit:
                export_cards(flash_cards,save_on_exit)
            print('Bye bye!')

            break
        if input_ == 'log':
            log()
        if input_ == 'hardest card':
            hardest_card(flash_cards)
        if input_ == 'reset stats':
            reset_stats(flash_cards)
        if input_ == 'db':
            print(flash_cards)

if __name__ == "__main__":
    save_on_exit = False
    flash_cards = {}
    args = sys.argv
    log_buffer = io.StringIO()
    if len(args) > 1:
        args = args[1:]
        args_dict = {}
        for el in args:
            com, file_name = el.split('=')
            args_dict.update({com:file_name})
        if '--export_to' in args_dict.keys():
            save_on_exit = args_dict.get('--export_to')
        if '--import_from' in args_dict.keys():
            file_name = args_dict.get('--import_from')
            import_cards(flash_cards, file_name=file_name)
    menu(flash_cards)


# flash_cards = {'France': {'def': 'Paris', 'score': '2'}, 'Poland': {'def': 'Warsaw', 'score': '5'}, 'Ukraine': {'def': 'Kiev', 'score': '1'}, 'Russia': {'def': 'Moscow', 'score': '2'}, 'USA': {'def': 'DC', 'score': '2'}, 'Great Bretain': {'def': 'London', 'score': '6'}}
# add_cards(flash_cards)
# # print([flash_cards[card]['def'] for card in flash_cards])
