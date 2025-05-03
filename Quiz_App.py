def load_questions(filename):
    questions = []
    with open(filename , "r") as file:
        for line in file:
            parts = line.strip().split("|")
            if len(parts) == 5:
                q = {
                    "question": parts[0],
                    "options": parts[1:5],
                    "answer": parts[1]
                }
                questions.append(q)
    return questions

def run_quiz(questions):
    score = 0
    for i , q in enumerate(questions,1):
        print(f"\nQuestion {i}: {q['question']}")
        for idx, opt in enumerate(q["options"], 1):
            print(f"{idx}.{opt}")
        
        choice = input("your answer is (1-4): ")
        if choice.isdigit():
            selected = int(choice)
            if 1<=selected <=4:
                if q["options" [selected - 1] == q["answer"]]:
                    score += 1
        return score

def main():
    file_name = "question.txt"
    questions = load_questions(file_name)
    if not questions:
        print("not questions found.")
        return
    total = len(questions)
    score = run_quiz(questions)
    print(f"\nyour score is : {score}/{total}")

if __name__ == "__main__":
    main()



