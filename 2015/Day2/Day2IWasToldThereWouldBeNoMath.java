/**
 * https://adventofcode.com/2015/day/2
 * 
 * @author (Daniela Pereira Rigoli)
 * @version (30/07/2020)
 */

import java.io.*;

public class Day2IWasToldThereWouldBeNoMath {
    public static void main(String[] args) {
        String[] values;
        values = new String[3];
        int l, w, h; //length l, width w, and height h
        int area1, area2, area3, areaSmall, areaTotal = 0; //part 1
        int answer1 = 0;  //part 1
        int ladoS1, ladoS2, ribbon = 0;  //part 2
        int answer2 = 0;  //part 2

        String path = "/presents2.txt"; //write the path for the txt with input
        try {
            BufferedReader reader = new BufferedReader(new FileReader(path));
            for (String line = reader.readLine(); line != null; line = reader.readLine()){
                if(line.length() > 0){
                    values = line.split("x");

                    l = tryParseInt(values[0]);
                    w = tryParseInt(values[1]);
                    h = tryParseInt(values[2]);

                    area1 = l * w;
                    area2 = w * h;
                    area3 = h * l;

                    if(area1 < area2){
                        if(area1 < area3){
                            areaSmall = area1;
                            ladoS1 = l;
                            ladoS2 = w;
                        } else {
                            areaSmall = area3;
                            ladoS1 = l;
                            ladoS2 = h;
                        }
                    } else {
                        if(area3 < area2){
                            areaSmall = area3;
                            ladoS1 = l;
                            ladoS2 = h;
                        } else {
                            areaSmall = area2;
                            ladoS1 = h;
                            ladoS2 = w;
                        }
                    }

                    areaTotal = (area1 * 2) + (area2 * 2) + (area3 * 2) + areaSmall; //for paper
                    ribbon = (2 * ladoS1) + (2 * ladoS2) + (l * w * h);

                }
                answer1 += areaTotal;
                answer2 += ribbon;

            }
        } catch (IOException e) {
            System.out.println("Não deu");
        }
        
        System.out.println("Answer for part 1 (paper): " + answer1);
        System.out.println("Answer for part 2 (ribbon): " + answer2);
    }


    public static int tryParseInt(String someText) {
        try {
        return Integer.parseInt(someText);
        } catch (NumberFormatException ex) {
        return 0;
        }
    }
}