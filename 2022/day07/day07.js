const fs = require("fs");
const util = require("util");
const readline = require("readline");

var oneCompilerConfig = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

const ConstantStrings = {
	ls: "ls",
	cd: "cd",
	file: "file",
	dir: "dir"
}

function Node(name, type, size=null)
{
  this.name = name;
  this.type = type;
  this.size = size;
  this.parent = null;
  this.children = [];
}

function Tree(name)
{
  var node = new Node(name);
  this.root = node;
}

function Node.LocateChild(name)
{
  for (let idx = 0; idx < this.children.length; idx++)
  {
    let currChildName = this.children[idx].name;
    if (currChildName == name)
      return this.children[idx];
  }
  console.error("Error in LocateChild(): No child with ".concat(name, " name found."));
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
      fileSystemTree = Tree(processedLine[2], ConstantStrings.dir, null);
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
          
          case ConstantStrings.ls:
            break;
            
          case ConstantStrings.cd:
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
        
        if (currCommand == ConstantStrings.ls)
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
