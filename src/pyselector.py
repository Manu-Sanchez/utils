import os
import sys
import time
import keyboard

RESET = '\033[0m'

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'

idx = 0
filter_term = ""
aux_choice_list = []

def _show(question, choice_list, color, idx, filter_term, window_size = 10):

    os.system("cls")

    if filter_term:
        print(f"Filtering By: {filter_term}")

    if choice_list: 
        window_side_size = int(window_size/2)

        window_prev_side_idx = idx - window_side_size
        if window_prev_side_idx < 0:
           
            window_side_size = window_side_size + (window_side_size - idx)
            window_prev_side_idx = 0

        window_next_side_idx = idx + window_side_size
        if window_next_side_idx > len(choice_list):
            window_next_side_idx = len(choice_list) 

        print(f"{YELLOW}{question}:{RESET} {choice_list[idx]}")
        
        aux_choice_list = choice_list.copy()

        if color: aux_choice_list[idx] = f"{color}> {aux_choice_list[idx]}{RESET}"
        print("\n".join(aux_choice_list[window_prev_side_idx:window_next_side_idx]))

    else:
        print(f"{YELLOW}{question}:{RESET}")




def keyboard_interaction(event, question, choice_list, allow_filter, case_sensitive, carrousel, color):
    
    global filter_term, idx , aux_choice_list

    aux_choice_list = choice_list.copy()
    
    #Update the filter
    if allow_filter:
        if event.name == "backspace":
            filter_term = filter_term[:-1]

        elif len(event.name) == 1:
            filter_term += event.name


        if filter_term:
            filtered_choice_list = []
            for choice in aux_choice_list:
                if not case_sensitive:
                    if filter_term.lower() in choice.lower():
                        filtered_choice_list.append(choice)

                else:
                    if filter_term in choice:
                        filtered_choice_list.append(choice)

            aux_choice_list = filtered_choice_list

            if idx > len(aux_choice_list) - 1:
                idx = len(aux_choice_list) - 1

    #Interaction
    if event.name == "flecha arriba":
        if idx - 1 < 0:
            if carrousel:
                idx = len(aux_choice_list) - 1

        else:
            idx -= 1

    elif event.name == "flecha abajo":
        if idx + 1 > len(aux_choice_list) - 1:
            if carrousel:
                idx = 0

        else:
            idx += 1

    if event.name != "enter":
        _show(
            question,
            aux_choice_list,
            color,
            idx,
            filter_term
        )

def show_choice_list(question, choice_list, allow_filter=False, case_sensitive=True, carrousel=False, color=None):

    global idx, filter_term, aux_choice_list

    idx = 0
    filter_term = ""
    choice_list = [str(choice) for choice in choice_list]

    _show(
        question,
        choice_list,
        color,
        idx,
        filter_term
    )

    keyboard.on_press(
        lambda event: keyboard_interaction(
            event,
            question,
            choice_list,
            allow_filter,
            case_sensitive,
            carrousel,
            color
        )
    )
    keyboard.wait("enter")
    keyboard.unhook_all()

    return aux_choice_list[idx]
    


    
if __name__ == "__main__":
    
    while True:
        res = show_choice_list(
            "Select an item",
            [
                "apple",
                "cheese",
                "orange",
                "milk",
                "water",
                "cola",
                "onion",
                "grapes",
                "lemon",
                "pineapple",
                "juice",
                "cucumber",
                "watermelon"
            ],
            color = RED,
            carrousel=True,
            allow_filter=True,
            case_sensitive=False
        )

        os.system("cls")
        print(f"You've selected: {res}")

        time.sleep(2)


