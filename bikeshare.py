import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input ("\nPlease enter the city that you want to filter(Washington,New York,Chicago)?\n)").lower()
        if city not in ('washington','new york','chicago'):
            print("\nEntered City Is invalid\n Please Enter one of the Cities (Washington,New York,Chicago)")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input ("\nPlease enter the month that you want to filter(January, February, March, April, May, June or type 'all')")
        if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
            print("\nPlease  Enter a valid month")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("\n Please enter a day(Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all')")
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):
            print("\nPlease Enter valid day")
            continue
        else:
            break


    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("Most Common Month:",common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("Most Common Week:",common_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_of_hour = df['hour'].mode()[0]
    print("Most Common Hour:",common_start_of_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("Most Commmon Start Station:",common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("Most Common End Station:",common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    start_stop_station = df.groupby(['Start Time','End Time']).count().idxmax()[1]
    print("Most Frequent Combination of start and end station trip",start_stop_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print("Total Travel Time",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time",mean_travel_time)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nCount of User types: ",user_types)


    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print("\nGender Types: ",gender_types)
    except KeyError:
        print("\n No Data Available")


    # TO DO: Display earliest, most recent, and most common year of birth
    

    try:    
        earliest_birth_year = df['Birth Year'].min()
        print("\nEarliest Birth Year: ",earliest_birth_year)
        
        recent_birth_year = df['Birth Year'].max()
        print("\nRecent Birth Year: ",recent_birth_year)
        
        
        common_birth_year = df['Birth Year'].mode()
        print("\nCommon Birth Year: ",common_birth_year)
        
    except KeyError:
        print("\n No Data Available")
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(df):
    
    row_index = 0

    see_data = input("\nYou like to see the data used to compute the stats? Please write 'yes' or 'no' \n").lower()
    while True:
        if see_data == 'no':
            return
        if see_data == 'yes':
            print(df[row_index: row_index + 5])
            row_index = row_index + 5
        see_data = input("\n Would you like to see five more rows of the data used to compute the stats? Please write 'yes' or 'no' \n").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
