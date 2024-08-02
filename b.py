def pattern_count(dna_sequence, pattern):
    """
    주어진 DNA 서열에서 특정 패턴(서브서열)의 빈도를 계산합니다.

    Parameters:
    dna_sequence (str): DNA 서열 (A, T, C, G로 구성된 문자열)
    pattern (str): 찾고자 하는 패턴 (서브서열)

    Returns:
    int: 패턴이 나타나는 빈도수
    """
    count = 0
    pattern_length = len(pattern)
    
    # 패턴이 나타나는 위치를 찾아 빈도수 계산
    for i in range(len(dna_sequence) - pattern_length + 1):
        if dna_sequence[i:i+pattern_length] == pattern:
            count += 1
    
    return count

# 테스트용 DNA 서열 및 패턴
test_sequence = "ATCGGCTAAGCTAGCTAGGCTA"
pattern = "GCTA"
pattern_frequency = pattern_count(test_sequence, pattern)
print(f"패턴 '{pattern}'의 빈도수: {pattern_frequency}")
