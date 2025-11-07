# Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

response = int(input("Enter API Response as 200 or 404 :"))
if response == 200:
    print("Passed API Request")
elif response == 404:
    print("Failed API Request")
else:
    print("Invalid Response")