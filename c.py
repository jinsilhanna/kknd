def find_longest_orf(dna_sequence):
    """
    주어진 DNA 서열에서 가장 긴 ORF를 찾습니다.

    Parameters:
    dna_sequence (str): DNA 서열 (A, T, C, G로 구성된 문자열)

    Returns:
    str: 가장 긴 ORF 서열
    """
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    longest_orf = ""
    
    for frame in range(3):
        for i in range(frame, len(dna_sequence), 3):
            if dna_sequence[i:i+3] == start_codon:
                for j in range(i, len(dna_sequence), 3):
                    codon = dna_sequence[j:j+3]
                    if codon in stop_codons:
                        orf = dna_sequence[i:j+3]
                        if len(orf) > len(longest_orf):
                            longest_orf = orf
                        break
    
    return longest_orf

# 테스트용 DNA 서열
test_sequence = "ATCGGCTATGTAGCTAGCTAATGAGGTAACTAG"
longest_orf = find_longest_orf(test_sequence)
print(f"가장 긴 ORF: {longest_orf}")
