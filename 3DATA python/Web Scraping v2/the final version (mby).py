from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

data1 = soup.findAll("div", class_="calendar-single")

when = []
content = []
time = []
date = []

for data2 in data1:
    calendar_date_day = data2.find("span", class_="calendar-single__date__day".strip())
    calendar_date_month = data2.find("span", class_="calendar-single__date__month")
    calendar_content = data2.find("h3", class_="h5-heading")
    calendar_time_from_time = data2.find("span", class_="calendar-single__time__from-time")
    calendar_time_to_time = data2.find("span", class_="calendar-single__time__to-time")
    calendar_time_to_date1 = data2.find("span", class_="calendar-single__time__to-date1")
    calendar_time_to_date2 = data2.find("span", class_="calendar-single__time__to-date2")

    calendar_date_day = calendar_date_day.text
    calendar_date_month = calendar_date_month.text
    calendar_content = calendar_content.text
    if calendar_time_from_time:
        calendar_time_from_time = calendar_time_from_time.text
        calendar_time_to_time = calendar_time_to_time.text
    if calendar_time_to_date1:
        calendar_time_to_date1 = calendar_time_to_date1.text
        calendar_time_to_date2 = calendar_time_to_date2.text

    calendar_content = calendar_content.replace("ðŸ˜Ž", ":)").replace("Ã¥", "å").replace("Ã¸", "ø").replace("Ã¦", "æ")

    when.append(f"{calendar_date_day} {calendar_date_month}")
    content.append(calendar_content)
    time.append(f"{calendar_time_from_time} - {calendar_time_to_time}")
    date.append(f"{calendar_time_to_date1} - {calendar_time_to_date2}")

amount = len(when)

stuff_that_will_happen = []

for x in range(amount):
    stuff_that_will_happen.append((when[x], content[x], time[x], date[x]))

for x in range(amount):
    print(stuff_that_will_happen[x])
