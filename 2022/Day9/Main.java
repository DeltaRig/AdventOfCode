import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * Author Daniela Rigoli
 * 11 Jan 2025
 * https://adventofcode.com/2022/day/9
 */

// head (H) and tail (T)

class Main {
    public static void main(String[] args) {
        Point head = new Point(0, 0);
        Point tail = new Point(0, 0);
        List<Point> visited = new ArrayList<Point>();
        visited.add(head.copy());

        try {
            File f = new File("input.txt");
            Scanner sc = new Scanner(f);

            System.out.println(visited.get(0));

            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                System.out.println(line);
                // H and T stat at the same position, overlapping
                String[] instruction = line.split(" ");

                for (int i = 0; i < Integer.parseInt(instruction[1]); i++) {
                    move_head(head, instruction[0]);
                    // System.out.println("head: " + head.toString());
                    move_tail(tail, head); // Adjust tail to stay close to head
                    System.out.println("tail: " + tail.toString());

                    if (notInPoints(tail, visited)) {
                        System.out.println("added " + tail.x + " , " + tail.y);
                        visited.add(tail.copy());
                    }
                }

            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        System.out.println("Tail visited " + visited.size() + " different points");
    }

    public boolean isEqual(Point a, Point b) {
        if (a.x == b.x)
            if (a.y == b.y)
                return true;
        return false;
    }

    public static void move_head(Point h, String direction) {
        Map<String, Point> directions = Map.of("U", new Point(0, 1), "D", new Point(0, -1), "L", new Point(-1, 0), "R",
                new Point(1, 0));

        h.x += directions.get(direction).x;
        h.y += directions.get(direction).y;
    }

    public static void move_tail(Point t, Point h) {
        int dx = h.x - t.x;
        int dy = h.y - t.y;
        if (Math.abs(dx) > 1 || Math.abs(dy) > 1) {
            if (dx != 0)
                t.x += (dx > 0) ? 1 : -1;
            if (dy != 0)
                t.y = (dy > 0) ? 1 : -1;
        }
    }

    public static boolean notInPoints(Point t, List<Point> list) {
        for (Point p : list) {
            if (p.x == t.x)
                if (p.y == t.y)
                    return false;

        }
        return true;
    }

}

class Point {
    public int x = 0;
    public int y = 0;

    public Point(int a, int b) {
        x = a;
        y = b;
    }

    public String toString() {
        return "x: " + x + " | y: " + y;
    }

    public Point copy() {
        return new Point(y, x);
    }
}
