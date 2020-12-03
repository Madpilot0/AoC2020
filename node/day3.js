const tools = require('./tools')
const tree_map = tools.readFromFile('../inputs/day3.txt')

function traverse_map(tree_map, move) {
  let [move_right, move_down] = move
  let x_pos = 0
  let y_pos = 0
  let tree_count = 0
  while (y_pos < tree_map.length) {
    if (tree_map[y_pos][x_pos % tree_map[y_pos].length] === "#") {
      tree_count++
    }
    y_pos += move_down
    x_pos += move_right
  }

  return tree_count
}

function count_trees(tree_map, input_directions) {
  let result = 1
  input_directions.forEach((directions) => {
    let tree_count = traverse_map(tree_map, directions)
    result *= tree_count
  })

  return result
}

input_a = [
  [3,1]
]
input_b = [
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2]
]

console.log(`Part 1: ${count_trees(tree_map, input_a)}`)
console.log(`Part 2: ${count_trees(tree_map, input_b)}`)