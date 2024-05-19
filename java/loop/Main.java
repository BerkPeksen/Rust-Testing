public class Main {
    public static void main(String[] args) {
        long startTime = System.nanoTime();
        int count = 0;

        for (int i = 0; i < 200_000_000; i++) {
            count++;
        }
         
        
        long elapsedTime = System.nanoTime() - startTime;
        double elapsedMilliseconds = (double) elapsedTime / 1_000_000.0;
        System.out.printf("Time taken: %.3f milliseconds to count: %d%n", elapsedMilliseconds, count);
    }
}