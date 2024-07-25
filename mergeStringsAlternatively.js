// 
// QUESTION no- 1768
// METHODS- Two Pointers
// 
var word1 = 'chair';
var word2 = 'kebabas';

function mergeAlternatively(word1, word2) {
  let mergedString = '';

  for (let i = 0; i < word2.length; i++) {
    if (typeof word1[i] !== 'undefined') {
      mergedString += word1[i];
    }

    mergedString += word2[i];
  }

  console.log(mergedString);

  return mergeAlternatively;
}

const answer = mergeAlternatively(word1, word2);
