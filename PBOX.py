# P-box순열
class P_Box:
    def pBoxReplace(sBoxResult):  # pbox 순열 하기 위한 함수
        pBox = [
            16,
            7,
            20,
            21,
            29,
            12,
            28,
            17,
            1,
            15,
            23,
            26,
            5,
            18,
            31,
            10,
            2,
            8,
            24,
            14,
            32,
            27,
            3,
            9,
            19,
            13,
            30,
            6,
            22,
            11,
            4,
            25,
        ]
        sBoxResultBit = ""  # sbox 결과를 저장할 문자열
        pBoxResultBit = ""  # pbox pbox결과를 저장할 문자열
        bit = ""
        emptyList = []
        pBoxResult = []

        for i in range(len(sBoxResult)):  # sbox 결과를 문자열로 저장
            for j in range(len(sBoxResult[i])):
                sBoxResultBit += sBoxResult[i][j]

        for i in pBox:  # sbox 문자열을 참고하여 pbox에 인덱싱하여 저장
            pBoxResultBit += sBoxResultBit[i - 1]

        for i in pBoxResultBit:  # 결과 8비트씩 저장
            bit += i
            if len(bit) == 8:
                emptyList.append(bit)
                bit = ""
        pBoxResult.append(emptyList)

        return pBoxResult  # pbox 순열 결과 [['000..','000...',..]]
