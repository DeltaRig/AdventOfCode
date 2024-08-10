import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
/**
 * https://adventofcode.com/2022/day/2
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (08/08/2024)
 */
public class Day2 {

    private static Map<String, String> mapOptions = new HashMap<String, String>();


    public static void main(String args[]){
        mapOptions.put("A", "X");
        mapOptions.put("B", "Y");
        mapOptions.put("C", "Z");
        // part 1
        int score = followGuide("input.txt");
        // What would your total score be if everything goes exactly according to your strategy guide?
        System.out.println("What would your total score be if everything goes exactly according to your strategy guide?");
        System.out.println(score);

    }
    //day 2 part 1
        /**
     *  A X for Rock, 1
     *  B Y for Paper,2
     *  and C Z for Scissors 3
     *  win 6
     *  lose 0
     *  draw 3
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
}