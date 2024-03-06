print('Welcome to My Quiz!!')

play = input('Do you want to play the Quiz or not? ')

if play.lower() != 'yes':
    quit()

print("Let's Start our quiz")
score = 0

answer = input('Who is known as the "God of Cricket" in India? ').lower()
if answer.lower() == 'sachin tendulkar':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('Which Indian cricketer holds the record for the highest individual score in Test cricket? ').lower()
if answer.lower() == 'virender sehwag':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('In which year did India win their first Cricket World Cup? ').lower()
if answer == '1983':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('Who is the captain of the Indian cricket team in Test matches as of 2024? ').lower()
if answer.lower() == 'rohit sharma':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('Which Indian bowler has taken the most wickets in international cricket across all formats? ').lower()
if answer.lower() == 'anil kumble':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('In which city is the Wankhede Stadium located, a venue famous for hosting World Cup finals? ').lower()
if answer.lower() == 'mumbai':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('Who holds the record for the most runs scored in a single edition of the Indian Premier League (IPL)? ').lower()
if answer.lower() == 'virat kohli':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('Which Indian cricketer is known as the "Captain Cool" for his calm and composed leadership style? ').lower()
if answer.lower() == 'mahendra singh dhoni':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('Who was the first Indian cricketer to score a century in T20 International cricket? ').lower()
if answer.lower() == 'suresh raina':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

answer = input('In which year did India achieve the historic Test series victory in Australia for the first time? ').lower()
if answer == '2018-19':
    score += 1
    print("Correct! Your score is " + str(score))
else:
    print('Incorrect')

print('You got ' + str(score) + ' questions correct')
print('You got ' + str((score / 10) * 100) + '%.')  # Fixed the denominator in the percentage calculation
