# -*- coding: utf-8 -*-
import requests

# 源地址
url = "https://t.freetv.fun/m3u/china_original.txt"
headers = {"User-Agent":"Mozilla/5.0"}

def main():
    # 下载源内容
    r = requests.get(url, headers=headers, timeout=20)
    r.encoding = "utf-8"
    content = r.text

    # 1 直接保存原文件为 txt
    with open("live.txt", "w", encoding="utf-8") as f:
        f.write(content)

    # 2 生成带 genre 分组的 m3u
    lines = content.splitlines()
    out = "#EXTM3U\n"
    group = "国内直播"

    temp_name = ""
    for line in lines:
        line = line.strip()
        if line.startswith("#EXTINF"):
            temp_name = line
        elif line.startswith("http"):
            out += f'#EXTINF:-1,genre="{group}",{temp_name.split(",")[-1]}\n'
            out += line + "\n"

    with open("live.m3u", "w", encoding="utf-8") as f:
        f.write(out)

    print("✅ 已生成 live.txt 和 live.m3u")

if __name__ == "__main__":
    main()
