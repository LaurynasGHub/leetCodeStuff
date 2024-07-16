const nums = [1,2,3,4]

// my solution, works, but on testcase 18 gives time limit exceeded error
function productOfArrayExceptSelf(nums){
      let returnNums = []

    for (i = 0; i < nums.length; i++){
        let num = 1

        let calcArr = nums.toSpliced(i, 1)

        for (a = 0; a < calcArr.length; a++){
                num = num * calcArr[a]
            
        }
        returnNums.push(num)
   }

   return returnNums
