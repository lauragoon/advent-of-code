using System;
using System.IO;

class Day01
{
    public sealed class Puzzle
    {
        public int SolvePart1(string filePath)
        {
            int startPos = 50;
            int numTimesAtZero = 0;
            
            foreach (string line in File.ReadLines(filePath))
            {
                startPos = RotateDialPart1(startPos, line);
                if (startPos == 0)
                    numTimesAtZero++;
            }
                
            return numTimesAtZero;
        }
        
        public int SolvePart2(string filePath)
        {
            int startPos = 50;
            int numTimesPassZero = 0;
            
            foreach (string line in File.ReadLines(filePath))
            {
                (startPos, var newTimesPassZero) = RotateDialPart2(startPos, line);
                numTimesPassZero += newTimesPassZero;
            }
            return numTimesPassZero;
        }
        
        internal static int RotateDialPart1(int currPos, string rotationIns)
        {
            char direction = rotationIns[0];
            int directionNum = direction == 'L' ? -1 : 1;
            int amt = int.Parse(rotationIns.Substring(1));
            
            int newPos = currPos + (directionNum * amt);
            
            // Fix outer-bounds wrap-around
            while (newPos > 99 || newPos < 0)
            {
                if (newPos > 99)
                    newPos = newPos - 100;
                else if (newPos < 0)
                    newPos += 100;
            }
                
            return newPos;
        }
        
        internal static (int, int) RotateDialPart2(int currPos, string rotationIns)
        {
            char direction = rotationIns[0];
            int directionNum = direction == 'L' ? -1 : 1;
            int amt = int.Parse(rotationIns.Substring(1));
            int numTimesPassZero = 0;
            
            // Base case: no displacement
            if (amt == 0)
                return (currPos, 0);
            
            // Calculate how many complete rotations (passing through 0)
            numTimesPassZero = amt / 100;
            
            // Calculate the final position
            int newPos = (currPos + (directionNum * amt)) % 100;
            
            // Handle negative & positive wrap-around
            if (newPos < 0)
                newPos += 100;
            else if (newPos > 99)
                newPos -= 100;
                
            // Check if we pass through 0 during the partial rotation
            int partialAmt = amt % 100;
            if (direction == 'L')
            {
                if (currPos != 0 && currPos - partialAmt < 0)
                    numTimesPassZero++;
            }
            else
            {
                if (newPos != 0 && currPos + partialAmt > 99)
                    numTimesPassZero++;
            }
            
            if (currPos != 0 && newPos == 0)
            {
                numTimesPassZero++;
            }
                
            return (newPos, numTimesPassZero);
        }
    }
    
    internal static class Program
    {
        static void Main()
        {
            var input = "../aoc-inputs/2025/01.txt";
            var puzzle = new Puzzle();  // Create an instance
            
            var part1Ans = puzzle.SolvePart1(input);  // Call the method on the instance
            Console.WriteLine($"Part 1 Answer: {part1Ans}"); // Ans: 1089
            
            var part2Ans = puzzle.SolvePart2(input); 
            Console.WriteLine($"Part 2 Answer: {part2Ans}"); // Ans: 6530
        }
    }
}