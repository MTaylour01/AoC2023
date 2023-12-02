import os
import requests
import csv

#ok ngl I nicked most of this from Nyaalex so credit to her lol
class AoCHandler():

    def __init__(self, day):
        self.day = day
        #I have never touched requests and cookies before, mother help me I'm scared
        self.session = requests.Session()
        cookies = self.session.cookies
        with open('SECRET_COOKIE') as f:
            secret_cookie = f.read().strip()
        cookies.set('session', secret_cookie, domain='adventofcode.com')


    def get_data(self):
        #Do we already have data? We should probably read from there and not spam AoC lmao
        if os.path.exists(f'Day{self.day}.dat'):
            with open(f'Day{self.day}.dat') as f:
                data = f.read()
        #Get our input from AoC
        else:
            data = self.session.get(f'https://adventofcode.com/2023/day/{self.day}/input').text
            with open(f'Day{self.day}.dat', 'w') as f:
                f.write(data)
        return data


    def submit(self, answer, part, dry=False):
        if not answer:
            return
        #Check if we've already submitted before via our submissions.csv and don't bother submitting if we already have!
        with open('submissions.csv') as submissions:
            csv_reader = csv.DictReader(submissions)
            days = [day for day in csv_reader]
        submission_state = days[self.day-1][f'Part {part}']
        if submission_state == "No Submission":
            if input(f'For part {part}, you got an answer of {answer}. Would you like to submit this? [y/n]:') == 'y':
                data = {
                    'level' : part,
                    'answer' : answer
                }
                if not dry:
                    r_text = self.session.post(f'https://adventofcode.com/2023/day/{self.day}/answer', data=data).text
                else:
                    if submission_state == answer:
                        r_text = 'That\'s the right answer'
                    else:
                        r_text = 'That\'s not the right answer'

                if 'That\'s not the right answer' in r_text:
                    print("That's not the right answer, sorry!")
                elif 'That\'s the right answer' in r_text:
                    print("That's the right answer! Saving to submissions.csv file!")
                    days[self.day-1][f'Part {part}'] = answer
                    with open('submissions.csv', 'w') as f:
                        csv_writer = csv.DictWriter(f, fieldnames=csv_reader.fieldnames)
                        csv_writer.writeheader()
                        csv_writer.writerows(days)
                elif 'You gave an answer too recently' in r_text:
                    print("You gave an answer too recently!")
                
        else:
            if submission_state == str(answer):
                print(f'For part {part}, you got an answer of {answer}. You\'ve already submitted this, but you\'ll be pleased to know you got it right again! Well done!')
            else:
                print(f'For part {part}, you got an answer of {answer}. You\'ve already submitted this, but you\'ve somehow got it wrong this time! The correct answer is {submission_state}')

