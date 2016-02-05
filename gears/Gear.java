
// A solution to the Gears problem from 
// the 2015 ACM-ICPC Southeast USA Programming Contest Division 1

import java.util.ArrayList;
import java.util.Scanner;
import java.util.ArrayDeque;
import java.util.Queue;
import java.lang.String;
import java.lang.Integer;
import java.lang.Math;

class Gear {

    public int x;
    public int y;
    public int r;
    public int rotation;
    public ArrayList<Gear> adjacent;
    public boolean last;
    public boolean visited;

    Gear(int x, int y, int r) {
        this.x = x;
        this.y = y;
        this.r = r;
        this.rotation = 0; // 1 = clockwise
        this.adjacent = new ArrayList<Gear>();
        this.last = false; // not target gear
        this.visited = false;
    }

    public String toString() {
        return Integer.toString(this.x) + " " + Integer.toString(this.y) + " " + Integer.toString(this.r);
    }

    private static boolean adjacent(Gear gear1, Gear gear2) {
        double sum_of_radii_squared = Math.pow(gear1.r + gear2.r, 2);
        double distance_squared = Math.pow(gear2.x - gear1.x, 2) + Math.pow(gear2.y - gear1.y, 2);
        return sum_of_radii_squared == distance_squared;
    }
    
    private static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // read gear info from stdin
        Gear[] gears = new Gear[n];
        for (int i = 0; i < n; ++i) {
            gears[i] = new Gear(sc.nextInt(), sc.nextInt(), sc.nextInt());
        }
        // update gears' adjacency lists
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j && adjacent(gears[i], gears[j])) {
                    gears[i].adjacent.add(gears[j]);
                }
            }
        }
        // mark the last gear
        gears[n-1].last = true;
        // arbitrarily set the rotation of the source gear
        gears[0].rotation = 1;
        // traverse the graph of gears breadth-first to determine movement
        Queue<Gear> q = new ArrayDeque<Gear>();
        q.add(gears[0]);
        while (!q.isEmpty()) {
            Gear g = q.remove();
            g.visited = true;
            if (g.last) {
                int gcd = gcd(g.r, gears[0].r);
                int a = g.r / gcd;
                int b = gears[0].r / gcd;
                if (gears[0].rotation != g.rotation) b *= -1;
                // print the ratio of source gear revolutions to target gear revolutions
                System.out.println(a + " " + b); 
                return;
            }
            for (int i = 0; i < g.adjacent.size(); ++i) {
                Gear adj = g.adjacent.get(i);
                if (!adj.visited) {
                    if (adj.rotation == 0) {
                        adj.rotation = -1 * g.rotation;
                        q.add(adj);
                    } else if (g.rotation == adj.rotation) {
                        System.out.println("-1"); // no movement
                        return;
                    }
                }
            }
        }
        System.out.println("0"); // no path to target
    }
}
