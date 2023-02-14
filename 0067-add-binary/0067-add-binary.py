class Solution:
    def addBinary(self, a: str, b: str) -> str:
        end1 = len(a)-1
        end2 = len(b)-1
        carry = 0
        ans = []
        
        while end1>=0 or end2>=0:
            if end1>=0 and end2>=0:
                temp = int(a[end1]) + int(b[end2]) + carry
            if end1>=0 and end2<0:
                temp = int(a[end1]) + carry
            if end1<0 and end2>=0:
                temp = int(b[end2]) + carry
                
            ans.append(str(temp%2))
            carry = temp//2
            
            end1, end2 = end1-1, end2-1
            
        if carry!=0:
            ans.append(str(carry))
        ans.reverse()
        
        return "".join(ans)
        
        
                
                
        