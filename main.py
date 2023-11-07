x=int(input("What is the error code?"))
match x:
    case 400:
        print("It represents the Bad Request")
    case 401:
        print("It represents the Unauthorized")
    case 402:
        print("It represents the Payment Required")
    case 403:
        print("It represents the Forbidden")
    case 404:
        print("It represents the Not Found")

