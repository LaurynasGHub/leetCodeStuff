//
// QUESTION no- 1071
// METHODS- String, Math
//
var str1 = 'AABCABDCABCA';
var str2 = 'ABAB';

function gcdOfStrings(str1, str2) {
  for (i = 0; i < str1.length; i++) {
    let slicedPart = str1.slice(i, i + str2.length);

    if (slicedPart === str2) {
      for (i = 0; i < str2.length; i++) {
        let slicedPart2 = str2.slice(i, i);
      }

      return slicedPart;
    }
  }

  return '';
}

gcdOfStrings(str1, str2);
