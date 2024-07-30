// 
// QUESTION no 28
// METHODS- KMP algorithm, Two Pointers
// 
var strStr = function (haystack, needle) {
    const needleLength = needle.length;
    let i = 0, j = -1;

    // LPS - Longest Prefix Suffix / Prefix table 
    const lps = [-1];
    while (i < needleLength - 1) {
        if (j === -1 || needle[i] === needle[j]) {
            i++;
            j++;
            lps[i] = j;
        } else {
            j = lps[j];
        }
    }

    i = 0, j = 0;
    while (i < haystack.length && j < needleLength) {
        if (haystack[i] === needle[j]) {
            i++;
            j++;
        } else {
            j = lps[j];
            if (j < 0) {
                i++;
                j++;
            }
        }
    }
    if (j === needleLength) {
        return i - j;
    }
    return -1;
}
