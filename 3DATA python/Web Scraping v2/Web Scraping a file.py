from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

data1 = soup.findAll("div", class_="calendar-single")


for data2 in data1:
    calendar_date_day = data2.find("span", class_="calendar-single__date__day")
    calendar_date_month = data2.find("span", class_="calendar-single__date__month")
    calendar_content = data2.find("h3", class_="h5-heading")
    calendar_time_from_time = data2.find("span", class_="calendar-single__time__from-time")
    calendar_time_to_time = data2.find("span", class_="calendar-single__time__to-time")
    calendar_time_to_date1 = data2.find("span", class_="calendar-single__time__to-date1")
    calendar_time_to_date2 = data2.find("span", class_="calendar-single__time__to-date2")

    calendar_content = calendar_content.text.replace("ðŸ˜Ž", ":)").replace("Ã¥", "å").replace("Ã¸", "ø").replace("Ã¦", "æ")

    print(calendar_date_day.text)
    print(calendar_date_month.text)
    print(calendar_content)
    if calendar_time_from_time and calendar_time_to_time:
        print(calendar_time_from_time.text)
        print(calendar_time_to_time.text)
    if calendar_time_to_date1:
        print(calendar_time_to_date1.text)
        print(calendar_time_to_date2.text)
