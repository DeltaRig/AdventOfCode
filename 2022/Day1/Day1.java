import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * https://adventofcode.com/2022/day/1
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (31/07/2024)
 */

public class Day1 {
    public static void main(String args[]){

        String path = "input.txt";
        int[] part1 = calorieCounting(path);
        int part2 = 0;

        System.out.println("About the Elf carrying the most Calories. How many total Calories is that Elf carrying?");
        System.out.println(part1[0]);

        System.out.println("Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?");
        for(int i = 0; i < part1.length; i++){
            part2+=part1[i];
            System.out.println(part1[i]);
        }
        System.out.println(part2);

    }

    public static int[] calorieCounting(String file){
        int[] result = new int[]{0,0,0};
        int cur = 0;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(file));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){    
                if(! line.isEmpty()){
                    cur += Integer.parseInt(line);
                } else {
                    // update the value of the elf with more calories
                    ranker(result, cur, 0);
                    cur = 0;
                }
                
            }

        } catch (IOException e) {
            System.out.println("Fail to open file");
        }
        
        return result;
    }
    private static void ranker(int[] ranking, int value, int index){
        int temp;
        int temp2;
        while(index < ranking.length){ // 3
            if(value > ranking[index]){
                temp = ranking[index];
                ranking[index] = value;
                for(int i = index+1; i < ranking.length; i++){ // 3
                    temp2 = ranking[i];
                    ranking[i] = temp;
                    temp = temp2;
                }
                return;
            }
            index++;
        }  
    }
}