import urllib.request
from datetime import datetime
import pytz

UPSTREAM_URL = "https://live.fanmingming.com/tv/m3u/ipv6.m3u" 
LOCAL_FILE = "tv.m3u"

def update_m3u():
    try:
        req = urllib.request.Request(UPSTREAM_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8')
            
        if "#EXTM3U" in content:
            tz = pytz.timezone('Asia/Shanghai')
            update_time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
            content = content.replace("#EXTM3U\n", f"#EXTM3U\n#EXTINF:-1, [更新时间]\nhttp://127.0.0.1/fake.m3u8\n#EXTINF:-1, {update_time}\nhttp://127.0.0.1/fake.m3u8\n")

            with open(LOCAL_FILE, "w", encoding="utf-8") as f:
                f.write(content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_m3u()
