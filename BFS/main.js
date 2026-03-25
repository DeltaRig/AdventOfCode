// Problema resolvido com BFS
// 2026 March 21
// Daniela Rigoli - Javascript - node v18.16.1
const fs = require('fs');

// leitura do arquivo (stdin ou arquivo)
const input = fs.readFileSync(
    process.argv[2] ? process.argv[2] : 'input.txt',
    'utf-8').trim().split('\n');

// listas
let c = []; // capacidade
let a = []; // start
let t = []; // goal

// parse das 3 linhas
c = input[0].split(' ').map(Number);
a = input[1].split(' ').map(Number);
t = input[2].split(' ').map(Number);

// somas
let sc = c.reduce((s, x) => s + x, 0);
let sa = a.reduce((s, x) => s + x, 0);
let st = t.reduce((s, x) => s + x, 0);

console.log("c:", c, " | ", sc);
console.log("a:", a, " | ", sa);
console.log("t:", t, " | ", st);

// verificações iniciais
if (sa != st) {
    console.log("impossivel pq sa != st " + sa + " | " + st );
    process.exit(0);
}

if (st > sc) { // goal > capacidade
    console.log("impossivel pq st > sc");
    process.exit(0);
}

for (let i = 0; i > t.length; i++) {
    if (t[i] > c[i]) { // goal[i] > capacidade[i]
        console.log("impossivel pq " +i + " | " + t[i] +" > " + c[i]);
        process.exit(0);
    }
}

// pass, now and future
let p = new Set();
let n = [a];
let f = [];

p.add(serialize(a));

goal(n[0])
while(n.length > 0){
    // tenta gerar novos estados
    for(let i = 0; i < n[0].length; i++){
        if (n[0][i] > t[i]) {
            for (let j = 0; j < n[0].length; j++) {
                if (i === j) continue;

                if (n[0][j] < t[j]) { // now < goal de quem vai receber
                    // quanto pode transferir
                    let maxTransfer = Math.min(
                        n[0][i], //  now 
                        c[j] - n[0][j]  // capacidade - now de quem recebe
                    );

                    if (maxTransfer > 0) {
                        let newA = [...n[0]];
                        newA[i] -= maxTransfer;
                        newA[j] += maxTransfer;

                        var size = p.size;
                        p.add(serialize(newA));
                        if(size < p.size){
                            f.push(newA);
                            console.log("f " + f);
                            console.log("p " + p);
                        }
                    }
                }
            }
        }
    }
    
    //
    goal(n[0])
    console.log("now ", n[0])
    n.shift();
    if(n.length == 0){
        n = f;
        f = [];
        console.log(f)
    }

    
}

// se terminou tudo sem achar solução
console.log("impossivel não achei");


function serialize(arr) {
    return arr.join(',');
}

function goal(s){ // check if achieved goal
    let ok = true;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== t[i]) {
            ok = false;
            break;
        }
    }

    if (ok) {
        console.log("possivel");
        process.exit(0);
    }
}
