import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static class Schedule implements Comparable<Schedule> {

        int id, startTime, endTime;

        Schedule(int id, int startTime, int endTime) {
            this.id = id;
            this.startTime = startTime;
            this.endTime = endTime;
        }

        public int compareTo(Schedule o) {
            return this.startTime - o.startTime;
        }

        @Override
        public String toString() {
            return "Schedule{" +
                "id=" + id +
                ", startTime=" + startTime +
                ", endTime=" + endTime +
                '}';
        }
    }

    static class Schedule2 implements Comparable<Schedule2> {

        int id, startTime, endTime;

        Schedule2(int id, int startTime, int endTime) {
            this.id = id;
            this.startTime = startTime;
            this.endTime = endTime;
        }

        public int compareTo(Schedule2 o) {
            return this.endTime - o.endTime;
        }

        @Override
        public String toString() {
            return "Schedule{" +
                "id=" + id +
                ", startTime=" + startTime +
                ", endTime=" + endTime +
                '}';
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        Schedule[] arr = new Schedule[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            int startTime = Integer.parseInt(st.nextToken());
            int endTime = Integer.parseInt(st.nextToken());

            arr[i] = new Schedule(id, startTime, endTime);
        }

        Arrays.sort(arr);

        int count = 1;
        PriorityQueue<Schedule2> pq = new PriorityQueue<>();
        pq.add(new Schedule2(arr[0].id, arr[0].startTime, arr[0].endTime));

        for (int i = 1; i < n; i++) {
            Schedule cur = arr[i];
//            System.out.println(pq.peek());
//            System.out.println(cur);
            Schedule2 poll = pq.poll();

            pq.add(new Schedule2(arr[i].id, arr[i].startTime, arr[i].endTime));

            if (cur.startTime < poll.endTime) {
                pq.add(poll);
                count = Math.max(count, pq.size());
            }

        }

        System.out.println(count);

    }

}