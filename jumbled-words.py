import random

def choose():
    words = ['rainbow', 'mathematics', 'dog', 'cat', 'mountain', 'flower', 'edelweiss', 'marvel']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

def thank(p1n, p2n, p1, p2):
    print(p1n, " Your Score is : ", p1)
    print(p2n, " Your Score is : ", p2)
    if p1 > p2:
        print("Congratulations on your win ", p1n)
    elif p2 > p1:
        print("Congratulations on your win ", p2n)
    else:
        print("No winner this time!")
    print("Thanks for Playing \nHave a nice day!")

def play():
    p1name = input("Player 1, Please Enter your name : ")
    p2name = input("Player 2, Please Enter your name : ")
    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        picked_word = choose()
        qn = jumble(picked_word)
        print(qn)
        if turn % 2 == 0:
            print(p1name, ' Your Turn. ')
            ans = input('What is on my mind? ')
            if ans == picked_word:
                pp1 = pp1 + 1 
                print("Your score is : ", pp1)
            else:
                print("Better Luck Next Time, I thought : ", picked_word)
            c = int(input('Press 1 to continue and 0 to quit : '))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        else:
            print(p2name, ' Your Turn. ')
            ans = input('What is on my mind? ')
            if ans == picked_word:
                pp2 = pp2 + 1 
                print("Your score is : ", pp2)
            else:
                print("Better Luck Next Time, I thought : ", picked_word)
            c = int(input('Press 1 to continue and 0 to quit : '))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        turn = turn + 1
        
play()
