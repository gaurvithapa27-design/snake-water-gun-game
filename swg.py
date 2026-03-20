import random
computer=random.choice(['snake', 'water', 'gun'])
user=int(input("Enter your choice (1 for snake, 2 for water, 3 for gun): "))
a=''
if user==1:
    a='snake'
elif user==2:
    a='water'
elif user==3:
    a='gun'
print(f"Computer chose: {computer}")
print(f"User chose: ",a)
if computer==a:
    print("It's a tie!")
elif (computer=='snake' and a=='water') or (computer=='water' and a=='gun') or (computer=='gun' and a=='snake'):
    print("Computer wins!")
elif(computer=='water' and a=='snake')or(computer=='gun' and a=='water')or(computer=='snake' and a=='gun'):
    print("You win!")
else:
    print("Invalid input! Please choose 'snake', 'water', or 'gun'.")