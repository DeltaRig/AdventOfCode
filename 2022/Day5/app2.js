// Daniela Pereira Rigoli September 5th 2024

const fs = require('fs');

function readStacksAndMoves(fileName) {
    const data = fs.readFileSync(fileName, 'utf-8');
    const lines = data.split('\n');
    
    let stacks = [];
    let moves = [];
    let stackLines = [];

    for (const line of lines) {
        if (line.startsWith('move')) {
            moves.push(line.trim());
        } else if (line.trim().length === 0) {
            continue;
        } else if (line.trim()[0].match(/[0-9]/)) {
            const stackCount = line.split(/\s+/).length;
            stacks = Array.from({ length: stackCount }, () => []);
        } else if (line.includes('[')) {
            stackLines.push(line);
        }
    }

    for (let i = stackLines.length - 1; i >= 0; i--) {
        const stackLine = stackLines[i];
        for (let j = 0; j < stackLine.length; j += 4) {
            const crate = stackLine[j + 1];
            if (crate !== ' ') {
                const stackIndex = Math.floor(j / 4);
                stacks[stackIndex].push(crate);
            }
        }
    }

    return { stacks, moves };
}

// O(n)
function processMoves(stacks, moves) {
    for (const move of moves) {
        const parts = move.split(' ');
        const numCrates = parseInt(parts[1]);
        const fromStack = parseInt(parts[3]) - 1;
        const toStack = parseInt(parts[5]) - 1;

        // Remove the crates to move (preserve order, so we slice them together)
        const cratesToMove = stacks[fromStack].splice(stacks[fromStack].length - numCrates, numCrates);
        
        // Add them to the target stack (preserving order)
        stacks[toStack].push(...cratesToMove);
    }
    // Get the top crate of each stack and form the result
    const result = stacks.map(stack => stack[stack.length - 1] || '').join('');
    return result;
}
const fileName = 'input.txt';
const { stacks, moves } = readStacksAndMoves(fileName);
const result = processMoves(stacks, moves);
console.log("Top crates after rearrangement:", result);
