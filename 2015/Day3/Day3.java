/**
 * https://adventofcode.com/2015/day/3
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (31/07/2020)
 */
import java.io.*;

public class Day3 {
    public static void main(String args[]){
        int[] local = new int[2]; //x, y
        local[0] = 0; local[1] = 0; // start in (0,0)
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
                        if(line.charAt(i) == '^'){ //north
                            local[0] += 1;
                        } else if(line.charAt(i) == 'v'){ //south
                            local[0] -= 1;
                        }  else if(line.charAt(i) == '>'){ //east
                            local[1] += 1;
                        } else { //lest
                            local[1] -= 1;
                        }
                        
                        newLocal = compare.compare(local);
                        if(newLocal){
                            houses++;
                            compare.add(local);
                        }

                    }
                }
            }
            
            System.out.println("Houses: " + houses);
        } catch (IOException e) {
            System.out.println("Não deu");
        }
    }
    

}