#30.     Calendar
#Get a date (mon/day/year) from user. 
#Print exact the week of dates (Sun to Sat). 
#ex) input: 2/20/2001 if the day isWednesday
#output: Sunday 2/17/2001 
#Monday 2/18/2001 
#Tuesday 2/19/2001 
#Wednesday 2/20/2001 
#Thursday 2/21/2001 
#Friday 2/22/2001 
#Saturday 2/23/2002
#        



#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int NUMBEROFDAYS[] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

bool isLeapYear(int year)
{
    return (year%400 == 0)||(year%4 == 0 && year%100 != 0);
}

int numberOfDaysInMonthAndYear(int month, int year)
{
    if(isLeapYear(year) && month == 2)
    {
        return 29;
    }
    else return NUMBEROFDAYS[month];
}

void printDay(int day, int month, int year, int whichDay)
{
    cout<<day<<", "<<month<<", "<<year<<" is "<<whichDay<<endl;
}

void findWeek(int day, int month, int year, int whichDay)
{
    for( int i = whichDay ; i > 0 ; -- i )
    {
        if(day == 1)
        {
            if(month == 1)
            {
                year--;
                month = 12;
                day = numberOfDaysInMonthAndYear(month, year);
            }
            else month--;
        }
        else day--;
    }
    
    for(int i = 0; i < 7 ; ++ i)
    {
        printDay(day, month, year, i);
        day++;
        if(day > numberOfDaysInMonthAndYear(month, year) )
        {
            day = 1;
            month++;
            if(month > 12)
            {
                month = 1;
                year++;
            }
        }
    }
    
}


int main (int argc, const char * argv[])
{
    findWeek(1,1,2001,3);
    return 0;
}
