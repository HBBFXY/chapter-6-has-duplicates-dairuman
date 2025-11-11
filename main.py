# 在这个文件中编写代码
def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
def has_duplicates(lst):
    # 创建一个集合，集合会自动去除重复元素
    unique_elements = set(lst)
    # 如果原列表长度大于集合长度，说明有重复元素
    return len(lst) != len(unique_elements)

# 测试函数
test_lists = [
    [1, 2, 3, 4, 5],  # 无重复
    [1, 2, 2, 3, 4],  # 有重复
    ["a", "b", "c", "a"],  # 有重复
    []  # 空列表
]

for lst in test_lists:
    if has_duplicates(lst):
        print(f"列表 {lst} 包含重复元素，返回 True")
    else:
        print(f"列表 {lst} 不包含重复元素，返回 False")
   

# 主程序 - 测试函数
if __name__ == "__main__":
    # 学生需要提供测试用例
    test_cases = [
        [1, 2, 3],          # 无重复
        [1, 2, 2],          # 有重复
        ["a", "b", "a"],    # 字符串重复
        []                   # 空列表
    ]
    
    # 测试每个用例，编写具体测试代码
