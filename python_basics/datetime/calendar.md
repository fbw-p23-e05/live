# Calendar

If you want to set up a personal planner, or maybe practice your coding problem of the day, your friendly garden snake language python has you covered. How so?

Python has a built-in module called the Calendar module which allows you to perform date, month, and calendar-related operations while even letting you manipulate your code for some specific day or month of the year.

The Calendar module in python uses the idealized calendar which is the current Gregorian calendar. It is extended in both directions (past and future) indefinitely. These calendars have the **first day of the week as Monday and the last day of the week as Sunday.**

| Method/Function | Description |
|-----------------|-------------|
| `setfirstweekday()` | This method is used to set the first day of the week. The days of the week are provided in the function as MONDAY, TUESDAY ... SUNDAY for convenience, however, you can also make use of numbers 0 - 6 where 0 is Monday and 6 is Sunday |
| `firstweekday()` | With the use of this method we can get the current weekday that is set as the first day of the week |
| `isleap()` | As the name of the method suggests, it tells us whether a year is leap or not. It returns true if the year is a leap year and false, if not |
| `leapdays()` | This method returns the number of leap years present in a specified range of years given as input. |
| `weekday()` | This method returns the day of the week on a particular date. For example, 15 may 2016 as input to this method will return 6 = sunday |
| `weekheader()` | We can use this method to get a header that contains the weekday names in abbreviated format |
| `monthrange()` | This method returns the weekday of the first day of the month and the number of days in that month as a tuple for any specified year and month given as input |
| `monthcalendar()` | Returns a matrix that represents the calendar of a month where every row is representative of the week, and the days outside the specified month are represented as zeroes |
| `prmonth()` | This method is used to print the calendar of a month with formatting as per user. The user can format the width between two columns and the number of blank lines between rows. |
| `month()` | Returns the calendar of a month in the format of a multiline string |
| `prcal()` | Used to print the calendar of the complete year with options for formatting the output |
| `calendar()` | This method is as we discussed in the beginning of the article, used to print the 3 - column calendar of a year |