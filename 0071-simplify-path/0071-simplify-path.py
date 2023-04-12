class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        stack = []
        for i in folders:
            if i == ".." and not stack:
                continue
            elif i == ".." and stack:
                stack.pop()
            elif i == "."or i == "":
                continue
            else:
                stack.append(i)
        return "/" + "/".join(stack)
                
        