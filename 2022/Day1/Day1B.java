import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/**
 * https://adventofcode.com/2022/day/1
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (31/07/2024)
 */


public class Day1B {
    public static void main(String args[]){

        String path = "input.txt";
        ArrayList<Integer> elfs = calorieCounting(path);
        elfs.sort(Collections.reverseOrder());
        int part1 = elfs.get(0);
        int part2 = elfs.get(0) + elfs.get(1) + elfs.get(2);

        System.out.println("About the Elf carrying the most Calories. How many total Calories is that Elf carrying?");
        System.out.println(part1);

        System.out.println("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?");
        System.out.println(part2);

    }

    public static ArrayList<Integer> calorieCounting(String file){
        ArrayList<Integer> elfs = new ArrayList<Integer>(); 
        int cur = 0;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){  
                if(! line.isEmpty()){
                    cur += Integer.parseInt(line);
                } else {
                    elfs.add(cur);
                    cur=0;
                }
            }
        } catch (IOException e) {
            System.out.println("Fail to open file");
        }
        return elfs;
    }
}