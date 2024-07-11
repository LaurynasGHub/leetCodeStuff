const candies = [2, 3, 5, 1, 3];
const extraCandies = 3;

function kidsWithCandies(candies, extraCandies) {
  const highValue = Math.max(...candies);

  let resultArray = [];

  candies.forEach((element) => {
    console.log('element', element + extraCandies);

    if (element + extraCandies >= highValue) {
      resultArray.push(true);
    } else {
      resultArray.push(false);
    }
  });

  return resultArray;
}

let array = kidsWithCandies(candies, extraCandies);
console.log(array);
