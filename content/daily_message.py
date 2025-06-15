# content/daily_message.py
from content.level_rules import determine_risk_level

def generate_daily_message():
    # 模擬資料：你未來可替換成 GPT 自動摘要或 NewsAPI 抓取內容
    news_title = "共軍夜間實彈軍演接近24海浬，美艦同步部署東側海域"
    keywords = ["軍演靠近", "航母", "封鎖"]
    risk = determine_risk_level(keywords)

    if risk == "🟨 黃燈":
        advice = "🔸 整備72小時包，檢查證件與奶粉備品"
    elif risk == "🟧 橘燈":
        advice = "🔸 準備撤離演練，與孩子練習穿緊急鞋與逃生故事"
    else:
        advice = "🔸 若有票或機會，考慮離島或北撤；若無則備好家中避難物資"

    message = f"""🛎️【今日台海快訊】
📰 {news_title}
{risk}

📦 家庭避難建議：
{advice}

🔗 詳情：https://news.example.com/sample
"""
    return message
