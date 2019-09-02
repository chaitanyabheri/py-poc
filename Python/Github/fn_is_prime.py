import requests
def is_prime(num):

    if __name__ == '__main__':
        def valid_prime(num):
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



        def print_prime(num):

            return('num entered is ',num)


#print(requests.get('https://www.danb.com'))