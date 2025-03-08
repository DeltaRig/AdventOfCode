import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
/**
 * https://adventofcode.com/2022/day/2
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (August 9th 2024)
 */
public class Day2p2 {
    // part 1
    private static Map<String, String> mapOptions = new HashMap<String, String>();

    // part 2
    private static Map<String, Integer> mapPoints = new HashMap<String, Integer>();

    public static void main(String args[]){
        // part 1
        mapOptions.put("A", "X");
        mapOptions.put("B", "Y");
        mapOptions.put("C", "Z");

        // part 2
        mapPoints.put("A", 1);
        mapPoints.put("B", 2);
        mapPoints.put("C", 3);

        String path = "input.txt";
        // part 1
        int score = followGuide(path);
        // What would your total score be if everything goes exactly according to your strategy guide?
        System.out.println("What would your total score be if everything goes exactly according to your strategy guide?");
        System.out.println(score);

        //part 2
        score = followGuidep2(path);
        // what would your total score be if everything goes exactly according to your strategy guide?
        System.out.println("what would your total score be if everything goes exactly according to your strategy guide?");
        System.out.println(score);

    }
    //day 2 part 1
        /**
     *  A for Rock, 1
     *  B for Paper,2
     *  and C for Scissors 3
     *  win 6 X
     *  lose 0 Z
     *  draw 3 Y
     */
    private static int followGuide(String path){
        int result = 0;
        String[] round;

        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){    
                if(! line.isEmpty()){
                    round = line.split(" ");
                    // first sum the points to have letter 
                    if(round[1].equals("X")){
                        result+=1;
                        if(round[0].equals("C")) // win
                            result += 6; 
                    } else if(round[1].equals("Y")){
                        result+=2;
                        if(round[0].equals("A"))  // win
                            result += 6; 
                    } else {
                        result += 3;
                        if(round[0].equals("B")) // win
                            result += 6; 
                    }
                    if(mapOptions.get(round[0]).equals(round[1])) // if win draw sum 3
                        result+= 3;
                    // when lose 0 points are add
                }
            }

        } catch (IOException e) {
            System.out.println("Fail to open file");
        }
        return result;
    }

    /**
     *  A for Rock, 1
     *  B for Paper,2
     *  and C for Scissors 3
     *  win 6
     *  lose 0
     *  draw 3
     * X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
     */
    // O(n)
    // O(1) Memory
    private static int followGuidep2(String path){
        int result = 0;
        String[] round;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){ 
                if(! line.isEmpty()){
                    round = line.split(" ");
                    if(round[1].equals("Y")){
                        result+=3; // draw
                        result+= mapPoints.get(round[0]);
                    } else if(round[1].equals("Z")){ // A Z
                        result+=6; // win
                        int win = mapPoints.get(round[0]);
                        result += win + 1 > 3 ? 1 : (win +1);
                    } else {
                        // when lose 0 points are add
                        int choose = mapPoints.get(round[0]);
                        result += choose - 1 <= 0 ? 3 : (choose -1);
                    }
                }
            }

        } catch (IOException e) {
            System.out.println("Fail to open file");
        }
        return result;
    }
}