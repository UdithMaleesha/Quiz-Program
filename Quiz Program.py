#a dictionaty that stores questions and answers 
#have a veriable that tracks the score of the answers
#loop through the dictionary using the key value pairs
#display each question  to the user and allow them ti answer
#tell them if they  are right or wrong
#show the final result  when quiz is completed


quiz ={
    
    "question1" :{
        
        "question" : "What is the capital of sri lanka?",
        "answer" : "Sri jayawardenepura kotte"
    },
    
    "question2":{
        "question" :"What is the capital of  Germany?",
        "answer" :"Berlin"
    },
    
    "question3":{
        
        "question" : "What is the capital of Italy?",
        "answer" : "Rome"
    },

    "question4":{
        
        "question": "What is the capital of Japan?",
        "answer" : "Tokyo"                
    },
        
     "question5":{
        
        "question": "What is the capital of Spain?",
        "answer" : "Madrid"                
    },
     
     
     "question6":{
        
        "question": "What is the capital of India?",
        "answer" : "New Delhi"                
    },
     
     
     "question7":{
        
        "question": "What is the capital of Switzerland?",
        "answer" : "Bern"                
    },      
}
 
score = 0   

for key, value in quiz.items():
    print(value ['question'])
    answer = input ("Answer?")
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is : "+ str(score))
        print("")
        print("")
    
    else:
        print("Wrong!")
        print("The answer is :" + value ['answer'] )
        print("Your Score  is:" + str(score))
        print("")     
        print("")


print("You got " + str (score) + "out of 7 question correctly" )  
print("Your percentage is " + str(int(score/7 *100))+"%" )     
        
    
    
    
