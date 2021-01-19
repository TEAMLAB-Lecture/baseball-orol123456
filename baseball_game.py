# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):

    return user_input_number.isdigit()


def is_between_100_and_999(user_input_number):
    if 100<=int(user_input_number)<1000:
        return True
    return False


def is_duplicated_number(three_digit):
    if len(three_digit)>len(set(three_digit)):
        return True
    return False


def is_validated_number(user_input_number):
    if is_digit(user_input_number) and not is_duplicated_number(user_input_number) and is_between_100_and_999(user_input_number):
        return True
    return False


def get_not_duplicated_three_digit_number():
    while True:
        n=get_random_number()
        if not is_duplicated_number(str(n)):
            return n



def get_strikes_or_ball(user_input_number, random_number):
    strike,ball=0,0
    if user_input_number==random_number:
        strike=3
    else:
        for n in user_input_number:
            if n in random_number:
                if user_input_number.index(n) == random_number.index(n):
                    strike+=1
                else:
                    ball+=1
    return strike,ball


def is_yes(one_more_input):
    tmp=one_more_input
    while True:
        tmp=tmp.lower()
        if tmp=='y' or tmp=='yes':
            return True
        elif tmp=='n' or tmp=='no':
            return False
        else:
            print('Wrong Input, Input again')
            tmp=input("You win, one more(Y/N) ?")


def is_no(one_more_input):
    while True:
        tmp=one_more_input.lower()
        print(tmp)
        if tmp=='n' or tmp=='no':
            return True
        elif tmp=='y' or tmp=='yes':
            return False
        else:
            print('Wrong Input, Input again')
            tmp=input("You win, one more(Y/N) ?")


def main():
    print("Play Baseball")
    user_input = 999
    while True:
        flag=False
        flag2=False
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        # ===Modify codes below=============
        # 위의 코드를 포함하여 자유로운 수정이 가능함
        while True:
            guess=input('Input guess number : ')
            if guess.isdigit():
                if int(guess)==0:
                    flag2=True
                    break
            if is_validated_number(guess):
                strike,ball=get_strikes_or_ball(guess,random_number)
                print("Strikes : {} , Balls : {}".format(strike,ball))
                if strike==3:
                    res=(input("You win, one more(Y/N) ?"))
                    print(res)
                    if is_yes(res):
                        flag=True
                        break
                    else:
                        break
            else:
                print('Wrong Input, Input again')
                print('asdf')

        if not flag:
            break
        if flag2:
            break
    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
