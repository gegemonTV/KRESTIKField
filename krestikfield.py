import random



score = {'Player': 0, 'PC': 0}

def view_field():
    print(f''' {field[1]} │ {field[2]} │ {field[3]}
───┼───┼───
 {field[4]} │ {field[5]} │ {field[6]}
───┼───┼───
 {field[7]} │ {field[8]} │ {field[9]}''')

def p_step():
    step = int(input())
    while field[step] == 'o' or field[step] == 'x':
        step = int(input('input another numbor: '))
    field[step] = 'x'

def ai_step():
    step = random.randint(1,9)
    while field[step] == 'o' or field[step] == 'x':
        step = random.randint(1,9)
    field[step] = 'o'

def pc_step():
    step = random.randint(1,9)
    while field[step] == 'o' or field[step] == 'x':
        step = random.randint(1,9)
    field[step] = 'x'
    
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
        if check_win('x') == 1:
            print('жы!')
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        if check_win('o')==1:
            print('жыжищ!')
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        view_field()
        i+=1
        pc_step()
         
        
        if check_win('x') == 1:
            print('жы!')
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        if check_win('o')==1:
            print('жыжищ!')
            score_edit()
            print(f"Player: {score['Player']} ============== PC: {score['PC']}")
            y = input('enter Enter')
            break
        
        
        view_field()
    if i>=9:
        if check_win('x') ==0 and check_win('o') == 0:
            print('nothing')
            y = input('enter Enter')
            
   
