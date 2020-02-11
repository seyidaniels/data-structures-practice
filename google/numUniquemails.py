class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = []
        for email in emails:
            eArray = email.split('@')
            eArray[0] = eArray[0].split('+')[0]
            eArray[0] = eArray[0].replace(".", '')
            r = eArray[0] + '@'+eArray[1]
            if r in results:
                continue
            result.append(r)
        return len(result)
