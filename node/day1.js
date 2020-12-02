const { exec } = require('child_process')
const tools = require('./tools')

const expenses = tools.readFromFile('../inputs/day1.txt')
                  .map((v) => parseInt(v))

function getExpensesTwo(expenses) {
  for (let x = 0; x < expenses.length; x++) {
    for (let y = x; y < expenses.length; y++) {
      if (expenses[x] + expenses[y] === 2020) {
        console.log('found')
        return expenses[x] * expenses[y]
      }
    }
  }
}

function getExpensesThree(expenses) {
  for (let x = 0; x < expenses.length; x++) {
    for (let y = x; y < expenses.length; y++) {
      for (let z = y; z < expenses.length; z++) {
        if (expenses[x] + expenses[y] + expenses[z] === 2020) {
          return expenses[x] * expenses[y] * expenses[z]
        }
      }
    }
  }
}

// Playing around with .some and .slice
function testje(expenses) {
  let value = null
  expenses.some((x, v) => {
    if (value) return true
    expenses.slice(v).some((y) => {
      if (x + y === 2020) {
        value = x * y
        return true
      }
    })
  })
  return value
}

console.log(`Part 1: ${getExpensesTwo(expenses)}`)
console.log(`Part 2: ${getExpensesThree(expenses)}`)

console.log(`Test for part 1: ${testje(expenses)}`)