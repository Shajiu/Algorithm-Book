# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 12:56
# @Author  : Shajiu
# @FileName: ReverseSentence.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，
    有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的
    顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""
class Solution:
    def ReverseSentence(self,s):
        s=[v for v in s.split(" ")]
        s.reverse()
        s=' '.join(s)
        return s

if __name__ == '__main__':
    result=Solution()
    print(result.ReverseSentence("student. a am I"))