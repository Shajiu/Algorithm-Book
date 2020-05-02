# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 20:13
# @Author  : Shajiu
# @FileName: Array_subset.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    输入一个非空整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
class Solution:
    def VerifySquenceOfBST(self,sequence):
        length=len(sequence)
        if length==0:
            return False
        if length==1:
            return True
        root=sequence[-1]
        left=0
        while sequence[left]<root:
            left+=1
        for j in range(left,length-1):
            if sequence[j]<root:
                return False
        return self.VerifySquenceOfBST(sequence[:left]) or self.VerifySquenceOfBST(sequence[left:length-1])