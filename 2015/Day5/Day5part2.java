/**
 * https://adventofcode.com/2015/day/5
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (01/08/2020)
 */
import java.io.*;

public class Day5part2 {
    public static void main(String args[]){
        int nice = 0, repeat, twice; //answer part 2
        String compare;
        boolean check;
        

        String path = "input5.txt"; //write the path for the txt with input
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){    
                check = true; //for each line
                // check if contains a pair of any two letters that appears at least twice in the string without overlapping
                repeat = 0;
                for(int i = 0; i < line.length() - 2; i++){ 
                    if(line.charAt(i) == line.charAt(i+2)){ 
                        repeat++;
                    }
                }

                if(repeat < 1){
                    check = false;
                }

                // check if contains at least one letter which repeats with exactly one letter between them
                twice = 0;
                for(int i = 0; i < line.length() - 1; i++){ 
                    compare = line.substring(i,i+2);
                    for(int j = 0; j < line.length() - 1; j++){
                        if(Math.abs(i - j) > 1){
                            if(compare.equals(line.substring(j,j+2))){
                                twice++;
                            }
                        }
                        
                    }
                }

                if(twice < 1){
                    check = false;
                }

                if(check){
                    nice++;
                }
            }

        } catch (IOException e) {
            System.out.println("Não deu");
        }
        
        System.out.println("How many strings are nice?" +
            "\nAre " + nice + " strings nice");

    }

}