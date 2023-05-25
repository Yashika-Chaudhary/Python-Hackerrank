def swap_case(s):
    new_str = []
    for i in s:
        if i == i.upper(): 
            new_str.append(i.lower())
        else: 
            new_str.append(i.upper())
    return ''.join(new_str) 


if __name__ == '__main__':
