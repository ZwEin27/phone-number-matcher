import en


for i in range(100000):
    en.spelling.correct('th0usand')

# 1 for 1.9s
# 100 for 2s
# 1000 for 2.1s
# 10000 for 3.9s
# 100000 for 21.6s