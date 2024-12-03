import re

def main():
    summ = 0

    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    with open("example1_1.txt", "r") as w:
        for i in w:
            i = i.strip()
            matches = re.findall(pattern, i)
            
            summ += sum(int(a) * int(b) for a, b in matches)
    
    # Print the final sum
    print(f"Sum of all valid mul() instructions: {summ}")

if __name__ == "__main__":
    main()
