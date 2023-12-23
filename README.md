#Python Selector Utility

Utility used to display a choice list in the CLI and select an item.
This has implemented also a filtering functionality, but first let's explain how does it works.

##How Does It Works?
It's simply getting a list and printing it formated to seem like a choice list.
This is made by the _show function.

´´´
def _show(question, choice_list, color, idx, filter_term, window_size = 10):

    os.system("cls")
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
´´´

This receives the question we want to show, the list of choices and