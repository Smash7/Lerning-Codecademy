from contextlib import contextmanager


class personalized():
  def __init__(self, sender, receiver):
    self.file = open(
        f"Python3 Intermediate/Aisha's Greetings (Project 7)/{sender}_personalized.txt", "w")
    self.sender = sender
    self.receiver = receiver

  def __enter__(self):
    self.file.write(f"Dear {self.receiver}\n")
    return self.file

  def __exit__(self, *exc):
    self.file.write(f"\nSincerely, {self.sender} \n")
    self.file.close()


@contextmanager
def generic(card_type, sender, recipient):
  card_file = open(card_type, 'r')
  order = open(
      f"Python3 Intermediate/Aisha's Greetings (Project 7)/{sender}_generic.txt", 'w')
  try:
    order.write(f"Dear {recipient}, \n")
    order.write(card_file.read())
    order.write(f"\nSincerely, {sender} \n")
    yield order
  finally:
    card_file.close()
    order.close()


with generic("Python3 Intermediate/Aisha's Greetings (Project 7)/thankyou_card.txt", "Mwenda", "Amanda") as file:
  print("Card Generated!")

with personalized('John', 'Michael') as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don't say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

with generic("Python3 Intermediate/Aisha's Greetings (Project 7)/thankyou_card.txt", 'Josiah', 'Remy') as gen, personalized('Josiah', 'Esther') as card:
  card.write("Happy Birthday!! I love you to the moon and back. Even though you're a pain sometimes, you're a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You're getting old!")
