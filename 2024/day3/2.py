import re

def main():
    summ = 0
    enabled = True

    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"

    with open("example1_2.txt", "r") as w:
        for i in w:
            i = i.strip()
            matches = re.findall(pattern, i)

            for i in matches:
                if i == "don't()":
                    enabled = False
                elif i == "do()":
                    enabled = True
                
                if enabled and i.startswith("mul"):
                    numbers = i.replace("mul(", "").replace(")", "").split(",")
                    summ += int(numbers[0]) * int(numbers[1]) 
    
    # Print the final sum
    print(f"Sum of all valid mul() instructions: {summ}")

if __name__ == "__main__":
    main()
