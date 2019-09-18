import random



score = {'Player': 0, 'PC': 0}

w_steps = {}

def view_field():
    print(f''' {field[1]} │ {field[2]} │ {field[3]}
───┼───┼───
 {field[4]} │ {field[5]} │ {field[6]}
───┼───┼───
 {field[7]} │ {field[8]} │ {field[9]}''')

def some_steps(let):
    mb_steps = []
    for i in range(1,10):
        if field[i] == 'o' or field[i] == 'x':
            continue
        else:
            mb_steps.append(f'{i}{let}')
    return mb_steps


def restring(m):
    ch = ''
    for i in range(len(m)-1):
        ch+=m[i]
    return ch


def ai_step():
    global w_steps
    ch = ''
    st = some_steps('o')
    global game, field
    step = random.randint(1,9)
    while field[step] == 'o' or field[step] == 'x':
        step = random.randint(1,9)
    field[step] = 'o'
    game.append(f'{step}o')
    g = restring(game)
    for i in range(len(st)):
        ch = f'{g}{st[i]}'
        if w_steps.get(ch) == None:
            w_steps[ch] = 1
             
            print(w_steps)    

def pc_step():
    global game
    step = random.randint(1,9)
    while field[step] == 'o' or field[step] == 'x':
        step = random.randint(1,9)
    field[step] = 'x'
    game.append(f'{step}x')
    
def check_win(let):
    if field[1] == field[2] and field[2]==field[3] and field[1]==let:
        return 1
    elif field[4] == field[5] and field[5]==field[6] and field[4]==let:
        return 1
    elif field[7] == field[8] and field[8]==field[9] and field[7]==let:
        return 1
    if field[1] == field[4] and field[4]==field[7] and field[1]==let:
        return 1
    if field[2] == field[5] and field[5]==field[8] and field[2]==let:
        return 1
    if field[3] == field[6] and field[6]==field[9] and field[3]==let:
        return 1
    if field[1] == field[5] and field[5]==field[9] and field[1]==let:
        return 1
    if field[7] == field[5] and field[5]==field[3] and field[7]==let:
        return 1
    else:
        return 0

def score_edit():
    if check_win('x') == 1:
        score['Player'] += 1
        
    elif check_win('o') == 1:
        score['PC'] += 1


while True:
    game = []
    i=1
    field = {1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6',
             7: '7', 8: '8', 9: '9'}
    


    
    print('hollo')


    while i<9:
        i+=1       
        print()
        print()
        
        ai_step()
        
        print(game)
        
        if check_win('x') == 1:
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        if check_win('o')==1:
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        view_field()
        i+=1
        pc_step()
        view_field()
        print(game)
        if check_win('x') == 1:
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        if check_win('o')==1:
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        
        
        view_field()
    if i>=9:
        if check_win('x') ==0 and check_win('o') == 0:
            print('nothing')
            y = input('enter Enter')
    print(w_steps)
            
   
