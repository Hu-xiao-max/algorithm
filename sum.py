def solution(numbers):
    # Please write your code here
    # 拆分每个数字组
    split_numbers = [list(map(int, str(num))) for num in numbers]
    print(split_numbers)
    return -1

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([123, 456, 789]) == 14)
    # print(solution([123456789]) == 4)
    # print(solution([14329, 7568]) == 10)