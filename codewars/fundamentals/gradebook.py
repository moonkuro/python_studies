def get_grade(s1, s2, s3):
    media_final = (s1 + s2 + s3) / 3

    if 0 <= media_final < 60:
        return "F"
    elif 60 <= media_final < 70:
        return "D"
    elif 70 <= media_final < 80:
        return "C"
    elif 80 <= media_final < 90:
        return "B"
    elif 90 <= media_final <= 100:
        return "A"