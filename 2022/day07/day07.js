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
  this.type = type; // file or dir
  this.size = size; // int for file, null for dir
  this.parent = null;
  this.children = [];
}

function Tree(name, type, size=null)
{
  var node = new Node(name, type, size);
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
                if (fileSystemPointer == null)
                  console.error("Error in main/LocateChild(): No child with ".concat(name, " name found."));
                break;
            }
            
        }
      }
      
      // build filesystem via $ls
      else
      {
        
        if (currCommand == ConstantStrings.ls)
        {
          let data1 = processedLine[0];
          let data2 = processedLine[1];
          
          // don't add duplicate data shown via $ls
          if (fileSystemPointer.LocateChild(data2)) == null)
          {
            if (data1 == ConstantStrings.dir)
              fileSystemPointer.children.push(Node(data2, ConstantStrings.dir, null))
            else
              fileSystemPointer.children.push(Node(data1, ConstantStrings.file, parseInt(data1)))
          }
        }
        
        else
        {
          console.error("Error in main function: Unexpected pathing, no command to execute.")
        }
      }
    }
    
});



// console.log(processedLine);
    
// console.log("Part 1 answer: " + part1Ans); // 
// console.log("Part 2 answer: " + part2Ans); //
