def solution(numbers):
    # 拆分每个数字组
    split_numbers = [list(map(int, str(num))) for num in numbers]
    
    # 递归生成所有组合
    def generate_combinations(index, current_combination):
        if index == len(split_numbers):
            # 计算当前组合的各位数字之和
            total_sum = sum(current_combination)
            # 判断和是否为偶数
            if total_sum % 2 == 0:
                return 1
            else:
                return 0
        else:
            count = 0
            for num in split_numbers[index]:
                count += generate_combinations(index + 1, current_combination + [num])
            return count
    
    # 从第一个数字组开始生成组合
    return generate_combinations(0, [])

if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([123, 456, 789]) == 14)
    # print(solution([123456789]) == 4)
    # print(solution([14329, 7568]) == 10)