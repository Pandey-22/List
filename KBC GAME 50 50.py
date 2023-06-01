print("WELCOME TO KBC GAME")
name=input("enter the name")
questions_list=[["What is the capital of India"],["How many countries in Asia"],
    ["When did India become independent"],["Wow many states are there in India"]]
options_list=[["1.Banglore","2.Delhi","3.Chandigarh","4.Bhopal"],["1.18","2.28","3.38","4.48"],
    ["1.15August-1945","2.15August-1946","3.15August-1947","4.15August-1949"],["1.28","2.38","3.18","4.58"]]
solution_list=[2,4,3,1]
lifeline_5050_list=[["1.Banglore","2.Delhi"],["1.48","2.38"],["1.15August-1946","2.15August-1947"],["1.28","2.38"]]
lifeline_5050_solution_list=[2,1,2,1]
i=0
count=0
while i<len(questions_list):
    print("Q",i+1,questions_list[i])
    j=0
    while j<len(options_list):
        print(j+1,options_list[i][j])
        j=j+1
    b=int(input("enter your anynumber otherwise use lifelife 5050"))
    if b==solution_list[i]:
        print("Congratulations🥳🥳! Your answer is correct")
    elif b==5050:
        print("Okay let's use lifeline 5050")
        if count==0:
            k=0
            while k<len(lifeline_5050_list):
                print(k+1,lifeline_5050_list[k])
                k=k+1
            count=count+1
            c=int(input("Enter the anynumber"))
            if c==lifeline_5050_solution_list[i]:
                print("Congratulations🥳🥳 you won this money")
            else:
                print("Sorry😒😒! Your answer is wrong you are lost your money")
        else:
            print("Sorry🙏🙏! Now you can't use 5050 because you already used the 5050")
            d=int(input("Enter the anynumber"))
            if d==solution_list[i]:
                print("Congratulations🥳🥳! Correct answer")
            else:
                print("Sorry😒😒! Wrong answer")
                break
    else:
        print("Your answer is wrong that's why next time you will try again")
        break
    i=i+1