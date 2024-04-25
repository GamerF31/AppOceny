def srednia_ocen(ocena):
    if not ocena:
        return 0;
    return sum(ocena) / len(ocena);

def najlepsza_ocena(ocena):
    if not ocena:
        return None
    return max(ocena)

def najgorsza_ocena(ocena):
    if not ocena:
        return None
    return min(ocena)