        first_occurrence = {}
        last_occurrence = {}
        
        for i in range(n):
            if s[i] not in first_occurrence:
                first_occurrence[s[i]] = i
            last_occurrence[s[i]] = i
