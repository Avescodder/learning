import json
from typing import Literal
from random import randbytes

ByteOrder = Literal['little', 'big']

size: dict[int, ByteOrder] = {
    1: 'big',
    2: 'little'
}

sent: dict[int, str] = {
    1: 'Please, choose one number from 1 to 4 (bytes size) ->\n',
    2: 'Perfect, now lets play a game, enter 1 or 2 ->\n',
    3: 'Your guess (attempt {attempt}/15) ->\n',
    4: 'Too low! Try higher.\n',
    5: 'Too high! Try lower.\n',
    6: '🎉 Congratulations! You guessed it in {attempt} attempts!\n',
    7: '💀 Game Over! The number was {number}. Better luck next time!\n'
}

ciphers: dict[int, dict] = {
    1: {
        'name': 'QUANTUM_FLUX_CIPHER',
        'description': 'Encrypted with quantum entanglement protocol',
        'difficulty': '⭐⭐⭐',
        'hint': 'Numbers between cosmic boundaries'
    },
    2: {
        'name': 'NEURAL_MATRIX_CODE',
        'description': 'Protected by neural network encryption',
        'difficulty': '⭐⭐⭐⭐',
        'hint': 'Pattern recognition required'
    },
    3: {
        'name': 'VOID_SHADOW_PROTOCOL',
        'description': 'Secured with dark matter algorithms',
        'difficulty': '⭐⭐⭐⭐⭐',
        'hint': 'Hidden in the void'
    }
}


def print_banner() -> None:
    banner = """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║        🎮  BYTE DECODER: THE NUMBER GAME  🎮            ║
    ║                                                          ║
    ║              Crack the encrypted bytes                   ║
    ║              15 attempts to decode reality               ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print(banner)


def print_ciphers() -> None:
    print("\n📡 AVAILABLE ENCRYPTION PROTOCOLS:\n")
    cipher_data = json.dumps(ciphers, indent=4, ensure_ascii=False)
    print(cipher_data)
    print()


def get_bytes_size() -> int:
    while True:
        try:
            size: int = int(input(sent[1]))
            if 1 <= size <= 4:
                return size
            print('❌ Choose between 1 and 4 bytes.\n')
        except ValueError:
            print('❌ Please enter a valid number.\n')


def get_random_bytes(num_bytes: int) -> bytes:
    bytes_num: bytes = randbytes(num_bytes)
    return bytes_num


def get_number_for_bytes(x: int = 2) -> int:
    num: int = int(input(sent[x]))
    return num


def decode_bytes(bytes_num: bytes, byte_order: Literal['little', 'big']) -> int:
    number: int = int.from_bytes(bytes_num, byteorder=byte_order)
    return number


def get_size(key: int) -> Literal['little', 'big']:
    return size[key]


def get_cipher_choice() -> int:
    while True:
        try:
            choice: int = int(input('Select cipher protocol (1, 2, or 3) ->\n'))
            if choice in ciphers:
                return choice
            print('❌ Invalid protocol. Choose 1, 2, or 3.\n')
        except ValueError:
            print('❌ Please enter a valid number.\n')


def display_cipher_info(cipher_id: int) -> None:
    cipher = ciphers[cipher_id]
    print(f"\n🔐 SELECTED: {cipher['name']}")
    print(f"📝 {cipher['description']}")
    print(f"💪 Difficulty: {cipher['difficulty']}")
    print(f"💡 Hint: {cipher['hint']}\n")


def play_game(target: int, max_attempts: int = 15) -> bool:
    for attempt in range(1, max_attempts + 1):
        try:
            guess: int = int(input(sent[3].format(attempt=attempt)))
            
            if guess == target:
                print(sent[6].format(attempt=attempt))
                return True
            elif guess < target:
                print(sent[4])
            else:
                print(sent[5])
                
        except ValueError:
            print('❌ Invalid input. Enter a number.\n')
            continue
    
    print(sent[7].format(number=target))
    return False


def display_encrypted_number(encrypted_bytes: bytes, cipher_id: int, max_value: int) -> None:
    print(f"\n🔒 ENCRYPTED DATA:")  # noqa: F541
    print(f"Cipher: {ciphers[cipher_id]['name']}")
    print(f"Raw bytes: {encrypted_bytes.hex()}")
    print(f"Length: {len(encrypted_bytes)} bytes")
    print(f"Binary: {bin(int.from_bytes(encrypted_bytes, 'big'))}")
    print(f"Max possible value: {max_value:,}\n")


def main() -> None:
    print_banner()
    print_ciphers()
    
    cipher_choice: int = get_cipher_choice()
    display_cipher_info(cipher_choice)
    
    bytes_size: int = get_bytes_size()
    
    byte_order_key: int = get_number_for_bytes()
    byte_order: Literal['little', 'big'] = get_size(byte_order_key)
    
    random_bytes: bytes = get_random_bytes(bytes_size)
    target_number: int = decode_bytes(random_bytes, byte_order)
    
    max_value: int = 256 ** bytes_size - 1
    
    display_encrypted_number(random_bytes, cipher_choice, max_value)
    
    print(f"🎯 MISSION: Decode the number from encrypted bytes")  # noqa: F541
    print(f"📊 Byte order: {byte_order.upper()}")
    print(f"🎲 Number range: 0 - {max_value:,}")
    print(f"⏱️  Attempts: 15\n")  # noqa: F541
    print("="*60)
    print("GAME START!")
    print("="*60 + "\n")
    
    success: bool = play_game(target_number)
    
    if success:
        print("\n🏆 You are a master decoder! 🏆")
    else:
        print("\n💻 System encrypted. Try again, hacker.")


if __name__ == '__main__':
    main()