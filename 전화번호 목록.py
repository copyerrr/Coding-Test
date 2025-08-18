def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if (phone_book[i] == phone_book[i + 1][:len(phone_book[i])]):
            answer = False
            break   
        

    return answer

# 숫자로 이루어진 문자열 형식은 sort하면 사전순으로 정렬이 된다