
/**
 * https://adventofcode.com/2015/day/4
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (01/08/2020)
 */
import java.math.BigInteger;
import java.security.*;

public class Day4 {
    public static void main(String args[]){
        boolean check = false;
        int cont = 0;
        String input = "bgvyzdsv";
        String test = "";

        do{
            test = MD5(input + cont);
            System.out.println(test);
            for(int i = 0; i < 5; i++){ // part 1 
                if(test.charAt(i) != '0'){
                    check = false;
                    break;
                }
                check = true;
            }
            cont++;
        }while(check == false);

        cont -= 1;
        int answer1 = cont;
        check = false;
        
        do{
            test = MD5(input + cont);
            System.out.println(test);
            for(int i = 0; i < 6; i++){ // part 2
                if(test.charAt(i) != '0'){
                    check = false;
                    break;
                }
                check = true;
            }
            cont++;
        }while(check == false);
        System.out.println("start with at least five zeroes in MD5: " + answer1);
        System.out.println("start with at least six zeroes in MD5: " + (cont - 1));

    }

    public static String MD5(String md5) {
        try {
             java.security.MessageDigest md = java.security.MessageDigest.getInstance("MD5");
             byte[] array = md.digest(md5.getBytes());
             StringBuffer sb = new StringBuffer();
             for (int i = 0; i < array.length; ++i) {
               sb.append(Integer.toHexString((array[i] & 0xFF) | 0x100).substring(1,3));
            }
             return sb.toString();
         } catch (java.security.NoSuchAlgorithmException e) {
         }
         return null;
    }
}