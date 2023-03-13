# 学习单位 ：广东工业大学
# 学   生 ：凌嘉辉
# 开发时间 ：2023/1/5 18:30

# 二叉树
class Tree(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # 以中序遍历，以中缀表达式存储再expression列表中
    def inorder(self, root, expression1):
        if root:
            if root.data in ['+', '-', '*', '/', '^']:
                expression1.append('(')
            self.inorder(root.left, expression1)
            expression1.append(root.data)
            self.inorder(root.right, expression1)
            if root.data in ['+', '-', '*', '/', '^']:
                expression1.append(')')


class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 进栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()


def assign_getvalue(expression2):
    expression_copy = " ".join(map(str, expression2))
    matrix = ['hello' for i in range(26)]
    for i in range(len(expression2)):
        if 'a' <= expression2[i] <= 'z':
            if matrix[ord(expression2[i]) - ord('a')] == 'hello':
                temp = expression2[i]
                expression2[i] = input(f'please input the value of {temp}:')
                matrix[ord(temp) - ord('a')] = expression2[i]
            else:
                expression2[i] = matrix[ord(expression2[i]) - ord('a')]
        elif expression2[i] == '^':
            expression2[i] = '**'
    expression_str = " ".join(map(str, expression2))
    print(expression_copy.replace(' ', ''), '=', end=' ')
    print(eval(expression_str), '\n')


if __name__ == '__main__':
    print('广东工业大学大学-----先进制造学院-----21级计科6-----3121009321-----凌嘉辉')
    tree = Tree()
    stack = Stack()
    answer = 'y'
    while answer == 'y':
        # 输入前缀表达式，各数据项之间用空格隔开
        s = list(input('Please enter a prefix expression, with each data separated by a space:').split())
        index = len(s) - 1
        # 据上述所说，从右往左遍历
        while index >= 0:
            ch = s[index]
            # ch是变量或者常数，直接进栈
            if ch not in ['+', '-', '*', '/', '^']:
                tree = Tree(data=ch)
                stack.push(tree)
                index -= 1
            # ch是操作符，则将栈顶两个元素弹出栈外并作相应运算，再将结果压入栈内
            else:
                lchild = stack.pop()
                rchild = stack.pop()
                tree = Tree(data=ch, left=lchild, right=rchild)
                stack.push(tree)
                index -= 1
        print('Input is Over')
        expression = []
        # 以中序遍历，以中缀表达式存储再expression列表中
        tree.inorder(tree, expression)
        # 对表达式进行赋值并且求出表达式的值
        assign_getvalue(expression)
        print('广东工业大学大学-----先进制造学院-----21级计科6-----3121009321-----凌嘉辉')
        answer = input('是否继续进行计算(y/n)：')
