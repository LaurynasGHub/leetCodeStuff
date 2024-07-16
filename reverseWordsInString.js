const s = " Hello   World  "

function reverseWordsInStrin(s){
      const sString = s.replace(/\s+/g,' ').trim().split(' ')

    let returnString = []

    for(i = 1; i< sString.length+1; i++){
        returnString.splice(i, 0, sString[sString.length - i])
    }

    return returnString.join(' ')
}
