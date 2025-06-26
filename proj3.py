#quiz app
def quiz():
    questions = {
        "What is the capital of India?": ("Delhi",),
        "What is 5 + 7?": ("12",),
        "Which language is this quiz written in?": ("Python",)
    }

    score = 0
    for q, ans in questions.items():
        user_ans = input(q + " ")
        score += 1 if user_ans.strip().lower() == ans[0].lower() else 0

    return score

get_level = lambda s: "Excellent" if s == 3 else "Good" if s == 2 else "Needs Improvement"

score = quiz()
print(f"Your score: {score}/3")
print("Performance:", get_level(score))
