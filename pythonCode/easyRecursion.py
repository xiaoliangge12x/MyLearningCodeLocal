# Easy Recursion Function to Count Down
def countDown(n):
    print n
    if (n<=1):
        return
    else:
        countDown(n-1)

# Main Function
countDown(10)