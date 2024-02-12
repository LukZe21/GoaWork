user_input = input('Enter equation - ') # მომხმარებელი იყვანს მაგალითს ( სასურველია ყოველი character იყოს გამოტოვებული ' ')


# კალკულატორის ფუნქცია
def calculator(user_input):
    nums = user_input.split(' ') # მომხმარებლის ჩანაწერს გაყოფს
    symbol = nums[1] # ამოიღებს პირველ ინდექსად მყოფ character-ს (ამ შემთხვევაში მათემატიკურ ნიშანს)
    nums = [int(i) for i in nums if i.isdigit()] # for loop-ის გამოყენებით იქმნება სია სადაც მხოლოდ integer ღირებულებები ემატება

    # შემდეგისთვის შესატანი 2 რიცხვი
    num0 = 0
    num1 = 0

    # for loop-ს გამოიყენება nums ცვლადის list-ზე
    for idx, num in enumerate(nums):
        if idx == 0: # პირველი რიცხვი დაემატება num0 ცვლადს
            num0 += num
        elif idx == 1: # მეორე რიცხვი დაემატება num1 ცვლადს
            num1 += num

    # მათემატიკური ფუნქციების სია
    function_dict = {'+': num0+num1, '-': num0-num1, '/': num0/num1, '*': num0*num1}        
    if symbol in function_dict.keys(): # თუ სიმბოლო იქნება ფუნქციის სიაში
        return function_dict.get(symbol) # დააბრუნებს ორი რიცხვის გამოთვლას.
    
print(calculator(user_input))







