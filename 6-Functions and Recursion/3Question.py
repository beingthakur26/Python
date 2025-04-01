# Question 1.
# WAF to print the length of a list. (list is the parameter)

cities = ["delhi", "kolkata", "mumbai", "varanasi"]
heroes = ["ironman", "superman", "thor", "hulk"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)
 


# Question 2.
# WAF to print the elements of a list in asingle line. (list is the parameter)

cities = ["delhi", "kolkata", "mumbai", "varanasi"]

def print_len(list):
    for item in list :
        print(item, end=" ")

print_len(cities)



# Question 3. 
# WAF to find the factorial of n. (n is the parameter)

n =int(input("Enter a n : "))

def cal_fact(n) :
    fact = 1 
    for i in range(1, n+1) :
        fact *= i
    return fact
fact = cal_fact(n)
print(fact)


    
# Question 4. 
# WAF to convert USD to INR. 

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD = ", inr_val, "INR = ")
converter(10)
    # OR 
USD = int(input("Enter USD : "))
def con(USD):
     inr = USD * 83 
     return inr
inr = con(USD)
print(inr)
