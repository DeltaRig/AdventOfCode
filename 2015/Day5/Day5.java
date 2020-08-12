/**
 * https://adventofcode.com/2015/day/5
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (01/08/2020)
 */
import java.io.*;

public class Day5 {
    public static void main(String args[]){
        int nice = 0, twice, vowels; //answer part 1
        String compare;
        boolean check;
        

        String path = "/input5.txt"; //write the path for the txt with input
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){    
                check = true; //for each line
                twice = 0;
                for(int i = 0; i < line.length() - 1; i++){ // check does not contain the strings ab, cd, pq, or xy
                    compare = line.substring(i,i+2);
                    if(compare.equals("ab") || compare.equals("cd") || compare.equals("pq") || compare.equals("xy")){
                        check = false;
                    }

                    if(line.charAt(i) == line.charAt(i+2)){ // check if the string contains at least one letter that appears twice in a row
                        twice++;
                    }
                }
                if(twice < 1){
                    check = false;
                }

                //check if the string contains at least three vowels
                vowels = vowels(line);
                if(vowels < 3){
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

    public static int vowels(String word){
        int total = 0;
        for(int count = 0; count < word.length(); count++)
        {
            char letter = word.charAt(count);
            if(letter == 'a' || letter == 'e' || letter =='i' || letter == 'o' || letter=='u'){
                total++;
            } 
        }
        return total;
    }
}