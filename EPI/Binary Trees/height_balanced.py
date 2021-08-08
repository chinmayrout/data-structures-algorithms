import collections


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height'))

    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(balanced=True, height=-1)
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(tree.right)
        if not right_result:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height)
        return BalancedStatusWithHeight(is_balanced, height)
    return check_balanced(tree).balanced


if __name__ == '__main__':

    '''
    Construct the following tree
                    1
                   / \
                  2   3
                /  \
               4    5
    '''

    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    print(is_balanced_binary_tree(root))
