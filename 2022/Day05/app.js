

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

function processMoves(stacks, moves) {
    for (const move of moves) {
        const parts = move.split(' ');
        const numCrates = parseInt(parts[1]);
        const fromStack = parseInt(parts[3]) - 1;
        const toStack = parseInt(parts[5]) - 1;

        for (let i = 0; i < numCrates; i++) {
            const crate = stacks[fromStack].pop();
            stacks[toStack].push(crate);
        }
    }
    
    const result = stacks.map(stack => stack[stack.length - 1] || '').join('');
    return result;
}

const fileName = 'input.txt';
const { stacks, moves } = readStacksAndMoves(fileName);
const result = processMoves(stacks, moves);
console.log("Caixas no topo das pilhas:", result);
