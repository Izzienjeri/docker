def classify_integer(num: int) -> str:
  """
  Classifies an integer based on the following conditions:
  - If the integer is greater than 100, return "Greater than 100".
  - If the integer is between 50 and 100 (inclusive), return "Between 50 and 100".
  - If the integer is less than 50, return "Less than 50".
  """
  if num > 100:
    return "Greater than 100"
  elif 50 <= num <= 100:
    return "Between 50 and 100"
  else:
    return "Less than 50"

