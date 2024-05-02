if __name__ == "__main__":
  # Introduction to the Python for else statement

  """
  In Python, the for statement can have an optional else clause, which you may not be familiar with especially if you"re coming from other languages such as Java or C#.
  The following shows the syntax of the for statement with the else clause:

  for item in iterables:
    # process item
  else:
    # statement

  In this syntax, the else clause will execute only if the loop runs normally.
  In other words, the else clause won"t execute if the loop encounters a break statement.
  In addtional, the else clause also executes when the iterables object has no item.
  The following flowchart illustrates the for ... else statement:

  The else clause is quite useful in some cases if you know how to apply it effectively.
  """

  # Python for else statement example

  people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Peter", "age": 30},
    {"name": "Jenifer", "age": 28}
  ]

  name = input("Enter a name: ")

  # found = False
  # for person in people:
  #   if person["name"] == name:
  #     found = True
  #     print(person)
  #     break

  # if not found:
  #   print(f"{name} not found!")

  for person in people:
    if person["name"] == "name":
      print(person)
      break
  else:
    print(f"{name} not found!")
