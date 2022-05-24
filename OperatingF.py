class Operating:
    def display32Bit(binPlain): #비트열 리스트(2차원)를 받아 출력하는 함수
        bit=''
        new = []
        displaybit=[]
        for i in range(len(binPlain)):
            for j in range(len(binPlain[i])):
                bit+=binPlain[i][j]
                if len(bit)==8:
                    new.append(bit)
                    bit=''
                    if len(new)==4:
                        displaybit.append(new)
                        new=[]
        return displaybit

    def displayBit(binPlain): #비트열 리스트를 받아 출력하는 함수
        for i in range(len(binPlain)):
            if i==0 and len(binPlain)>1:
                print('L >>>',end='')
            elif i==1:
                print('R >>>',end='')
            else:
                print(">>>",end='')
            for j in range(len(binPlain[i])):
                print(binPlain[i][j],end=' ')
            print()

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

    def FinalPermutation(saveResult):
        emptyBit=''
        emptyBit="".join(saveResult[-1][0])+"".join(saveResult[-1][1]) #3차원 리스트의 리스트를 참조하여 비트열로 변환
        finalBitResult = ''
        finalListResult = []
        new=[]
        bit=''

        finalPermutation=[40, 8, 48, 16, 56, 24, 64, 32,
                        39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28,
                        35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26,
                        33, 1, 41,  9, 49, 17, 57, 25]
                
        for i in finalPermutation:
            finalBitResult+=emptyBit[i-1]            
        
        for i in finalBitResult:
            bit+=i
            if len(bit)==8:
                finalListResult.append(bit)
                bit=''
        return [finalListResult]

    def changeChr(finalRoundResult):
        for i in finalRoundResult[0]:
            for j in i[-1::-1]:
                if j==1:
                    chnum=
                
                
                