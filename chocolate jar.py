# chocolate jar
def cal_cho(jars):
    total_chocolates_A = 0
    for jar in jars:
        chocolates_in_jar = jar
        while chocolates_in_jar > 0:
            
            total_chocolates_A += 1
            chocolates_in_jar -= 1
            if chocolates_in_jar == 0:
                break
            
            chocolates_in_jar -= 1
            if chocolates_in_jar == 0:
                break
            
            chocolates_in_jar -= 1
    return total_chocolates_A


jars = list(map(int, input().split()))
N = int(input())
result = cal_cho(jars)
print(result)




