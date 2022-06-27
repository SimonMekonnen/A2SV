class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
       
        mylist = list(s.split(" "))
        count = [0]*len(mylist)
        for i in mylist:
            count[int(i[-1])-1] = i
        sent = ""
        for i in count:
            sent+=i
        listsent = list(sent)
        for i in range(len(listsent)):
            if listsent[i].isnumeric():
                listsent[i] = " "
        listsent.pop()
        ho =""
        for i in listsent:
            ho+=i
        return ho
     