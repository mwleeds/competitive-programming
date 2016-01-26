// solution to Exercise 1.2.3 problem #3 from "Competitive Programming 3"

import java.util.Scanner;
import java.util.Date;
import java.util.GregorianCalendar;
import java.lang.String;
import java.text.SimpleDateFormat;
import java.text.ParseException;

class Ex1_2_3_3 {
    public static void main(String[] args) throws ParseException {
        Scanner sc = new Scanner(System.in);
        String dateString = sc.nextLine();
        SimpleDateFormat inDateFormat = new SimpleDateFormat("dd MMMM yyyy");
        Date date = new Date();
        try {
            date = inDateFormat.parse(dateString);
        } catch (ParseException p) {
            System.err.println("Caught ParseException: " + p.getMessage());
            return;
        }
        SimpleDateFormat outDateFormat = new SimpleDateFormat("EEEE");
        String dayOfWeek = outDateFormat.format(date);
        System.out.println(dayOfWeek);
    }
}
