team1 = ('enter a team name')
each_win_gets = 3
each_draw_gets = 1
each_loss_gets = 0
number1 = input('enter a team wins')
number1 = int(number1)
number2 = input('enter a team draws')
number2 = int(number1)
number3 = input('enter a team losses')
number3 = int(number3)
total = (number1 * 3) + (number2 * 1) + (number3 * 0)
print('the total points for team1 is',total)