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
    c=['y','yes']
    try:
        tmp=one_more_input.lower()
    except:
        return False
    else:
        if tmp in c:
            return True
        return False



def is_no(one_more_input):
    c=['n','no']
    try:
        tmp=one_more_input.lower()
    except:
        return False
    else:
        if tmp in c:
            return True
        return False


def main():
    print("Play Baseball")
    user_input = 999
    flag=True
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    while flag:  
        # ===Modify codes below=============
        # 위의 코드를 포함하여 자유로운 수정이 가능함
        while True:
            guess=input('Input guess number : ')
            if guess=='0':
                break
            else:
                if is_validated_number(guess):
                    strike,ball=get_strikes_or_ball(guess,random_number)
                    print("Strikes : {} , Balls : {}".format(strike,ball))
                    if strike==3:
                        while True:
                            res=(input("You win, one more(Y/N) ?"))
                            if is_no(res):
                                flag=False
                                break
                            elif is_yes(res):
                                random_number=str(get_not_duplicated_three_digit_number())
                                print("Random Number is : ",random_number)
                                break
                            else:
                                print('Wrong Input, Input again')
                else:
                    print('Wrong Input, Input again')
    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
