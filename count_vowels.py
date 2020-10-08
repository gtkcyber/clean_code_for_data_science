import re

class count_vowels:
    def vowel_consonant_ratio(text):
        # Convert to lower case
        text = text.lower()

        # Count vowels
        vowels = len(re.findall('[aeiouy]', text))

        # Count consonants (everything else)
        consonants = len(re.findall('[^aeiouy]', text))
        return vowels / consonants

    print(vowel_consonant_ratio('encylopedia'))
    #print(vowel_consonant_ratio('yoyo'))

    #print(vowel_consonant_ratio('fast-moving'))