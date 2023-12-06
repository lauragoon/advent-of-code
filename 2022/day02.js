const fs = require("fs");
const util = require('util')

const filename = "../aoc-inputs/2022/02.txt";
const shapes = {
    'A': "Rock",
    'B': "Paper",
    'C': "Scissors"
};
const decryptShapes = {
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
const decryptOutcomes = {
    'X': "OutcomeLose",
    'Y': "OutcomeDraw",
    'Z': "OutcomeWin"
};
const outcomeToIdx = {
    "OutcomeLose": 0,
    "OutcomeDraw": 1,
    "OutcomeWin": 2
};
const shapeOutcomes = {
    "Rock": ["Scissors", "Rock", "Paper"],
    "Paper": ["Rock", "Paper", "Scissors"],
    "Scissors": ["Paper", "Scissors", "Rock"]
};

function getMatchOutcome(oppShape, myShape)
{
    var oppShapeVal = shapes[oppShape];
    var myShapeVal = decryptShapes[myShape];

    if (oppShapeVal == myShapeVal) return "OutcomeDraw";

    if ((oppShapeVal == "Rock" && myShapeVal == "Scissors") ||
        (oppShapeVal == "Paper" && myShapeVal == "Rock") ||
        (oppShapeVal == "Scissors" && myShapeVal == "Paper"))
    {
        return "OutcomeLose";
    }

    return "OutcomeWin";
}

function getMatchScore(myShape, matchOutcome, needDecrypt=true)
{   
    var myShapeVal = myShape;
    if (needDecrypt) myShapeVal = decryptShapes[myShape];

    return scores[myShapeVal] + scores[matchOutcome];
}

function playStrategyMatch(oppShape, stratOutcome)
{
    var oppShapeVal = shapes[oppShape];
    var stratOutcomeVal = decryptOutcomes[stratOutcome];

    var myShapeVal = shapeOutcomes[oppShapeVal][outcomeToIdx[stratOutcomeVal]];
    
    return [myShapeVal, stratOutcomeVal]
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

    var scoresPerMatch1 = processedData
        .map(match => {
            return [match[1], getMatchOutcome(match[0], match[1])]
        })
        .map(results => {
            return getMatchScore(results[0], results[1])
        });
    
    part1Ans = scoresPerMatch1.reduce((a,b) => a + b);
    console.log("Part 1 answer: " + part1Ans); // 14827

    var scoresPerMatch2 = processedData
        .map(match => {
            return playStrategyMatch(match[0], match[1])
        })
        .map(results => {
            return getMatchScore(results[0], results[1], needDecrypt=false)
        });

    part2Ans = scoresPerMatch2.reduce((a,b) => a + b);
    console.log("Part 2 answer: " + part2Ans); // 13889

});