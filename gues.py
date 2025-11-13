from random import randint
from collections import Counter


def generate_number(length: int = 3) -> str:
    digits: list[int] = []
    while len(digits) < length:
        digit = randint(0, 9)
        if digit not in digits:
            digits.append(digit)
    return ''.join(map(str, digits))


def check_guess(secret: str, guess: str) -> tuple[int, int]:
    bulls = sum(s == g for s, g in zip(secret, guess))
    
    secret_counter = Counter(secret)
    guess_counter = Counter(guess)
    total_matches = sum((secret_counter & guess_counter).values())
    
    cows = total_matches - bulls
    
    return bulls, cows


def validate_input(guess: str, length: int) -> bool:
    return guess.isdigit() and len(guess) == length and len(set(guess)) == length


def play_game(length: int = 3) -> None:
    secret = generate_number(length)
    attempts = 0
    
    while True:
        guess = input()
        
        if not validate_input(guess, length):
            print(f"Enter {length} unique numbers")
            continue
        
        attempts += 1
        bulls, cows = check_guess(secret, guess)
        
        if bulls == length:
            print(f"Guesed in {attempts} attempts")
            break
        
        result = []
        if bulls > 0:
            result.extend(["+1"] * bulls)
        if cows > 0:
            result.extend(["-1"] * cows)
        if not result:
            result.append("0")
        
        print(" ".join(result))


if __name__ == "__main__":
    play_game(3)