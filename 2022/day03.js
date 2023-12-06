const fs = require("fs");
const util = require("util")

const filename = "../aoc-inputs/2022/03.txt"

fs.readFile(filename, "utf8", (err, data) =>
{
    if (err)
    {
        console.error(err);
        return;
    }

    var processedData1 = data
        .split(/\n/)
        .filter(dataStr => dataStr.length > 0)
        .map(rucksack => {
            var len_rucksack = rucksack.length;
            var second_idx = len_rucksack / 2;

            return [rucksack.substring(0,second_idx).split(""),
                rucksack.substring(second_idx,len_rucksack).split("")]
        });

    var sharedItems = processedData1
        .map(rucksack => {
            return rucksack[0].filter(item => rucksack[1].includes(item))
        })
        .map(item => {
            return item[0]
        });
    
    part1Ans = sharedItems
        .map(item => {
            if (item == item.toLowerCase()) return item.charCodeAt(0)-96;
            else return item.charCodeAt(0)-38;
        })
        .reduce((a,b) => a + b);
    console.log("Part 1 answer: " + part1Ans); // 7872

    var processedData2 = data
        .match(/(?:^.*$\n?){3}/mg)
        .filter(rucksack => rucksack.length > 0)
        .map(group => {
            return group
                .split(/\n/)
                .filter(dataStr => dataStr.length > 0)
                .map(rucksack => {
                    return rucksack.split("");
                });
        });

    // console.log(util.inspect(processedData2, {maxArrayLength: null, depth:null }))

    var badgeItems = processedData2
        .map(group => {
            return group[0]
                .filter(item => group[1].includes(item))
                .filter(item => group[2].includes(item))[0]
        });

    part2Ans = badgeItems
        .map(item => {
            if (item == item.toLowerCase()) return item.charCodeAt(0)-96;
            else return item.charCodeAt(0)-38;
        })
        .reduce((a,b) => a + b);
    console.log("Part 2 answer: " + part2Ans); // 2497
    
});
