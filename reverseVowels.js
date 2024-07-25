// 
// QUESTION no- 345
// METHODS- Two Pointers, String
// 
const s = 'hello';

function reverseVowels(s) {
  const vowels = 'aeiouAEIOU';
  let left = 0;
  let right = s.length - 1;
  const sArray = s.split(''); // Convert the string to an array for easier modification

  while (left < right) {
    // Move the left pointer to the next vowel
    while (left < right && !vowels.includes(sArray[left])) {
      left++;
    }

    // Move the right pointer to the next vowel
    while (left < right && !vowels.includes(sArray[right])) {
      right--;
    }

    // Swap the vowels at the left and right pointers
    [sArray[left], sArray[right]] = [sArray[right], sArray[left]];

    left++;
    right--;
  }

  // Convert the array back to a string
  return sArray.join('');
}

reverseVowels(s);
