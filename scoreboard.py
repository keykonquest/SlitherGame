from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.update_data()

    def update_data(self):
        self.write(f"Score: {self.current_score}", False, "center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color((255, 0, 0))
        self.write("GAME OVER", False, "center", font=("Courier", 30, "normal"))

    def food_eaten(self):
        self.current_score += 1
        self.clear()
        self.update_data()
