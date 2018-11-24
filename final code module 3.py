def load_file():
    import urllib.request
    local_path ="F:\\My Documents\\elements1_20.txt"
    url="https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt"
    urllib.request.urlretrieve(url,local_path)
    return local_path
path = load_file()
file = open(path,'r')
elements_list = []
line = file.readline().strip().lower()
while line:
    elements_list.append(line)
    line = file.readline().strip().lower()
file.close()

def get_names():
    test_elements = []
    print("List any 5 of the first 20 elements in the Periodic table\n")
    while len(test_elements)<5:
        test_element = input("Enter the name of an element: ").lower()
        if test_element in test_elements:
            print(test_element,'was already entered')
        elif test_element == "":
            pass
        else:
            test_elements.append(test_element)
    return test_elements

responses = get_names()
correct_list = []
incorrect_list = []

for response in responses:
    if response in elements_list:
        correct_list.append(response)
    else:
        incorrect_list.append(response)
print(len(correct_list)*20,'% correct')
print('Found: '," ",end="")
for element in correct_list:
    print(element.title(),' ',end="")
print('\nNot Found: ',' ',end="")
for element in incorrect_list:
    print(element.title(),' ',end="")
