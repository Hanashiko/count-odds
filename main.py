from typing import List

def countOdds(low: int, high: int) -> int:
    count: int = 0
    for i in range(low, high + 1):
        if i % 2 != 0:
            count += 1
    return count

def main() -> None:
    print(countOdds(3, 7))
    print(countOdds(8, 10))
    print(countOdds(800445804, 979430543))

if __name__ == "__main__":
    main()