const tools = require('./tools')

const passwords = tools.readFromFile('../inputs/day2.txt')

function validPasswordCount (passwords) {
  validCount = 0
  passwords.forEach((p) => {
    let [minNum, maxNum, char, pwd] = p.split(/-|:|\s/g).filter(p => p)
    // if (new RegExp(char, 'g') || []).length
    let re = new RegExp(char, 'g')
    count_chars = (pwd.match(re) || []).length
    if (count_chars >= minNum && count_chars <= maxNum) {
      validCount++
    }
  })
  return validCount
}

function validPasswordChar (passwords) {
  validCount = 0
  passwords.forEach((p) => {
    let [minNum, maxNum, char, pwd] = p.split(/-|:|\s/g).filter(p => p)
    if ((pwd[minNum - 1] === char || pwd[maxNum - 1] === char) && pwd[minNum - 1] !== pwd[maxNum - 1]) {
      validCount++
    }
  })
  return validCount
}

console.log(`Part 1: ${validPasswordCount(passwords)}`)
console.log(`Part 2: ${validPasswordChar(passwords)}`)