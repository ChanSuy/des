# 평문 문자열
# 평문 비트열
# 초기순열 후 비트열
# 왼쪽,오른쪽 32bit

# 1) 평문 64비트 단위 패딩
#     -첫자리 1 나머지 0으로 패딩해서 채우기
#     -문자열 길이 8글자 모드연산을 통해 패딩여부 판단
# 2) 초기순열 표 만들기
#     -초기순열 표 하나씩 뽑아서 평문열(비트로 64개 표현한)에서 인덱싱함
# 3) 순열에 대응할 때 순열 값 다 0이라고 생각하고 and연산한 뒤 결과를 해당 인덱스에 저장하기
class FristPermutation: #초기 순열 함수

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
            print('>>>',end='')
            for j in range(len(binPlain[i])):
                print(binPlain[i][j],end=' ')
            print()

    def changeBit(string): #문자열 평문을 비트열로 표현하는 함수
        binPlain=[] #문자하나씩 리스트로 저장하는 2차원리스트
        new=[] #일시적으로 한문자를 비트열로 저장하여 사용할 빈 리스트
        for i in string: #평문 
            bit=bin(ord(i))[2:]
            bit='0'*(8-len(bit))+bit
            new.append(bit)
            if len(new)==8:
                binPlain.append(new)
                new=[]
        return binPlain

    def fristPermutationMapping(self,binPlain): #초기순열 표를 가져와서 매핑하는 함수 인자값 binPlain
        fristPermutation=self.fristPermutationGraph()
        binPlain_str='' #빈 문자열(2차원 리스트->문자열 한줄로 나열할 문자열)
        binPlain_change='' #빈 문자열(binPlain_str을 받아 초기순열하는 결과를 나열할 문자열)
        fristPermutationList=[] #초기 순열 결과 저장할 리스트
        new=[] #2차원 리스트 만들기위한 임시 리스트 changeBit함수의 것과 같다.
        bit=''
        for i in range(len(binPlain)): #2차원 리스트 문자열로 변환
            for j in range(len(binPlain[i])):
                binPlain_str+=binPlain[i][j]
        
        for i in fristPermutation: #초기순열표(인덱스가 있는)를 참고하여 재배치
            binPlain_change+=binPlain_str[i-1]

        for i in binPlain_change: #다시 2차원 리스트 변환
            bit+=i #001010.....으로 나열된 문자열에서 1개씩 빼서 저장
            if len(bit)==8:
                new.append(bit)
                bit=''
            if len(new)==8:
                fristPermutationList.append(new)
                new=[]
        return fristPermutationList #[['000...','000..',....]]의 형태 

    def fristPermutationGraph(): #초기순열표 생성
        even = [] #짝수
        odd = [] #홀수
        for i in range(8,1,-2): #짝수 숫자 넣기
            for j in range(8):
                even.append(i+j*8)
        for i in range(7,0,-2): #홀수 숫자 넣기
            for j in range(8):
                odd.append(i+8*j)
        
        even.reverse() #32bit크기 뒤집기(짝수)
        odd.reverse() #32bit 크기 뒤집기(홀수)
        
        fristPermutation=[] #32bit씩 쪼갠 홀 짝 더해서 하나의 리스트에 넣기
        fristPermutation=even+odd

        return fristPermutation

    def paddingPlain(Plain): #평문 패딩
        if len(Plain)%8!=0: #64비트 즉, 8문자단위가 아니면
            Plain+=chr(128) #0b10000000을 추가한 뒤
            while len(Plain)%8!=0: #0b00000000추가
                Plain+=chr(0)
        return Plain

    def extendPermutation(fristPermutationResult): #32비트씩 나눠진 2차원 리스트를 받아 오른쪽32비트만 인덱싱하여 확장 순열하는 함수
        extendPermutationGraph=[]
        emptyStr=''
        emptyList=[]
        extendPermutationResult=[]
        bit=''

        for i in range(8): #확장 순열 만드는 알고리즘
            for j in range(6):
                value=(31+4*i+j)%32 #인덱스라 생각하고 표에 -1씩 한 뒤 식 적용시 맞음
                extendPermutationGraph.append(value)
        fristRightPermutation="".join(fristPermutationResult[0])
        for i in extendPermutationGraph: #확장 순열 인덱싱하여 비트열 재배치
            emptyStr+=fristRightPermutation[32:][i]

        for i in emptyStr: #재배치한 비트열 2차원 리스트로 적용(display 메소드 사용하기 위함)
            bit+=i
            if len(bit)%8==0:
                emptyList.append(bit)
                bit=''
        extendPermutationResult.append(emptyList)
        return extendPermutationResult #확장 순열 결과 2차원 리스트로 출력
