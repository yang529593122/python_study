def countMatches( items, ruleKey, ruleValue):
    dic = {"type": 0, "color": 1, "name": 2}
    ans = 0
    for item in items:
        if item[dic[ruleKey]] == ruleValue:
            ans += 1
    return ans


items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "phone"],
    ["phone", "gold", "iphone"]
]
ruleKey = "type"
ruleValue = "phone"

print(countMatches(items, ruleKey, ruleValue))
