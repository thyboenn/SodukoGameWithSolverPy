import pygame
import time

# initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((640, 480))

# title and icon
pygame.display.set_caption("Sudoku")

# boards
b1 = [
    [5, 0, 3, 0, 0, 0, 9, 0, 6],
    [0, 6, 9, 0, 0, 0, 7, 2, 0],
    [7, 2, 0, 0, 0, 0, 0, 5, 4],
    [0, 0, 0, 3, 2, 5, 0, 0, 0],
    [0, 0, 0, 4, 0, 7, 0, 0, 0],
    [0, 0, 0, 1, 8, 9, 0, 0, 0],
    [4, 5, 0, 0, 0, 0, 0, 7, 1],
    [0, 7, 1, 0, 0, 0, 4, 3, 0],
    [3, 0, 2, 0, 0, 0, 5, 0, 8],
]

b2 = [
    [0, 5, 4, 0, 0, 0, 1, 7, 0],
    [8, 2, 0, 1, 0, 7, 0, 3, 6],
    [3, 0, 0, 0, 0, 0, 0, 0, 9],
    [0, 4, 0, 0, 8, 0, 0, 1, 0],
    [0, 0, 0, 3, 0, 5, 0, 0, 0],
    [0, 3, 0, 0, 6, 0, 0, 2, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 6, 0, 2, 0, 8, 0, 5, 7],
    [0, 8, 7, 0, 0, 0, 9, 6, 0],
]

b3 = [
    [1, 0, 6, 2, 0, 8, 9, 0, 4],
    [0, 5, 0, 0, 0, 0, 0, 8, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 7],
    [5, 0, 0, 0, 8, 0, 0, 0, 9],
    [0, 0, 0, 3, 2, 1, 0, 0, 0],
    [6, 0, 0, 0, 7, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 4, 0, 0, 0, 0, 0, 9, 0],
    [8, 0, 1, 9, 0, 6, 7, 0, 2],
]

boardlist = [b1, b2, b3]

### - variables: - #########
game_state = 0  # game state. 0 is off. 1 is on.

# draw board
draw_board_color = (0, 0, 0)

# mistakes variables
mistake_x = 90
mistake_y = 375
mistake_font = pygame.font.Font("freesansbold.ttf", 32)
mistake_value = 0

# time variables
time_x = 90
time_y = 435
time_font = pygame.font.Font("freesansbold.ttf", 32)
start_time = time.time()

# start button variables
start_button_x = 363
start_button_y = 4
start_button_w = 274
start_button_h = 72
start_button_font = pygame.font.Font("freesansbold.ttf", 28)
start_text = start_button_font.render("Start", True, (0, 0, 0))
start_text_x = 455
start_text_y = 30

# board select variables
## text
board_sel_x = 410
board_sel_y = 90
board_sel_font = pygame.font.Font("freesansbold.ttf", 28)

## counter
board_sel_count_x = 605
board_sel_count_y = 110
board_sel_count_font = pygame.font.Font("freesansbold.ttf", 13)
board_sel_count_value = 1

## go up
board_sel_up_x = 499
board_sel_up_y = 126
board_sel_up_w = 137
board_sel_up_h = 60
board_sel_up_font = pygame.font.Font("freesansbold.ttf", 28)
board_sel_up_text = start_button_font.render("=>", True, (0, 0, 0))
board_sel_up_text_x = 550
board_sel_up_text_y = 140

## go down
board_sel_down_x = 363
board_sel_down_y = 126
board_sel_down_w = 135
board_sel_down_h = 60
board_sel_down_font = pygame.font.Font("freesansbold.ttf", 28)
board_sel_down_text = start_button_font.render("<=", True, (0, 0, 0))
board_sel_down_text_x = 410
board_sel_down_text_y = 140

#  Solve button variables
solve_button_x = 363
solve_button_y = 190
solve_button_w = 274
solve_button_h = 72
solve_button_font = pygame.font.Font("freesansbold.ttf", 28)
solve_text = start_button_font.render("Solve", True, (0, 0, 0))
solve_text_x = 455
solve_text_y = 213
solve_value = 0

# show control
show_control_x = 435
show_control_y = 283
show_control_font = pygame.font.Font("freesansbold.ttf", 28)

show_control_text_font = pygame.font.Font("freesansbold.ttf", 16)

show_control_text_1_x = 380
show_control_text_1_y = 350
show_control_text_1 = "Mouseclick to select a box."

show_control_text_2_x = 380
show_control_text_2_y = 380
show_control_text_2 = "Number 1-9 to fill in the box."

show_control_text_3_x = 380
show_control_text_3_y = 410
show_control_text_3 = "Backspace to delete the number."

show_control_text_4_x = 380
show_control_text_4_y = 440
show_control_text_4 = "Enter to confirm the number."


# recursively makes a copy
def deep_copy(obj):
    if type(obj) != list:
        return obj
    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))
    return copy


def base_board_selecter():
    global base_board
    global board
    global solved_board
    for x in range(len(boardlist)):
        if x + 1 == board_sel_count_value:
            base_board = deep_copy(boardlist[x])


base_board_selecter()
board = deep_copy(base_board)
solved_board = deep_copy(base_board)


# checks if num is valid in position in board
def valid(y, x, num):
    for q in range(len(solved_board)):
        if solved_board[y][q] == num:
            return False
    for q in range(len(solved_board)):
        if solved_board[q][x] == num:
            return False
    xbox = (x // 3) * 3
    ybox = (y // 3) * 3
    for q in range(3):
        for p in range(3):
            if solved_board[ybox + q][xbox + p] == num:
                return False
    return True


# solves a deep_copy of board
# @returns the solved board
def solve():
    for y in range(len(solved_board)):
        for x in range(len(solved_board)):
            if solved_board[y][x] == 0:
                for num in range(1, 10):
                    if valid(y, x, num):
                        solved_board[y][x] = num
                        solve()
                        if sum([x.count(0) for x in solved_board]) == 0:
                            return solved_board
                        solved_board[y][x] = 0
                return None


# making the board
def draw_lines():
    for x in range(0, 10):
        if x % 3 == 0:
            line_thickness = 4
        else:
            line_thickness = 1
        pygame.draw.line(screen, (0, 0, 0), (0, x * 40), (360, x * 40), line_thickness)
        pygame.draw.line(screen, (0, 0, 0), (x * 40, 0), (x * 40, 360), line_thickness)
    pygame.draw.line(screen, (0, 0, 0), (360, 0), (360, 480), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 420), (360, 420), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 363), (0, 477), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 477), (637, 477), 4)
    pygame.draw.rect(screen, (0, 0, 0), (360, 0, 280, 80))
    pygame.draw.line(screen, (0, 0, 0), (637, 0), (637, 480), 4)
    pygame.draw.line(screen, (0, 0, 0), (637, 0), (637, 480), 4)
    pygame.draw.line(screen, (0, 0, 0), (363, 125), (637, 125), 1)
    pygame.draw.line(screen, (0, 0, 0), (498, 125), (498, 185), 1)
    pygame.draw.line(screen, (0, 0, 0), (363, 187), (637, 187), 4)
    pygame.draw.line(screen, (0, 0, 0), (363, 263), (637, 263), 4)
    pygame.draw.line(screen, (0, 0, 0), (363, 325), (637, 325), 1)


# drawing the board numbers ingame
def draw_board():
    for y in range(len(board)):
        for x in range(len(board)):
            board_font = pygame.font.Font("freesansbold.ttf", 24)
            board_y = 40 * y + 10
            board_x = 40 * x + 15
            num = str(board[y][x])
            if board[y][x] > 0:
                brd = board_font.render(num, True, draw_board_color)
                screen.blit(brd, (board_x, board_y))


# drawing the buttons
def draw_button(x, y, x1, y1, w1, h1, txt):
    # start button
    pygame.draw.rect(screen, (255, 255, 255), (x1, y1, w1, h1))
    screen.blit(txt, (x, y))
    if x1 < mouse[0] < x1 + w1 and y1 < mouse[1] < y1 + h1:
        pygame.draw.rect(screen, (160, 160, 160), (x1, y1, w1, h1))
        screen.blit(txt, (x, y))


def start_button_func():
    global game_state
    global start_time
    global key
    global board
    global start_text
    global draw_board_color
    global solve_text
    global solve_value
    if (
        start_button_x < mouse[0] < start_button_x + start_button_w
        and start_button_y < mouse[1] < start_button_y + start_button_h
    ):
        if game_state == 0:
            start_time = time.time()
            key = None
            game_state = 1
            start_text = start_button_font.render("Stop", True, (0, 0, 0))
            board = deep_copy(base_board)
            draw_board_color = (0, 0, 0)
            solve_text = start_button_font.render("Solve", True, (0, 0, 0))
            solve_value = 0
        elif game_state == 1:
            start_time = time.time()
            key = None
            game_state = 0
            start_text = start_button_font.render("Start", True, (0, 0, 0))
            board = deep_copy(base_board)
            draw_board_color = (0, 0, 0)


def interactive_board():
    for y in range(len(board)):
        for x in range(len(board)):
            # variables
            board_font = pygame.font.Font("freesansbold.ttf", 24)
            board_y = 40 * y + 10
            board_x = 40 * x + 15

            if x % 3 == 0:
                start_x = 40 * x + 3
                width = 37
            elif x % 3 == 1:
                start_x = 40 * x + 1
                width = 39
            elif x % 3 == 2:
                start_x = 40 * x + 1
                width = 38

            if y % 3 == 0:
                start_y = 40 * y + 3
                height = 37
            elif y % 3 == 1:
                start_y = 40 * y + 1
                height = 39
            elif y % 3 == 2:
                start_y = 40 * y + 1
                height = 38

            # func
            if board[y][x] == 0 and game_state == 1:
                if x * 40 < mouse[0] < x * 40 + 40 and y * 40 < mouse[1] < y * 40 + 40:
                    pygame.draw.rect(
                        screen, (160, 160, 160), (start_x, start_y, width, height)
                    )
                if selected == (y, x):
                    pygame.draw.rect(
                        screen, (0, 200, 0), (start_x, start_y, width, height)
                    )
                    pygame.draw.rect(
                        screen,
                        (255, 255, 255),
                        (start_x + 3, start_y + 3, width - 6, height - 6),
                    )
                    if key != None:
                        brd = board_font.render(str(key), True, (0, 0, 0))
                        screen.blit(brd, (board_x, board_y))


def selector():
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 0 and game_state == 1:
                if y == 0 and x == 0 and 0 < mouse[0] < 40 and 0 < mouse[1] < 40:
                    return (0, 0)
                elif (
                    y > 0
                    and x == 0
                    and 0 < mouse[0] < 40
                    and y * 40 < mouse[1] < y * 40 + 40
                ):
                    return (y, 0)
                elif (
                    y == 0
                    and x > 0
                    and x * 40 < mouse[0] < x * 40 + 40
                    and 0 < mouse[1] < 40
                ):
                    return (0, x)
                else:
                    if (
                        x * 40 < mouse[0] < x * 40 + 40
                        and y * 40 < mouse[1] < y * 40 + 40
                    ):
                        return (y, x)


# mistake function
def show_mistake(x, y):
    global mistake_value
    mstk = mistake_font.render("Mistakes: " + str(mistake_value), True, (0, 0, 0))
    screen.blit(mstk, (x, y))
    if game_state == 0:
        mistake_value = 0


# time function
def show_time(x, y):
    if game_state == 1:
        current_time = time.time()
        time_text = time_font.render(
            "Time: " + str(int(current_time - start_time)) + "s", True, (0, 0, 0)
        )
        screen.blit(time_text, (x, y))
    if game_state == 0:
        time_text = time_font.render("Time: 0s", True, (0, 0, 0))
        screen.blit(time_text, (x, y))


# board select
def show_board_select():
    board_sel_text = board_sel_font.render("Board select", True, (0, 0, 0))
    screen.blit(board_sel_text, (board_sel_x, board_sel_y))

    board_sel_count_text = board_sel_count_font.render(
        str(board_sel_count_value) + " / " + "3", True, (0, 0, 0)
    )
    screen.blit(board_sel_count_text, (board_sel_count_x, board_sel_count_y))


def board_sel_button_func():
    global board_sel_count_value
    global board
    global solved_board
    if solve_value == 0:
        if (
            board_sel_up_x < mouse[0] < board_sel_up_x + board_sel_up_w
            and board_sel_up_y < mouse[1] < board_sel_up_y + board_sel_up_h
        ):
            if game_state == 0:
                board_sel_count_value += 1
                base_board_selecter()
                board = deep_copy(base_board)
                solved_board = deep_copy(base_board)
                solved_board = solve()
        elif (
            board_sel_down_x < mouse[0] < board_sel_down_x + board_sel_down_w
            and board_sel_down_y < mouse[1] < board_sel_down_y + board_sel_down_h
        ):
            if game_state == 0:
                board_sel_count_value -= 1
                base_board_selecter()
                board = deep_copy(base_board)
                solved_board = deep_copy(base_board)
                solved_board = solve()

        if board_sel_count_value <= 1:
            board_sel_count_value = 1
        elif board_sel_count_value >= 3:
            board_sel_count_value = 3


def solve_button_func():
    global board
    global solve_text
    global solve_value
    if (
        solve_button_x < mouse[0] < solve_button_x + solve_button_w
        and solve_button_y < mouse[1] < solve_button_y + solve_button_h
    ):
        if game_state == 0:
            if sum([x.count(0) for x in board]) == 0:
                board = deep_copy(base_board)
                solve_text = start_button_font.render("Solve", True, (0, 0, 0))
                solve_value = 0
            else:
                board = deep_copy(solved_board)
                solve_text = start_button_font.render("Unsolve", True, (0, 0, 0))
                solve_value = 1


solved_board = solve()


def main_compare():
    global board
    global mistake_value
    global key
    if game_state == 1:
        for y in range(len(board)):
            for x in range(len(board)):
                if selected == (y, x):
                    if key == None:
                        return
                    elif key == solved_board[y][x]:
                        board[y][x] = key
                        key = None
                    elif key != solved_board[y][x]:
                        mistake_value += 1


def won_game():
    global draw_board_color
    if game_state == 1 and sum([x.count(0) for x in board]) == 0:
        draw_board_color = (0, 200, 0)


def show_controls():
    show_control_text = show_control_font.render("Controls:", True, (0, 0, 0))
    screen.blit(show_control_text, (show_control_x, show_control_y))

    show_control_text2_1 = show_control_text_font.render(
        show_control_text_1, True, (0, 0, 0)
    )
    screen.blit(show_control_text2_1, (show_control_text_1_x, show_control_text_1_y))

    show_control_text2_2 = show_control_text_font.render(
        show_control_text_2, True, (0, 0, 0)
    )
    screen.blit(show_control_text2_2, (show_control_text_2_x, show_control_text_2_y))

    show_control_text2_3 = show_control_text_font.render(
        show_control_text_3, True, (0, 0, 0)
    )
    screen.blit(show_control_text2_3, (show_control_text_3_x, show_control_text_3_y))

    show_control_text2_4 = show_control_text_font.render(
        show_control_text_4, True, (0, 0, 0)
    )
    screen.blit(show_control_text2_4, (show_control_text_4_x, show_control_text_4_y))


# Game Loop
running = True
while running:
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_button_func()
            board_sel_button_func()
            selected = selector()
            solve_button_func()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                key = 1
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                key = 2
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                key = 3
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                key = 4
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                key = 5
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                key = 6
            if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                key = 7
            if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                key = 8
            if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                key = 9
            if event.key == pygame.K_BACKSPACE:
                key = None
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                main_compare()

    draw_lines()
    draw_board()
    show_mistake(mistake_x, mistake_y)
    show_time(time_x, time_y)
    show_board_select()
    draw_button(
        start_text_x,
        start_text_y,
        start_button_x,
        start_button_y,
        start_button_w,
        start_button_h,
        start_text,
    )
    draw_button(
        board_sel_up_text_x,
        board_sel_up_text_y,
        board_sel_up_x,
        board_sel_up_y,
        board_sel_up_w,
        board_sel_up_h,
        board_sel_up_text,
    )
    draw_button(
        board_sel_down_text_x,
        board_sel_down_text_y,
        board_sel_down_x,
        board_sel_down_y,
        board_sel_down_w,
        board_sel_down_h,
        board_sel_down_text,
    )
    draw_button(
        solve_text_x,
        solve_text_y,
        solve_button_x,
        solve_button_y,
        solve_button_w,
        solve_button_h,
        solve_text,
    )
    show_controls()
    won_game()
    interactive_board()
    pygame.display.update()
