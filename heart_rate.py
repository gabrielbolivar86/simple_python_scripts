print("-----------------------------------------------------")
print("Hi, I'm here to help you with the slowest and fastest rates necessary to strengthen your heart")
print("When you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes. To find that range, subtract your age from 220. This difference is your maximum heart rate per minute. Your heart simply will not beat faster than this maximum (220 - age). When exercising to strengthen your heart, you should keep your heart rate between 65% and 85% of your heart's maximum. ")
print("-----------------------------------------------------")
max_heart_value = 220
user_age = input ("What is your age?: ")
age = int(user_age)
heart_range = max_heart_value - age
slowest = heart_range * 0.65
fastest = heart_range * 0.85
print('When you exercise to strengthen your heart, you should')
print(f'keep your heart rate between {slowest:.0f} and {fastest:.0f} beats per minute.')