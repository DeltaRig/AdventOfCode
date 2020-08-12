/**
 * https://adventofcode.com/2015/day/3
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (01/08/2020)
 */
import java.io.*;

public class Day3part2 {
    public static void main(String args[]){
        int[] localSanta = new int[2]; //x, y for Santa
        int[] localRobo = new int[2]; //x, y for Santa-Robo
        boolean newLocal; // is the firt time in this house?
        int houses = 1; // cont how many house Santa visit 

        Day3Compare compare;
        compare = new Day3Compare();

        String path = "/input3.txt"; //write the path for the txt with input
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){    
                if(line.length() > 0){
                    for(int i = 0; i < line.length(); i++){
                        if(i % 2 == 0){
                            if(line.charAt(i) == '^'){ //north
                                localRobo[0] += 1;
                            } else if(line.charAt(i) == 'v'){ //south
                                localRobo[0] -= 1;
                            }  else if(line.charAt(i) == '>'){ //east
                                localRobo[1] += 1;
                            } else { //lest
                                localRobo[1] -= 1;
                            }

                            newLocal = action(localRobo, compare);
                        } else {
                            if(line.charAt(i) == '^'){ //north
                                localSanta[0] += 1;
                            } else if(line.charAt(i) == 'v'){ //south
                                localSanta[0] -= 1;
                            }  else if(line.charAt(i) == '>'){ //east
                                localSanta[1] += 1;
                            } else { //lest
                                localSanta[1] -= 1;
                            }

                            newLocal = action(localSanta, compare);
                        }

                        if(newLocal){
                            houses++;
                        }

                    }
                }
            }
            
            System.out.println("Houses: " + houses);
        } catch (IOException e) {
            System.out.println("Não deu");
        }
    }
    
    public static boolean action(int[] local, Day3Compare compare){
        boolean newLocal = compare.compare(local);
        if(newLocal){
            compare.add(local);
        }
        return newLocal;
    }
    

}