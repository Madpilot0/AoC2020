const { readFileSync } = require("fs")

module.exports = {
  readFromFile: (filename) => {
    return readFileSync(filename, {encoding: "utf-8"}).toString().split("\n")
  }
}