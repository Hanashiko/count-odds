from typing import List

def countOdds(low: int, high: int) -> int:
    if low % 2 == 0:
        low += 1
    if high % 2 == 0:
        high -= 1
    return (high - low) // 2 + 1

def main() -> None:
    print(countOdds(3, 7))
    print(countOdds(8, 10))
    print(countOdds(800445804, 979430543))

if __name__ == "__main__":
    main()