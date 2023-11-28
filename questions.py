class Node:
  def __init__(self, text):
    self.text = text
    self.options = []

class Option:
  def __init__(self, text):
    self.text = text
    self.node = None

height_question = Node("Are you taller than 20 inches?")
age_question = Node("How old are you?")
too_short = Node("You are too short to go on this ride.")
too_young = Node("You are too young to go on this ride.")
just_right = Node("You can safely go on this ride.")

height_option_yes = Option("Yes")
height_option_no = Option("No")
age_option_younger = Option("Younger than 3 years old.")
age_option_exact = Option("Exactly 3 years old.")
age_option_older = Option("Older than 3.")

height_question.options.append(height_option_no)
height_question.options.append(height_option_yes)

age_question.options.append(age_option_younger)
age_question.options.append(age_option_exact)
age_question.options.append(age_option_older)

height_option_no.node = too_short
height_option_yes.node = age_question

age_option_younger.node = too_young
age_option_exact.node = too_young
age_option_older.node = just_right
