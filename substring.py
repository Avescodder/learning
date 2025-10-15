# Name extraction from a string using substring matching

def extract_name(input, name):
    start_index = input.find(name)
    if start_index != -1:
        end_index = start_index + len(name)
        return input[start_index:end_index]
    return ""

# Domain exatraction from eamil adress
def extartct_email_domain(email):
    start_index = email.find('@')
    print(start_index)
    if start_index != -1:
        return email[start_index + 1:]
    return ""

# main function 
def main():
    input_name = "Murat Okal"
    name = "Murat"
    email = input("Write your email here:\n")
    print(extract_name(input_name, name))
    print(extartct_email_domain(email))

if __name__ == '__main__':
    main()