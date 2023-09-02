#Write a program that takes side of a square as input and calculates the area of this square by using area() function.

def area(side):
  return side * side
if __name__ == "__main__":
  side = int(input("Enter the side of the square: "))
  print("The area of the square is", area(side))
