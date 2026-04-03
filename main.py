# FILTER 1
words = ["python", "code", "java", "script", "html", "database"]
result1 = list(filter(lambda w: len(w) > 4 and 'e' not in w, words))

# FILTER 2
roy = [5, 12, 7, 24, 9, 16, 3, 18, 11]
result2 = list(filter(lambda x: x % 2 == 0 and x > 10, roy))

# FILTER 3
sites = ["site.com", "test.org", "blog.uz", "info.org", "web.net"]
result3 = list(filter(lambda s: s.endswith(".org"), sites))

# FILTER 4
nums = [12, 8, 24, 15, 36, 9, 48, 20, 72]
result4 = list(filter(lambda x: x % 4 == 0 and x % 6 == 0, nums))

# FILTER 5
nums2 = [25, 13, 45, 102, 305, 77, 85, 100, 95]
result5 = list(filter(lambda x: str(x).endswith('5'), nums2))

# FILTER 6
words2 = ["salom", "dunyo", "kitob", "oquvchi", "uy", "maktab"]
result6 = list(filter(lambda w: len(w) % 2 != 0, words2))

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
