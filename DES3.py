class Operating:

    def toList2D(bitString): #비트열을 2차원 리스트로 만들어 주는 함수
        emptyList=[]
        result=[]
        bit=''
        for i in bitString:
            bit+=i
            if len(bit)==8:
                emptyList.append(bit) 
                bit=''
        result.append(emptyList)
        return result
        

    def operatingExclusive(result1,result2): #2차원 리스트를 받아 XOR 연산을 해주는 함수
        xorResult=[]
        emptyList=[]
        xorValue=''
        bit=''
        result1="".join(result1[0]) #리스트로 구현된 48bit평문과 48bit 라운드 키를 비트열로 변환하는 알고리즘
        result2="".join(result2[0])
        
        if len(result1)==48: #들어온 평문이 48비트인 경우 즉, 첫번째 XOR연산일 경우(확장순열과 키)
            for i in range(len(result1)): #48bit 길이 만큼 i값을 인덱싱하여 둘다 값이 같으면 0 다르면 1
                if result1[i]==result2[i]:
                    xorValue+='0'
                else:
                    xorValue+='1'
            for i in xorValue: #2차원 리스트로 만들어 주는 알고리즘
                bit+=i
                if len(bit)%8==0:
                    emptyList.append(bit)
                    bit=''
            xorResult.append(emptyList)
            return xorResult #2차원 리스트로 된 xor연산 결과
        else: #result1의 길이가 48bit이 아닌 경우 즉, 두번 째 XOR의 경우 (왼평과 pbox결과)
            for i in range(32): #32bit 길이 만큼 i값을 인덱싱하여 둘다 값이 같으면 0 다르면 1
                if result1[i]==result2[i]:
                    xorValue+='0'
                else:
                    xorValue+='1'
            for i in xorValue: #2차원 리스트로 만들어 주는 알고리즘
                bit+=i
                if len(bit)%8==0:
                    emptyList.append(bit)
                    bit=''
            xorResult.append(emptyList)
            return xorResult #2차원 리스트로 된 xor연산 결과            
