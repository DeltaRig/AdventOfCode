/**
 * https://adventofcode.com/2015/day/6
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (01/08/2020)
 */
import java.io.*;

public class Day6 {
    
    public static void main(String args[]){
        boolean[][] lights = new boolean[1000][1000];
        int iStart, iEnd, jStart, jEnd;
        

        String path = "input6.txt"; //write the path for the txt with input
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){    
                String[] words = line.split("\\s+|,+");

                System.out.println(words.length);

                if(words.length == 6){
                    //toggle
                    iStart = Integer.parseInt(words[1]);
                    jStart = Integer.parseInt(words[2]);
                    iEnd = Integer.parseInt(words[4]);
                    jEnd = Integer.parseInt(words[5]);

                    lights = toggle(lights, iStart, iEnd, jStart, jEnd);
                    //toggle iStart,iEnd through jStart,jStart
                } else {
                    iStart = Integer.parseInt(words[2]);
                    jStart = Integer.parseInt(words[3]);
                    iEnd = Integer.parseInt(words[5]);
                    jEnd = Integer.parseInt(words[6]);
                    //turn on iStart,iEnd through jStart,jStart

                    if(words[1].equals("on")){
                        //turn on
                        lights = on(lights, iStart, iEnd, jStart, jEnd);

                    }else{
                        //turn off
                        lights = off(lights, iStart, iEnd, jStart, jEnd);
                    
                    }
                }
            }

        } catch (IOException e) {
            System.out.println("Não deu");
        }
        
        System.out.println("how many lights are lit? " + count(lights));
    }



    public static int count(boolean[][] lights){ //count how many lights are lit
        int count = 0;
        for(int i = 0; i < lights.length; i++){
            for(int j = 0; j < lights[0].length; j++){
                if(lights[i][j]){
                    count++;
                }
            }
        }
        return count;
    }

    public static boolean[][] on(boolean[][] lights, int iStart, int iEnd, int jStart, int jEnd){ //turn on the lights
        for(int i = iStart; i <= iEnd; i++){
            for(int j = jStart; j <= jEnd; j++){
                lights[i][j] = true;
            }
        }
        return lights;
    }

    public static boolean[][] off(boolean[][] lights, int iStart, int iEnd, int jStart, int jEnd){ //turn off the lights
        for(int i = iStart; i <= iEnd; i++){
            for(int j = jStart; j <= jEnd; j++){
                lights[i][j] = false;
            }
        }
        return lights;
    }

    public static boolean[][] toggle(boolean[][] lights, int iStart, int iEnd, int jStart, int jEnd){ //toggle the lights
        for(int i = iStart; i <= iEnd; i++){
            for(int j = jStart; j <= jEnd; j++){
                if(lights[i][j]){
                    lights[i][j] = false;
                } else {
                    lights[i][j] = true;
                }
            }
        }
        return lights;
    }

}