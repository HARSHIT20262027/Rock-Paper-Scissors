from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)

app.secret_key = "rockpaper123"


@app.route("/")
def home():

    if "user_score" not in session:
        session["user_score"] = 0

    if "computer_score" not in session:
        session["computer_score"] = 0

    return render_template(
        "index.html",
        user_score=session["user_score"],
        computer_score=session["computer_score"],
        name=session.get("name"),
        sound=""
)

@app.route("/play", methods=["POST"])
def play():

    if "name" not in session:
        session["name"] = request.form["name"]

    name = session["name"]

    user = request.form["choice"]

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    # ---------------- RESULT ---------------- #

    if user == computer:

        result = "🤝 Match Draw"
        color = "orange"
        sound = "draw"
        

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
):

        result = f"🏆 Congratulations {name}, You Won!"
        color = "green"
        sound = "win"

        session["user_score"] += 1

    else:

        result = "💻 Computer Won!"
        color = "red"
        sound = "lose"

        session["computer_score"] += 1

    return render_template(
        "index.html",
        name=name,
        user=user,
        computer=computer,
        result=result,
        color=color,
        sound=sound,      # <-- Ye line missing hai
        user_score=session["user_score"],
        computer_score=session["computer_score"]
    )
    


@app.route("/reset")
def reset():

    session.clear()

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)