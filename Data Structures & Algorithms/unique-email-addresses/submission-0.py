class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        seen = set()
        for email in emails:
            localname, domainname = email.split("@")
            
            if '+' in localname: 
                localname = "".join(localname.split('+')[0])
                
            if '.' in localname:
                localname = "".join(localname.split('.'))
                
            seen.add(localname + '@' + domainname)
        return len(seen)