# Daniela Rigoli September 05 2024

def read_stacks_and_moves(file_name):
    stacks = []
    moves = []
    
    with open(file_name, 'r') as f:
        stack_lines = []
        
        for line in f:
            # Se a linha for um comando de movimento, armazenamos em 'moves'
            if line.startswith("move"):
                moves.append(line.strip())
            # Se a linha contiver números (representando os índices das pilhas), terminamos a leitura das pilhas
            elif line.strip() and line.strip()[0].isdigit():
                # Inicializar as pilhas (com base na quantidade de números lidos)
                stack_count = len(line.split())
                stacks = [[] for _ in range(stack_count)]
            # Caso contrário, armazenamos as linhas das pilhas
            elif "[" in line:
                stack_lines.append(line)

        for stack_line in reversed(stack_lines):
            # Processar a linha das pilhas
            for i in range(0, len(stack_line), 4):
                crate = stack_line[i+1]  # A caixa está no índice 1 da substring
                if crate != ' ':
                    # Calcular em qual pilha a caixa deve ser colocada
                    stack_index = i // 4
                    stacks[stack_index].append(crate)

    return stacks, moves


def process_moves(stacks, moves):
    for move in moves:
        parts = move.split()
        num_crates = int(parts[1])
        from_stack = int(parts[3]) - 1
        to_stack = int(parts[5]) - 1

        for _ in range(num_crates):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)

    # Obter o topo de cada pilha
    result = ''.join([stack[-1] for stack in stacks if stack])
    return result

file_name = 'input.txt'
stacks, moves = read_stacks_and_moves(file_name)
result = process_moves(stacks, moves)
print("Caixas no topo das pilhas:", result)
