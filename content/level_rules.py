# content/level_rules.py

def determine_risk_level(keywords):
    score = 0
    red_triggers = ["12海浬", "核武", "總動員", "交火", "導彈", "進犯"]
    orange_triggers = ["24海浬", "軍演靠近", "航母", "封鎖", "演習"]
    yellow_triggers = ["軍演", "共機", "空域異常", "軍事評論"]

    for word in keywords:
        if word in red_triggers:
            score += 5
        elif word in orange_triggers:
            score += 3
        elif word in yellow_triggers:
            score += 1

    if score >= 7:
        return "🔴 紅燈"
    elif score >= 4:
        return "🟧 橘燈"
    else:
        return "🟨 黃燈"
