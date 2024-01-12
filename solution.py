"""
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.
Your task is to determine the following:
1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.(ie: last day will be absent)
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:
for 5 days: 14/29
for 10 days: 372/773
"""
"""
idea: P, A 
2 ^ N = combination of the number of ways to attend classes over N days
consicutive four A = AAAA means that you won't be able to attend your graduation ceremony.'
Nth day is A then you miss your graduation ceremony.
"""
ans = 0
last_day_miss = 0


def probability_of_attendance(prev_attendance, curr_attendance, missing_attendance, number_of_days, attendance, miss_flag):
    global ans
    global last_day_miss

    if missing_attendance >= 4:
        miss_flag = True
        return

    if number_of_days == attendance:
        attendance_str = prev_attendance + curr_attendance
        if miss_flag:
            return
        if curr_attendance == 'A':
            last_day_miss += 1
        ans += 1
        return

    probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="P",
                              missing_attendance=0, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
    probability_of_attendance(prev_attendance=prev_attendance+curr_attendance, curr_attendance="A",
                              missing_attendance=missing_attendance+1, number_of_days=number_of_days+1, attendance=attendance, miss_flag=miss_flag)
    return


# probability_of_attendance("", "", 0, 0, 5, False)
# print(str(last_day_miss)+'/'+str(ans))
probability_of_attendance("", "", 0, 0, 10, False)
print(str(last_day_miss)+'/'+str(ans))
