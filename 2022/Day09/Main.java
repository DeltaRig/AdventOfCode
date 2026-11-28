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
                // H and T start at the same position, overlapping
                String[] instruction = line.split(" ");

                for (int i = 0; i < Integer.parseInt(instruction[1]); i++) {
                    move_head(head, instruction[0]);
                    move_tail(tail, head); // Adjust tail to stay close to head
                    System.out.println("tail: " + tail.toString());
                    addUnique(tail, visited);
                    // printBoard(head, tail, visited); // Print the board after each move
                }
            }
            sc.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        System.out.println("Tail visited " + visited.size() + " different points");
    }

    public static void move_head(Point h, String direction) {
        // don't available in Java 11
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
                t.y += (dy > 0) ? 1 : -1;
        }
    }

    public static boolean isEqual(Point a, Point b) {
        return a.x == b.x && a.y == b.y;
    }

    public static void addUnique(Point t, List<Point> list) {
        for (Point p : list) {
            if (isEqual(t, p)) {
                return;
            }
        }
        list.add(t.copy());
    }

    public static void printBoard(Point head, Point tail, List<Point> visited) {
        int size = 10; // Set the size of the board
        char[][] board = new char[size][size];

        // Initialize the board with dots
        for (int i = 0; i < size; i++) {
            Arrays.fill(board[i], '.');
        }

        // Mark visited points
        for (Point p : visited) {
            if (p.x >= 0 && p.x < size && p.y >= 0 && p.y < size) {
                board[size - 1 - p.y][p.x] = '#';
            }
        }

        // Mark head and tail positions
        if (head.x >= 0 && head.x < size && head.y >= 0 && head.y < size) {
            board[size - 1 - head.y][head.x] = 'H';
        }
        if (tail.x >= 0 && tail.x < size && tail.y >= 0 && tail.y < size) {
            board[size - 1 - tail.y][tail.x] = 'T';
        }

        // Print the board
        for (char[] row : board) {
            System.out.println(new String(row));
        }
        System.out.println();
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
        return new Point(x, y);
    }
}
