const fs = require("fs");
const util = require('util')

const filename = "strategy.txt";
const shapes = {
    'A': "Rock",
    'B': "Paper",
    'C': "Scissors",
    'X': "Rock",
    'Y': "Paper",
    'Z': "Scissors"
};
const scores = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
    "OutcomeLose": 0,
    "OutcomeDraw": 3,
    "OutcomeWin": 6
};

function getMatchOutcome(oppShape, myShape)
{
    var oppShapeVal = shapes[oppShape];
    var myShapeVal = shapes[myShape];

    if (oppShapeVal == myShapeVal) return "OutcomeDraw";

    if ((oppShapeVal == "Rock" && myShapeVal == "Scissors") ||
        (oppShapeVal == "Paper" && myShapeVal == "Rock") ||
        (oppShapeVal == "Scissors" && myShapeVal == "Paper"))
    {
        return "OutcomeLose";
    }

    return "OutcomeWin";
}

function getMatchScore(myShape, matchOutcome)
{
    var myShapeVal = shapes[myShape];
    return scores[myShapeVal] + scores[matchOutcome];
}

fs.readFile(filename, "utf8", (err, data) =>
{
    if (err)
    {
        console.error(err);
        return;
    }

    var processedData = data
        .split(/\n/)
        .filter(dataStr => dataStr.length > 0)
        .map(match => {
            return match.split(" ")
        });

    var scoresPerMatch = processedData
        .map(match => {
            return [match[1], getMatchOutcome(match[0], match[1])]
        })
        .map(results => {
            return getMatchScore(results[0], results[1])
        });
    
    part1Ans = scoresPerMatch.reduce((a,b) => a + b);
    console.log("Part 1 answer: " + part1Ans);
    
});