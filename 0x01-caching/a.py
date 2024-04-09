import time
colors = {
"monday" : "Blue",
"Tuesday" :" Red",
"Wednessday" : "Yellow",
"Thursday" : "Green",
"Friday": "Purple",
"Saturday": "Brown",
"Sunday" : "Gold"
}
while(True):
    day = input("Day of the week>>>")
    for key, value in colors.items():
        if key == day:
            print("i am Thinking.... ")
            time.sleep(2)
            print("Your color for the day is ", colors[key])
        