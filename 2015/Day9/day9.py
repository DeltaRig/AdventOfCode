#
# Daniela Rigoli
# 14/07/2021
# Python 3.9.5
#

# E são as arestas
# V são os vertices
def readG( name ) : 
  nodos = set()
  arestas = {}

  with open(name, 'r') as fp :
    for lin in fp :
      lin = lin.rstrip()
      words = lin.split()
      nodos.add( words[0] )
      nodos.add( words[2] )
      arestas[ ( words[0], words[2] ) ] = int(words[4])
      arestas[ ( words[2], words[0] ) ] = int(words[4])

  return nodos, arestas

V, E = readG( "entrada.txt" )

# print(V, "\n\n", E)

##########################################
def caminha( u, V, E, JaConheco ) :

  print("Estou em", u );
  JaConheco[u] = 1;

  for v in V :
    if ( u, v ) in E and not v in JaConheco :
      caminha( v, V, E, JaConheco )

#caminha("C71", V, E, {} )

##########################################
def numcomponentes( V, E ) :

  Comp = 0;
  Visitou = {}
  for u in V :
    if not u in Visitou :
      Comp += 1
      caminha( u, V, E, Visitou )
  return Comp

#print( "Componentes:", numcomponentes( V, E ) )

##########################################
def temcaminho( u, v, V, E, JaConheco ) :

  if u == v : return 1

  JaConheco[u] = 1;

  for w in V :
    if ( u, w ) in E and not w in JaConheco :
      if temcaminho( w, v, V, E, JaConheco ) == 1 : return 1

  return 0

# print( temcaminho("A4", "Q47", V, E, {} ) )
# print( temcaminho("G69", "O66", V, E, {} ) )

##########################################
def pontes( V, E ) :

    for (u, v) in E.copy() :
        if u > v : continue
        old = E[( u, v ) ]
        E.pop( ( u, v ) )
        res = temcaminho(u, v, V, E, {})
        if res == 0 :
            print( u, '--', v, "é ponte")
        E[ ( u, v ) ] = old
        
#pontes( V, E )

##########################################
def temciclo(u, V, E, Cor) :

  Cor[u] = "Amarelo"

  for v in V :
    if ( u, v ) in E :
      if v in Cor and Cor[v] == "Vermelho" : continue
      if v in Cor and Cor[v] == "Amarelo" : return 1
      if temciclo( v, V, E, Cor ) : return 1

  Cor[u] = "Vermelho"

  return 0

def temciclomaster( V, E ) :

  TemEntrada = {}
  for ( u, v ) in E :
    TemEntrada[v] = 1

  I = "Inicio"

  V.add(I);
  for v in V :
    if not v in TemEntrada :
      E[ ( I, v ) ] = 1

  res = temciclo( I, V, E, {} );

  V.remove(I);
  for v in V :
    if not v in TemEntrada :
      E.pop( ( I, v ) )

  return res

#print( temciclomaster( V, E ) )
##########################################
def achaordem(node, V, E) :
    faltaProcessar = {}
    caminha( node, V, E, faltaProcessar )
    print(faltaProcessar)

    #{'C28', 'D15', 'F21', 'P62', 'A79', 'U27', 'J46', 'A6', 'G50'}
    #[ a, c, b, f, g, t, h, j, x ]

    while ( len( faltaProcessar ) > 0 ) :
      for u in faltaProcessar:   #<==== Sera que é esse?
        print(u)
        podeser = 1
        for v in faltaProcessar :  #<=== Alguem dependendo de processamento chega nele?
          if ( v, u ) in E :     # Se sim, nao podemos o processar
            podeser = 0
            break
        if podeser == 1 : # Se ninguem que depende de processamento leva a u, entao processa u
            print("Processa ", u)
            faltaProcessar.pop( u )
            break

#achaordem( "E5", V, E )
######################################

import math

def prim( u, V, E ) :

    Bool = {}
    Bool[u] = True
    dist = 0

    while ( True ) :

      menorE = math.inf
      bestA = 0
      bestB = 0
      
      for a in Bool :
        for b in V :
          if ( a, b ) in E and not b in Bool :
            if E[(a,b)] < menorE :
              menorE = E[(a,b)]
              bestA = a
              bestB = b
      if bestB == 0 : break
      Bool[bestB] = True
      dist = dist + menorE
      print(bestA, "--", bestB, '[label="', menorE, '", color="red"]')

    return dist

#######################

def dijkstra( u, V, E ) :

    dist = {}
    prev = {}
    
    for v in V:
        dist[v] = math.inf
        prev[v] = ""

    dist[u] = 0

    Q = V.copy()

    ArestasOrig = {}
    ArestasDijkstra = {}

    while len(Q) != 0:
        u = retiraMin( Q, dist )
        for ( u, v ) in E:
            aux = dist[u] + E[(u, v)]
            if aux < dist[v] :
                dist[v] = aux
                prev[v] = u

   
    for v in V :
        if prev[v] != "" :
          ArestasDijkstra[ (prev[v], v) ] = 1

    for (u, v) in E :
        if not ( u, v ) in ArestasDijkstra :
          ArestasOrig[ (u,v) ] = 1

    print("strict graph G {")
    
    dist = 0
    for u in V :
        for v in V :
            #if ( u, v ) in ArestasOrig :
                #print(u, "--", v, "[label=\"", E[(u,v)],"\"]")
            if ( u, v ) in ArestasDijkstra :
                print(u, "--", v, "[color=\"red\",label=\"", E[(u,v)],"\"]")
                dist += E[(u,v)]

    print("}")

    return dist
    


def retiraMin(Q, dist) :
  menorDist = math.inf
  result = ""
  for q in Q :
    if dist[q] < menorDist :
      result = q
      menorDist = dist[q]
  Q.remove(result)
  return result



distanciaTotal = prim( "Tristram", V, E )
print(distanciaTotal)


