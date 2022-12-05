const fs = require("fs");
const util = require("util")

const filename = "drawing.txt";

fs.readFile(filename, "utf8", (err, data) =>
{
    if (err)
    {
        console.error(err);
        return;
    }

    crateStacks1 = [[],[],[],[],[],[],[],[],[]]
    crateStacks2 = [[],[],[],[],[],[],[],[],[]]

    stacks = data.split(/\n\n/)[0]
        .split(/\n/)
        .filter(dataStr => dataStr.length > 0)
        .map(line => {
            return line
                .match(/.{1,4}/g)
                .map(crate => {
                    return crate.replace(/\s/g, "")
                });
        })
        .slice(0,-1);

    stacks
        .map(line => {
            for (let i = 0; i < 9; i++)
            {
                if (line[i].length > 0)
                {
                    letter = line[i].replace("[", "").replace("]", "");
                    crateStacks1[i].unshift(letter);
                    crateStacks2[i].unshift(letter);
                }
            }
        });

    procedures = data.split(/\n\n/)[1]
        .split(/\n/)
        .filter(dataStr => dataStr.length > 0)
        .map(step => {
            step = step.split(" ");
            let i = step.length;
            while (i--) i % 2 === 0 && (step.splice(i, 1));
            return step;
        });

    procedures
        .map(step => {
            moveAmt = step[0];
            fromNum = step[1]-1;
            toNum = step[2]-1;

            for (let i = 0; i < moveAmt; i++)
            {
                moveCrate = crateStacks1[fromNum].pop();
                crateStacks1[toNum].push(moveCrate);
            }
        });

    // console.log(util.inspect(calorieData, {maxArrayLength: null, depth:null }))
    
    part1Ans = ""
    for (let i = 0; i < 9; i++)
    {
        part1Ans += crateStacks1[i].slice(-1);
    }
    console.log("Part 1 answer: " + part1Ans); // WCZTHTMPS

    procedures
        .map(step => {
            moveAmt = step[0];
            fromNum = step[1]-1;
            toNum = step[2]-1;

            moveCrate = crateStacks2[fromNum].slice(-moveAmt);
            crateStacks2[fromNum] = crateStacks2[fromNum].slice(0, -moveAmt);
            crateStacks2[toNum] = crateStacks2[toNum].concat(moveCrate);
        });

    part2Ans = ""
    for (let i = 0; i < 9; i++)
    {
        part2Ans += crateStacks2[i].slice(-1);
    }
    console.log("Part 2 answer: " + part2Ans); // BLSGJSDTS
    
});
