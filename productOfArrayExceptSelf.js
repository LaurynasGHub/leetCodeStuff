const nums = [1, 2, 3, 4];

// my solution, works, but on testcase 18 gives time limit exceeded error
function productOfArrayExceptSelf(nums) {
  let returnNums = [];

  for (i = 0; i < nums.length; i++) {
    let num = 1;

    let calcArr = nums.toSpliced(i, 1);

    for (a = 0; a < calcArr.length; a++) {
      num = num * calcArr[a];
    }
    returnNums.push(num);
  }

  return returnNums;
}

//using the optimized approach, still slow, but doesn't exceed time limit

function optimizedProductOfArrayExceptSelf(nums) {
  let returnNums = [];

  let rightArray = [1];
  let num = 1;

  for (i = 0; i < nums.length - 1; i++) {
    num = num * nums[i];
    rightArray.push(num);
  }

  let leftArray = [];
  num = 1;

  for (i = nums.length - 1; i > 0; i--) {
    num = num * nums[i];
    console.log('num-', num, 'i-', i);
    leftArray.unshift(num);
  }

  leftArray.push(1);

  console.log('rightArray- ', rightArray);
  console.log('leftArray- ', leftArray);

  for (i = 0; i < nums.length; i++) {
    returnNums[i] = rightArray[i] * leftArray[i];
  }

  console.log(returnNums);
}

// optimizedProductOfArrayExceptSelf(nums);

//top 5% answer
function productExceptSelf(nums) {
  let result = new Array(nums.length);

  let prefix = 1;
  for (let i = 0; i < nums.length; i++) {
    result[i] = prefix;
    prefix *= nums[i];
  }

  //instead of creating 2 arrays it creates 1 and
  //just multiplies 1st array values from the 2nd
  let suffix = 1;
  for (let i = nums.length - 1; i >= 0; i--) {
    result[i] *= suffix;
    suffix *= nums[i];
  }

  return result;
}

console.log(productExceptSelf(nums));
