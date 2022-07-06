class Solution:
    def isValid(self, s: str) -> bool:
            list = []
            for i in s:
                    if i=="(":
                        list.append(i)

                    if i == "{":
                        list.append(i)

                    if i == "[":
                        list.append(i)

                    if i == ")":
                        if ("(" not in list or list[len(list)-1]!="("):
                            return False

                        list.pop()

                        # return False
                    if i == "}":
                        if ("{" not in list or list[len(list)-1]!="{"):
                            return False
                        list.pop()


                    if i == "]":
                        if ("[" not in list or list[len(list)-1]!="["):
                            return False

                        list.pop()


            
            if (len(list) == 0):
                return True
            return False
