from tkinter import *
from PIL import ImageTk, Image
import requests
from geopy.geocoders import Nominatim

def both():
    global city
    city = enter_city.get()
    update_img()

def update_img():
    # Initialize Nominatim API
    global city
    geolocator = Nominatim(user_agent="MyApp")
    location = geolocator.geocode(str(city))
    lat =  location.latitude
    lon =  location.longitude
    api_key = "3038aaacdd1163cca7c60d50653d3b52"
    base_url = "https://api.openweathermap.org/data/2.5/weather?lat="
    url = base_url + str(lat) + "&lon=" + str(lon) + "&appid="+api_key
    response = requests.get(url).json()

    ####################################################
    icon = response.get("weather")[0].get("icon")
    maindis = response.get("weather")[0].get("description")
    temp = int(int(response.get("main").get("temp"))-273.15)
    wind = response.get("wind").get("speed")
    humidity = response.get("main").get("humidity")

    # open the image using PIL.Image and add a transparent layer
    alpha = Image.new("RGBA", (100, 80), (0, 0, 0, 0))
    img = Image.open(f"weather_icons\\{icon}.png")
    img = Image.alpha_composite(img, alpha)
    root.attributes('-transparentcolor', 'black')
    bg_image = ImageTk.PhotoImage(img)
    #configuring weather icons
    label = Label(root, image=bg_image, bg='black')
    label.grid(row="0",column="0")
    label.configure(image=bg_image)
    label.image = bg_image
    root.configure(bg='black')
    #labeling all info
    print("looping success")
    print(response.get("weather")[0].get("description"))
    print(int(response.get("main").get("temp"))-273.15) #273.15
    print(response.get("wind").get("speed"))
    print(response.get("main").get("humidity"))
    label2 = Label(root,text=f"{maindis}",font=('Helvetica bold', 15))
    label3 = Label(root,text=f"humidity:{humidity} | wind:{wind}",font=('Helvetica bold', 8))
    label4 = Label(root,text=f"{temp}°C",font=('Helvetica bold', 18))
    #making info bg transparent
    label2.configure(bg='black',fg="white")
    label3.configure(bg='black',fg="white")
    label4.configure(bg='black',fg="white")
    #deleting all main menu window labels
    start.destroy()
    enter_city.destroy()
    menu_screen.destroy()
    #displaying all weather content
    label2.grid(row="1",column="0",columnspan=2)
    label3.grid(row="2",column="0",columnspan=2)
    label4.grid(row="0",column="1")
    root.after(900000,update_img) #you can change the update time here which is in milliseconds




root = Tk()
x = (root.winfo_screenwidth())-(163)
y = 2
root.geometry(f"+{x}+{y}")
root.geometry("160x130")
root.attributes('-topmost',False)
#labeling main enter city
menu_screen = Label(root,text="enter place")
enter_city = Entry(root)
start = Button(root,text="start",command=both)
#displaying main content
menu_screen.grid(row=0,column=0,)
enter_city.grid(row=1,column=0)
start.grid(row=2,column=0)

print("out")
root.overrideredirect(True)##########
print("out2")



root.mainloop()
