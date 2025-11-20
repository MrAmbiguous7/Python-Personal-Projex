'''
file = open('practicetext11-6-25.txt', 'a+')
userin = input('This will be appended to the file : ')
file.write(userin)

file.seek(0)

print(file.read())

file.close()
'''
'''
with open('practicetext11-6-25.txt', 'r') as f:
    f.read()
'''
import math


def addscore(score, filename = 'practicetext11-6-25.txt'):
    with open(filename, 'a') as file:
        file.write(f'{score}\n')
def readscores(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        uscores = [float(line.strip()) for line in lines]
        return uscores
def main():
    while True:
        score = input('What was the score (q) to quit: ')
        if score != 'q':
            addscore(score)
        else:
            break
def displayinfo(ascores):
    print(f'Scores: {ascores}')
    print(f'Average: {sum(ascores)} / {len(ascores)}')
    print(f'Highest: {max(ascores)}')
    print(f'Lowest: {min(ascores)}')



main()
ascores = readscores('practicetext11-6-25.txt')
print(ascores)
