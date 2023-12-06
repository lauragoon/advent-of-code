const fs = require("fs");
const util = require("util")

const filename = "../aoc-inputs/2022/04.txt"

fs.readFile(filename, "utf8", (err, data) =>
{
    if (err)
    {
        console.error(err);
        return;
    }

    processedData = data
        .split(/\n/)
        .filter(dataStr => dataStr.length > 0)
        .map(pair => {
            return pair
                .split(",")
                .map(assignment => {
                    return assignment
                        .split("-")
                        .map(num => {
                            return parseInt(num)
                        })
                })
        });

    isAssignmentFullOverlap = processedData
        .map(pair => {
            var first_min = pair[0][0]
            var first_max = pair[0][1]
            var second_min = pair[1][0]
            var second_max = pair[1][1]

            return (first_min <= second_min && first_max >= second_max) ||
                (second_min <= first_min && second_max >= first_max)
        });
    
    part1Ans = isAssignmentFullOverlap.filter(pair => pair).length
    console.log("Part 1 answer: " + part1Ans); // 462

    isAssignmentPartialOverlap = processedData
        .map(pair => {
            var first_min = pair[0][0]
            var first_max = pair[0][1]
            var second_min = pair[1][0]
            var second_max = pair[1][1]

            return (first_min <= second_min && first_max >= second_min) ||
                (second_min <= first_min && second_max >= first_min)
        });

    part2Ans = isAssignmentPartialOverlap.filter(pair => pair).length
    console.log("Part 2 answer: " + part2Ans); // 835
    
});
