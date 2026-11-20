import json, re, urllib.request, datetime
url = ("https://api.open-meteo.com/v1/forecast?latitude=40.22&longitude=-74.74"
       "&current=temperature_2m,weather_code&daily=temperature_2m_max,temperature_2m_min"
       "&temperature_unit=fahrenheit&timezone=America%2FNew_York&forecast_days=1")
d = json.load(urllib.request.urlopen(url, timeout=30))
c = d["current"]["weather_code"]
if c == 0: icon, cond = "sunny", "Sunny"
elif c <= 2: icon, cond = "partly", "Partly Cloudy"
elif c == 3: icon, cond = "cloudy", "Cloudy"
elif c <= 48: icon, cond = "fog", "Foggy"
elif c <= 67 or 80 <= c <= 82: icon, cond = "rain", "Rain"
elif c <= 77 or c in (85, 86): icon, cond = "snow", "Snow"
else: icon, cond = "storm", "Storms"
wx = {"place": "New Jersey", "temp": round(d["current"]["temperature_2m"]), "cond": cond, "icon": icon,
      "hi": round(d["daily"]["temperature_2m_max"][0]), "lo": round(d["daily"]["temperature_2m_min"][0]),
      "updated": d["daily"]["time"][0]}
s = open("index.html", encoding="utf-8").read()
s2 = re.sub(r"^const WX = \{.*\};$", "const WX = " + json.dumps(wx, ensure_ascii=False) + ";", s, count=1, flags=re.M)
open("index.html", "w", encoding="utf-8").write(s2)
print(wx)
