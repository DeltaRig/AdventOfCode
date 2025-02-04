import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * Author Daniela Rigoli
 * 21 Jan 2025
 * https://adventofcode.com/2022/day/9
 * Java 11
 * Part 2
 */

// head (H) and tail (T)

class Point {
    public int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public Point copy() {
        return new Point(x, y);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Point point = (Point) obj;
        return x == point.x && y == point.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}

public class Main2 {
    public static void main(String[] args) {
        List<Point> rope = new ArrayList<>();
        // because we check all 10 positions
        for (int i = 0; i < 10; i++) {
            rope.add(new Point(0, 0));
        }
        // and we need to know which positions number 9 visited
        Set<Point> visited = new HashSet<>();
        visited.add(rope.get(9).copy());

        try {
            File file = new File("input.txt");
            Scanner sc = new Scanner(file);
            
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                String[] instruction = line.split(" ");
                
                for (int i = 0; i < Integer.parseInt(instruction[1]); i++) {
                    move_head(rope.get(0), instruction[0]);
                    
                    for (int j = 1; j < rope.size(); j++) {
                        move_tail(rope.get(j), rope.get(j - 1));
                    }
                    
                    visited.add(rope.get(9).copy());
                }
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        System.out.println("Tail visited " + visited.size() + " different points");
    }

    public static void move_head(Point head, String direction) {
        switch (direction) {
            case "U": head.y += 1; break;
            case "D": head.y -= 1; break;
            case "L": head.x -= 1; break;
            case "R": head.x += 1; break;
        }
    }

    public static void move_tail(Point t, Point h) {
        int dx = h.x - t.x;
        int dy = h.y - t.y;
        if (Math.abs(dx) > 1 || Math.abs(dy) > 1) {
            if (dx != 0)
                t.x += (dx > 0) ? 1 : -1;
            if (dy != 0)
                t.y += (dy > 0) ? 1 : -1;
        }
    }
}

