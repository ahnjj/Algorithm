class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid = []
        for email in emails:
            # 처리
            ld = email.split('@')
            
            # local
            # .
            if '.' in ld[0]:
                ld[0] = ld[0].replace('.', '')
            
            # +
            if '+' in ld[0]:
                ld[0] = ld[0].split('+')[0]
            
            # 처리 결과가 valid에 없으면 추가
            res = '@'.join(ld)
            
            if res not in valid:
                valid.append(res)
        return len(valid)