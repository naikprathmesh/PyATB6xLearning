# You want to check whether a web page loads within 3 seconds (performance test condition).
#
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds


load_time = float(input("Enter Load Time: "))
if load_time <= 0:
    print("Invalid Load Time")
elif load_time <= 3.0:
    print ("Performance Test Passed")
else:
    print("Page load too slow")
