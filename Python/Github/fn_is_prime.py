import requests
def is_prime(num):
    if str(num).isdigit() is False:
        return num + ' is NOT Prime'
    else: num = int(num)

    if num >1:
        for i in range(2, num):
            if (num%i)==0:
                print(num, ' is NOT Prime')
                break
        else:
            return(num, ' is A Prime')
    else:
        return(num, ' is NOT Prime')



print(is_prime('3'))


#print(requests.get('https://www.danb.com'))