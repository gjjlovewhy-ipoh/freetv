# -*- coding: utf-8 -*-
import requests

# 新地址
SOURCE_URL = "https://t.freetv.fun/m3u/china_original.txt"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def main():
    try:
        resp = requests.get(SOURCE_URL, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        lines = resp.text.strip().splitlines()

        m3u_out = "#EXTM3U\n"
        txt_out = "===== 直播源列表 =====\n\n"
        genre = "央视/卫视"

        for line in lines:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#EXTM3U"):
                continue
            if line.startswith("#EXTINF"):
                current_inf = line
            elif line.startswith("http"):
                # 加入 genre 分组
                new_inf = current_inf.replace("#EXTINF:-1,", f'#EXTINF:-1,genre="{genre}",')
                m3u_out += f"{new_inf}\n{line}\n"
                txt_out += f"{new_inf}\n{line}\n\n"

        # 导出两个独立文件
        with open("live.m3u", "w", encoding="utf-8") as f:
            f.write(m3u_out)
        with open("live.txt", "w", encoding="utf-8") as f:
            f.write(txt_out)

        print("✅ 读取成功，已生成 live.m3u + live.txt")

    except Exception as e:
        print(f"❌ 读取失败：{e}")

if __name__ == "__main__":
    main()
