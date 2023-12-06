const fs = require("fs");
const util = require("util");

const filename = "../aoc-inputs/2022/06.txt";

fs.readFile(filename, "utf8", (err, data) =>
{
    if (err)
    {
        console.error(err);
        return;
    }

    processedData = data
        .split(/\n/)[0]
        .split("");

    tempMarker1 = [];
    part1Ans = null;
    tempMarker2 = [];
    part2Ans = null;

    for (let i = 0; i < processedData.length; i++)
    {
        if (part1Ans == null && tempMarker1.length < 4)
        {
            tempMarker1.push(processedData[i]);
        }
        else if (part1Ans == null && tempMarker1.length == 4)
        {
            tempMarker1.shift();
            tempMarker1.push(processedData[i]);

            tempMarkerSet1 = new Set(tempMarker1);
            if (tempMarkerSet1.size == 4)
            {
                part1Ans = i + 1;
                if (part2Ans != null) break;
            }
        }

        if (part2Ans == null && tempMarker2.length < 14)
        {
            tempMarker2.push(processedData[i]);
        }
        else if (part2Ans == null && tempMarker2.length == 14)
        {
            tempMarker2.shift();
            tempMarker2.push(processedData[i]);

            tempMarkerSet2 = new Set(tempMarker2);
            if (tempMarkerSet2.size == 14)
            {
                part2Ans = i + 1;
                if (part1Ans != null) break;
            }
        }
    }
    
    console.log("Part 1 answer: " + part1Ans); // 1155
    console.log("Part 2 answer: " + part2Ans); // 2789
    
});
