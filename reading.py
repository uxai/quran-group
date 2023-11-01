import csv
import random

def main():
    quran = []
    members = []
    with open('quran.csv') as qurancsv:
        q = csv.reader(qurancsv, delimiter=',')
        for row in q:
            quran.append([row[0], int(row[1])])

    with open('members.csv') as memberscsv:
        m = csv.reader(memberscsv, delimiter=',')
        for row in m:
            members.append([row[0],row[1]])
    print("-------------------")
    print("QURAN READING GROUP")
    print("Names are in alphabetical order, the 4 digits are the last four digits of your phone number. If you would like to change name, let me know.")
    print("What range of suras would you like to assign?")
    lower = int(input("First sura:")) - 1
    upper = int(input("To which sura:")) - 1

    for member in members:
        if member[1] == "Y":
            chapter = random.randint(lower, upper)
            print("------")
            if quran[chapter][1] <= 15:
                print(f"{member[0]}:\nSura {chapter+1} - {quran[chapter][0]}\nVerses: 1 to {quran[chapter][1]}")
            else:
                verses = random.randint(1, quran[chapter][1] - 15)
                print(f"{member[0]}:\nSura {chapter+1} - {quran[chapter][0]}\nVerses: {verses} to {verses + 15}")

if __name__ == "__main__":
    main()