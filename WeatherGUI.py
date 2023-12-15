import tkinter as tk
#GUI toolkit
import requests
#Used for making HTTP requests
from PIL import Image, ImageTk
#Extensions of PIL

#1
#Set size of window
app = tk.Tk()

HEIGHT = 700
WIDTH = 800
app.resizable(height = 0, width = 0)

def format_response(weather_json):
    try:
        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        final_str = 'Location: %s \nConditions: %s \nTemperature (°C): %s' % (city, conditions, temp)
    except:
        final_str = 'There was a problem retrieving\n that information'
    return final_str


def get_weather(city):
    #Get the data from JSON API
    weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units':'metric'}
    response = requests.get(url, params=params)
    print(response.json())
    weather_json = response.json()

    results['text'] = format_response(response.json())

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    #Get icon showing current weather
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


#2
#Canvas lets us display various graphics on the application. In this case label with background.png
C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
background_image= tk.PhotoImage(file='./background.png')
background_label = tk.Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
#Parent container of other widgets
frame = tk.Frame(app,  bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

#Single-line text-field
textbox = tk.Entry(frame, font=('Comic sans MS', 25))
textbox.place(relwidth=0.65, relheight=1)

#Button
submit = tk.Button(frame, text='Get Weather', font=40, command=lambda: get_weather(textbox.get()))
submit.place(relx=0.7, relheight=1, relwidth=0.3)



lower_frame = tk.Frame(app, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


#Display box
bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=('Comic sans MS', 17), bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)






app.mainloop()