/**
 * https://adventofcode.com/2015/day/3
 * @author (Daniela Pereira Rigoli)
 * 
 * @version (31/07/2020)
 */

public class Day3Compare {
    private int[][] locais;

     //construtor
     public Day3Compare(){
        setLocais(new int[1][2]);
    }
    
    //getter
    public int[][] getLocals(){
        return locais;    
    }
    
    //setters
    public void setLocais(int[][] locais){
        this.locais = locais;
    }

    //boolean compara
    public boolean compare(int[] local){
        boolean result = true;
        for(int i = 0; i < locais.length; i++){
            if(locais[i][0] == local[0] && locais[i][1] == local[1]){
                result = false;
            }
        }
        return result;
    }

    //void add
    public void add(int[] local){
        int[][] novo = new int[locais.length + 1][2];
        for(int i = 0; i < locais.length; i++){
            novo[i] = locais[i];
        }
        novo[locais.length][0] = local[0];
        novo[locais.length][1] = local[1];
        locais = novo;
    }

}