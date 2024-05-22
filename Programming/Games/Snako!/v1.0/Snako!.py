#!/usr/bin/python3

#import important modules to make it
import curses # to initialize the window and make some graphics
import random # to make the food random

def main(screen):

    # hide the mouse cursor from the screen
    curses.curs_set(0)

    # to store values of max height->y and max width->x in the variables
    screen_h_y, screen_w_x = screen.getmaxyx()

    # to make a fullscreen window
    window = curses.newwin(screen_h_y, screen_w_x, 0, 0)

    # to receive from user his input from a keyboard
    window.keypad(1)
    window.nodelay(True)
    # to make an input very fast response
    # from user per 50 milliseconds
    window.timeout(50)

    # set coordinates y,x of snake's head in window
    snake_y = screen_h_y // 4
    snake_x = screen_w_x // 2

    # define snake's body [head, belly, tail]
    snake = [
        [snake_y, snake_x], #snake's head
        [snake_y, snake_x - 1], # snake's belly
        [snake_y, snake_x - 2] # snake's tail
    ]

    # to store snake's food in variable
    food = [screen_h_y // 2, screen_w_x // 2]

    # to display snake's food on the middle window
    window.addch(food[0], food[1], curses.ACS_DIAMOND)

    # set the default movement to right
    key = curses.KEY_RIGHT

    # to make an infinite loop and break this loop if the user exited
    while True:
        next_key = window.getch()
        key = key if next_key == -1 else next_key
    
        if key == 27: # when user press on ESCAPE Button exit the program
            break
            exit()

        # set new position for snake's head
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN and key != curses.KEY_UP:
            new_head[0] += 1
        elif key == curses.KEY_UP and key != curses.KEY_DOWN:
            new_head[0] -= 1
        elif key == curses.KEY_LEFT and key != curses.KEY_RIGHT:
            new_head[1] -= 1
        elif key == curses.KEY_RIGHT and key != curses.KEY_LEFT:
            new_head[1] += 1

        # Wrap around if the snake hits the border
        new_head[0] = new_head[0] % screen_h_y
        new_head[1] = new_head[1] % screen_w_x

        # set a new value for snake when eats the food
        snake.insert(0, new_head)

        if snake[0] == food:
            food = None

            while food is None:
                new_food = [
                    random.randint(2, screen_h_y - 2),
                    random.randint(2, screen_w_x - 2)
                ]
                food = new_food if new_food not in snake else None
            window.addch(food[0], food[1], curses.ACS_DIAMOND)

        else:
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')

        window.addch(snake[0][0], snake[0][1], curses.ACS_DIAMOND | curses.A_BOLD | curses.A_UNDERLINE)

curses.wrapper(main)