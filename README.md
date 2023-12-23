# Python Selector Utility

Utility used to display a choice list in the CLI and select an item.
This has implemented also a filtering functionality, but first let's explain how does it works.

## How Does It Works?
It's simply getting a list and printing it formated to seem like a choice list.
This is made by the _show function.

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

This receives the question we want to show, the list of choices, the color we want for highlighting the scope option,
the actual idx of the scope option, if we're filtering by a term to show to the user and how much options we want to show.

This last one is quite important, because it will depend of your cli window size, if you see that the results doesn't fit accordengly with 
your window size, please adjust this parameter.

#### Window Size = 20
![image](https://github.com/Manu-Sanchez/utils/assets/56635300/0e61065c-af3f-45c3-82d8-c2b08211fbe5)

As you can see I'm not able to see the question, the filter term and I'm loosing information.

#### Window Size = 5
![image](https://github.com/Manu-Sanchez/utils/assets/56635300/03f94e5d-6f79-4b2d-9516-54935e304606)

With an appropiate window size we can show all the information to the user, all the other items, will be displayed when the user scrolls down.

The users can interact with the arrow keys to scroll between the different items available in the choice list, this is handled by our two main functions
The main function: **show_choice_list** is aware of setting the keyboard handler function and wait till the 'enter' key is pressed.

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

By other hand the keyboard_interaction function is aware of listening the keys the user is pressing, for filtering and for scrolling.

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

Something that you can not and it's **HIGH IMPORTANT** is that you need to set the proper event.name keys to your system, in my case they are 'flecha abajo' for down key,
and 'flecha arriba' for the up key, so please adjust this one before using it.

Next, the filter it's very simpler and what it does is wait till the actual key pressed is a character (it has 1 of lenght), otherwise if the pressed key is the backspace, then it will remove the 
last character the user added to the filter.

This filter step is made before showing the results, so when setting any filter it will be automatically reflected in the choice list.

## Support
I love to share my developments with everyone, and I'll love also to continue and have more time to spend developing these utilities, so if you find it useful and you would like to receive new packages, updates, etc, you can support me with the following link: https://www.paypal.com/donate/?hosted_button_id=29SLPQEVYP9Y

Other way to support my job is to leave me a rating or a feedback, this will be also highly appretiated, I want to continue building things, growing and improving my ideas.

## License
This is an opensource branch
Take the code, and improve or update as you wish, I hope this can be useful as base for greather things :)


Thank You So Much <3
