def calculate_gc_content(dna_sequence):
    """
    주어진 DNA 서열에서 GC 함량을 계산합니다.

    Parameters:
    dna_sequence (str): DNA 서열 (A, T, C, G로 구성된 문자열)

    Returns:
    float: GC 함량 (백분율로 표현)
    """
    # 전체 서열 길이 계산
    total_length = len(dna_sequence)
    
    # G와 C의 개수 계산
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    
    # GC 함량 계산
    gc_content = (g_count + c_count ) / total_length * 100
    
    return gc_content

# 테스트용 DNA 서열
test_sequence = "ATCGGCTAAGCTAGCTAGGCTA"
gc_content = calculate_gc_content(test_sequence)
print(f"GC 함량: {gc_content:.2f}%")
