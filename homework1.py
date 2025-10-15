import re

def replace_word(text, old, new):
    return text.replace(old, new)

def to_title_case(text):
    return text.title()

def extract_date(text):
    match = re.search(r'(\d{1,2})[/-](\d{1,2})[/-](\d{4})', text)
    if match:
        d, m, y = match.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"
    return None

if __name__ == "__main__":
    sentence = "hello world, world is big"
    print(replace_word(sentence, "world", "earth"))

    print(to_title_case("this is a title test"))

    date_text = "Today is 05/10/2025"
    print(extract_date(date_text))