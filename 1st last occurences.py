        first_occurrence = {}
        last_occurrence = {}
        
        for i in range(n):
            if s[i] not in first_occurrence:
                first_occurrence[s[i]] = i
            last_occurrence[s[i]] = i

or simply


first_occurrence = {ch: s.find(ch) for ch in set(s)}
last_occurrence = {ch: s.rfind(ch) for ch in set(s)}
