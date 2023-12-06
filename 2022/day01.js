const fs = require("fs");
const util = require('util')

const filename = "../aoc-inputs/2022/01.txt"

fs.readFile(filename, "utf8", (err, data) =>
{
    if (err)
    {
        console.error(err);
        return;
    }

    var calorieData = data
        .split(/\n\n/)
        .map(calories => 
        {
            return calories
                .split(/\n/)
                .filter(calorieStr => calorieStr.length > 0)
                .map(calorie =>
                    {
                        return parseInt(calorie)
                    })
        });

    var summedCalories = calorieData
        .map(calories => 
        {
            return calories.reduce((a,b) => a + b);
        });
        
    // console.log(util.inspect(calorieData, {maxArrayLength: null, depth:null }))
    
    part1Ans = summedCalories.reduce((a,b) => Math.max(a,b));
    console.log("Part 1 answer: " + part1Ans); // 69289

    part2Ans = summedCalories
        .sort(function(a,b) {return a - b})
        .reverse()
        .splice(0,3)
        .reduce((a,b) => a + b);
    console.log("Part 2 answer: " + part2Ans); // 205615
    
});
