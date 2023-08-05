import time
import numpy as np
import pandas as pd

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    #greeting
    print(("\n"*3)+("Well, hello darling! Don't you look gorgeous, good God!\nI suppose you want me to tell you about this bikeshare data? Let's get started."))
    
    #ask user input for city to select proper csv
    while True:
        city = input('\nDo you want to see data for Chicago, New York, or Washington? \n').title()

        if city == "Chicago":
            print('\nIt really is windy there. Let me pull Chicago up for you.\n')
            break
        elif city == 'Washington':
            print('\nFeeling patriotic? Curious about alien biking patterns? Let me pull Washington up for you.\n')
            break
        elif city == 'New York':
            print('\nExcellent choice! Very stylish! Let me pull New York City up for you.\n')
            break
        else:
            print('\nWhoops, you\'ll need to enter one of the cities listed.\n')
    
    #user input to determine if month filter wanted
    while True:
        mfilter = input('Would you like to see the data filtered by month? Type Yes or No: \n').lower()

        if mfilter == 'yes':
            print("\nBut of course! Let's take a look at the calendar.")
            break
        elif mfilter == 'no':
            month = 'any month'
            print("\nOf course, all six, no months excluded. We all know there are only six months in a year.\n")
            break
        else:
            print("\nWhoops, you'll need to let me know if I'm filtering by month.Type 'Yes' or 'No'. \n")
    
    #user input to determine month filter
    month_commentary = {
        'Jan': 
            {'name': 'January',
            'message': "January? Chilly. Did people really rent bikes in January?"},
        'Feb': 
            {'name': 'February',
            'message': "February? Romantic. None of these bicycles were built for two. It was too much data."},
        'Mar': 
            {'name': 'March',
            'message': "March? Feeling green? Do you think people were biking under the influence?"},
        'Apr': 
            {'name': 'April',
            'message': "April? Biking in the showers? ...why not? Let's see what we got."},
        'May': 
            {'name': 'May',
            'message': "May? Look at all the flowers! Don't you have great taste."},
        'Jun': 
            {'name': 'June',
            'message': "June? I bet the weather was splendid for biking."}}

    if mfilter == 'yes':
        while True:
            month = input("\nWhich month are you curious about? We have Jan through Jun. \nEnter the abbreviated month below by entering the first 3 letters of the month. For example, January would be 'Jan', February would be 'Feb', etc.: \n").title()

            if month in month_commentary:
                print("\n" + month_commentary[month]['message'] + "\n")
                month = month_commentary[month]['name']
                break
            else:
                print("\nWhoops, you'll need to enter a month between Jan and Jun.\n")
    
    #user input to determine if day filter wanted
    while True:
        dfilter = input("\nWould you like to see the data filtered by the day of the week? Type 'Yes' or 'No': \n").lower()
    
        if dfilter == 'yes':
            print("\nMarvelous, darling. Let's narrow it down.\n")
            break
        elif dfilter == 'no':
            print("\nI mean, all the days are good days, right?\n")
            day='any day'
            break
        else:
            print("\nWhoops, you'll need to let me know if I'm filtering by day. Type 'Yes' or 'No'. \n")
    
        #user input to determine day filter
    if dfilter == 'yes':
        while True:
            day = input("\nWhich day of the week are you interested in? Type Mon, Tue, Wed, Thu, Fri, Sat or Sun: \n").title()

            if day == 'Mon':
                print("\nMonday? Are you sure? Well, okay.\n")
                day = 'Monday'
                break
            elif day == 'Tue':
                print("\nTuesday, a day for doing. Is there something remarkable about Tuesday?\n")
                day = 'Tuesday'
                break
            elif day == 'Wed':
                print("\nHump day! Let's see.\n")
                day = 'Wednesday'
                break
            elif day == 'Thu':
                print("\nI hear it's a thirsty day. Let's find out if it drove people to bike.\n")
                day = 'Thursday'
                break
            elif day == 'Fri':
                print("\nTGIF! Surely people were biking into Friday nights full of adventure.\n")
                day = 'Friday'
                break
            elif day == 'Sat':
                print("\nSaturday, in the park. Don't ask about the 4th of July, we only went to June.\n")
                day = 'Saturday'
                break
            elif day == 'Sun':
                print("\nSunday funday or Sunday scaries? Regardless, there was biking.\n")
                day = 'Sunday'
                break
            else:
                print("\nWhoops, you have to let me know what day I'm looking for. Type Mon, Tue, Wed, Thu, Fri, Sat or Sun: \n")

    #ux responsiveness message to display input
    print('-'*40+'\n')
    print("\nSo I'm looking for rides on {}, and in {}, in the city of {}. Let me get you some statistics, you fabulous thing.\n".format(day,month,city))
    print('-'*40+'\n')

    #format variables for use in later functions
    while True:
        if month == 'any month':
            month = 'all'
            break
        else:
            month = month.lower()
            break
    
    if city == 'New York':
        city = 'new_york_city'
    else:
        city = city.lower()
    
    #format day entry to integer
    day_dict = {
        'any day': 'all',
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6}

    if day in day_dict:
        day = day_dict[day]
    else:
        print('Day error!')
           

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv('{}.csv'.format(city))
    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['End Time'] = pd.to_datetime(df['End Time'])
  

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    
    #add columns for trip time and most common trip
    df['Combo Trip'] = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    df['Travel_Time'] = (df['End Time'] - df['Start Time'])
 
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nWhat were the most frequent times of travel?\n')
    start_time = time.time()

    # display the most common month
    # format for readability
    raw_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = (months[raw_month-1]).title()

    # display the most common day of week
    # format for readability
    raw_day = df['day_of_week'].mode()[0]
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    common_day = (days[raw_day])

    # display the most common start hour
    # format for readability
    raw_hour = df ['hour'].mode()[0]
    if raw_hour == 0:
        common_hour = ("12 am")
    elif raw_hour > 0 and raw_hour < 12:
        common_hour = ("{} am".format(raw_hour))
    elif raw_hour > 12:
        pm_hour = raw_hour - 12
        common_hour = ("{} pm".format(pm_hour))
    elif raw_hour == 12:
        common_hour = ("{} pm".format(raw_hour))
    

    print("In this period:\nThe most common month of travel was: {}\nThe most common day of the week for travel was: {}\nThe most common hour to start a trip was: {}".format(common_month,common_day,common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nHow much time did people spend biking?')
    start_time = time.time()

    # display total travel time
    
    tot_trav_time = df['Travel_Time'].sum()

    # display mean travel time
    m_trav_time = df['Travel_Time'].mean()

    print("In this period:\nThe total travel time was: {}\nThe average travel time was: {}".format(tot_trav_time, m_trav_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nWhat were the most popular stations? What was the most popular trip?\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df ['Start Station'].mode()[0]

    # display most commonly used end station
    common_end = df ['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    common_combo = df ['Combo Trip'].mode()[0]

    print("In this period:\nThe most common start station was: {}\nThe most common end station was: {}\nThe most common trip between stations was: {}".format(common_start, common_end, common_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nWho comprised our user base?\n')
    # find age related info, handle errors
    while True:
        try:
            start_time = time.time()
            youngest =  int(df['Birth Year'].max())
            oldest =  int(df['Birth Year'].min())
            birthiest =  int(df['Birth Year'].mode())
            print("In this period:\nThe youngest user was born in: {}\nThe oldest user was born in: {}\nThe most users were born in: {}".format(youngest,oldest,birthiest))
        except: KeyError
        break
    print('In terms of who our users were in this period:\n')
        # Display counts of user types
        # find subscription level related info, handle errors
    users = df.groupby(['User Type']).count()
    ucounts = users['Start Time']
    print(ucounts.to_string()+'\n')
   
    # Display counts of gender
    # find gender related info, handle errors
    while True:
            try: 
                genders = df.groupby(['Gender']).count()
                counts = genders['Start Time']
                print(counts.to_string()+'\n')
            except: KeyError
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_dig(df):
    """This function requests user input. If yes, user gets 5 rows of data from the dataframe at a time. The user will be prompted 
    again to see if they want 5 more rows of data until they input no or there is no more data to display"""
    view = 0
    rows = 5

    while view < len(df):
        try:
            more_data_plz = input("\n\nNow wasn't that fun? Would you like to see 5 rows of out of context data?\n").lower()

            if more_data_plz == "yes":
                print(df[view:view+rows])
                view += rows
            else:
                break
        except:
            print("Sorry! All out of info. Aren't you just a curious little person?")
            break       

def main():
    """Main body of program"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_dig(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
      
if __name__ == "__main__":
	main()
