def count_peaks(peaks):
    """(list of number) -> (list of number)
    Return list containing number of occurrences of top peaks and bottom peaks.

    A top peak is when the number in the list is at least 5 times greater than its neighbors.
    A bottom peak is when the number in the list is at least 5 times lower than its neighbors.
    
    :param peaks: List of numbers representing the peaks.
    :return: A list with the counts of top peaks and bottom peaks. 
    """
    top_peaks = 0
    bottom_peaks = 0

    for indice in range(1, len(peaks)-1):
        if (peaks[indice] > peaks[indice-1] + 5) and (peaks[indice] > peaks[indice+1] + 5):
            top_peaks = top_peaks + 1
        if (peaks[indice] < peaks[indice-1] - 5) and (peaks[indice] < peaks[indice+1] - 5):
            bottom_peaks = bottom_peaks + 1
    
    return [top_peaks, bottom_peaks]


