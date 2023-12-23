import os
import keyboard

RESET = '\033[0m'

ROJO = '\033[91m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'

idx = 0
filter_term = ""

def _show(question, choice_list, color, idx, filter_term):

    os.system("cls")
    print(f"Filtering By: {filter_term}")

    if choice_list: 
        print(f"{AMARILLO}{question}:{RESET} {choice_list[idx]}")
        
        aux_choice_list = choice_list.copy()

        if color: aux_choice_list[idx] = f"{color}> {aux_choice_list[idx]}{RESET}"
        print("\n".join(aux_choice_list))

    else:
        print(f"{AMARILLO}{question}:{RESET}")




def keyboard_interaction(event, question, choice_list, carrousel, color):
    
    global filter_term, idx 

    aux_choice_list = choice_list.copy()
    
    #Update the filter
    if event.name == "backspace":
        filter_term = filter_term[:-1]

    elif len(event.name) == 1:
        filter_term += event.name


    if filter_term:
        filtered_choice_list = []
        for choice in aux_choice_list:
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


    _show(
        question,
        aux_choice_list,
        color,
        idx,
        filter_term
    )



def show_choice_list( question, choice_list, carrousel=0, color=None):

    global idx, filter_term

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
            carrousel,
            color
        )
    )
    keyboard.wait("enter")
    
if __name__ == "__main__":
    print(show_choice_list(
        "Select an item",
        [
            0,1,2,3,4,5
        ],
        color = ROJO
    ))



    
