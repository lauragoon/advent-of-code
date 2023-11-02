const fs = require("fs");
const util = require("util");
const readline = require("readline");

var oneCompilerConfig = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

function Node(data)
{
  this.data = data;
  this.parent = null;
  this.children = [];
}

function Tree(data)
{
  var node = new Node(data);
  this.root = node;
}

function Node.LocateChild(data)
{
  for (let idx = 0; idx < this.children.length; idx++)
  {
    let currChildData = this.children[idx].data;
    if (currChildData == data)
      return this.children[idx];
  }
  console.error("Error in LocateChild(): No child with ".concat(data, " name found."));
  return null;
}

var currCommand = "";
var fileSystemTree = null;
var fileSystemPointer = null;

oneCompilerConfig.on("line", function(line)
{
    processedLine = line.split(" ");
    
    // create start of filesystem, guaranteed to be a $cd command
    if (fileSystemTree == null)
    {
      fileSystemTree = Tree(processedLine[2]);
      fileSystemPointer = fileSystemTree.root;
    }
    
    // contribute to building up existing filesystem
    else
    {
      
      // keep track of current $ command
      if (processedLine[0] == "$")
      {
        currCommand = processedLine[1];
        // execute necessary commands
        switch(currCommand)
        {
          
          case "ls":
            break;
            
          case "cd":
            let cdParam = processedLine[2];
            
            switch(cdParam)
            {
              case "/":
                fileSystemPointer = fileSystemTree.root;
                break;
                
              case "..":
                fileSystemPointer = fileSystemPointer.parent;
                break;
                
              default:
                fileSystemPointer = fileSystemPointer.LocateChild(processedLine[2]);
                break;
            }
            
        }
      }
      
      // build filesystem via $ls
      else
      {
        
        if (currCommand == "ls")
        {
          break; // TODO
        }
        
        else
        {
          console.error("Error in main function: Unexpected pathing, no command to execute.")
        }
      }
    }
    
    
    // console.log(processedLine);
    
    // console.log("Part 1 answer: " + part1Ans); // 
    // console.log("Part 2 answer: " + part2Ans); // 
    
});
