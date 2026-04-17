import time
import random
from datetime import datetime
import requests

# Power BI Push URL
# url = "https://api.powerbi.com/beta/1380dd78-5b89-40ee-b046-d89d51024a62/datasets/cbfb994b-8944-4c88-9b8c-88eb957c781f/rows?experience=power-bi&key=2Ccci3x%2B726Ia%2BmsbmCBEFwOI05gt983gfQ7a8vs1oeumJ3N2wCWwIfi91%2FZsp2wVYaFrdTAFEkq%2BVhQycELOA%3D%3D"
# Weather API
def get_weather(city):
    api_key = "7b5223516eb6435080650150260704"
    url_weather = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    try:
        response = requests.get(url_weather, timeout=3).json()
        condition = response["current"]["condition"]["text"].lower()
        temp = response["current"]["temp_c"]

        result = "Sunny"

        if any(word in condition for word in ["rain", "drizzle", "shower", "thunder"]):
            result = "Rain"
        elif temp >= 30:
            result = "Heat"

        # 🔥 ensure variation for Power BI
        return random.choice([result, result, result, "Rain"])
    except Exception as e:
        print("API ERROR:", e)
        return "Error"
# Data
products = {
    "T-Shirt": (700, 400),
    "Jeans": (2000, 1200),
    "Hoodie": (2500, 1500),
    "Saree": (3500, 2200),
    "Smartwatch": (5000, 3500),
    "Power Bank": (1500, 900)
}

cities = ["Chennai", "Bangalore", "Mumbai", "Delhi"]

print("🚀 Live Streaming Started...")

while True:

    city = random.choice(cities)
    weather = get_weather(city)

    product = random.choice(list(products.keys()))
    price, cost_price = products[product]

    # Simple logic based on weather
    if weather == "Rain":
        quantity = random.randint(5, 8)
    elif weather == "Heat":
        quantity = random.randint(1, 3)
    else:
        quantity = random.randint(2, 5)

    final_amount = price * quantity
    profit = (price - cost_price) * quantity

    # Final Data (Clean)
    data = {
        "Order_ID": random.randint(100000, 999999),
        "Time": datetime.now().isoformat(),
        "Product": product,
        "City": city,
        "Weather": weather,
        "Quantity": quantity,
        "Final_Amount": final_amount,
        "Profit": profit
    }

    
    # try:
    #     response = requests.post(url, json=[data])
    #     if response.status_code == 200:
    #         print(f"✅ {city} | {weather} | ₹{final_amount}")
    #     else:
    #         print("❌ Failed:", response.text)
    # except Exception as e:
    #     print("❌ Error:", e)
    print(f"✅ {city} | {weather} | ₹{final_amount}")
    time.sleep(30)
