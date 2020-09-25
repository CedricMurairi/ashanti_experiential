"""
    The ashanti experiential
    Author: Cedric Murairi
    Users are asked their gender and date of birth, based on what they are provided with a name that would fit them
"""

#these variables map each value of the day to its name value for the two genders
female_names = {0:"Adwoa", 1:"Abeena", 2:"Akwa", 3:"Yaa", 4:"Afia", 5:"Amma", 6:"Akosua"}
male_names = {0:"Kadjo", 1:"Kwabena", 2:"Kwaku", 3:"Yaw", 4:"Kofi", 5:"Kwame", 6:"Kwasi"}

def main():
    gender = input('What is your gender? Male or Female:   ')
    birth_date = input('What is you date of birth? >>>> use 11/12/1930 format:   ')

    #check if the gender value is either male of female, otherwise, it calls main again
    if gender.lower() not in ['male', 'female']:
        print('The gender you entered is invalid')
        return main()

    #calls the function get_day and pass its value and the gender to get_name to get the name and print it
    print(get_name(get_day(birth_date), gender))

#receives a gender and a day to check for that day's name value depending on gender
def get_name(day, gender):
    if gender.lower() == 'female':
        return female_names[day]
    if gender.lower() == 'male':
        return male_names[day]

#get the equivalent day of the week from a provided birth date
#return 0 for monday ... 6 for sunday
def get_day(birth_date):
    birth_date = birth_date.split('/')
    year = int(birth_date[2])
    month = int(birth_date[1])
    day = int(birth_date[0])
    return datetime.datetime(year, month, day).weekday()

if __name__=="__main__":
    main()
