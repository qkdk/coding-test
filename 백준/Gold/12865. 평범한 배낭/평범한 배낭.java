import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static class Bag {
		int weigh;
		int value;

		public Bag(int weigh, int value) {
			this.weigh = weigh;
			this.value = value;
		}

		@Override
		public String toString() {
			return "Bag [weigh=" + weigh + ", value=" + value + "]";
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		Bag[] bags = new Bag[n + 1];
		int[][] dp = new int[n + 1][k + 1];
		for (int i = 1; i < n + 1; i++) {
			st = new StringTokenizer(br.readLine());
			bags[i] = new Bag(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		}

		// i 가방번호
		// j 가능한 무게
		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < k + 1; j++) {
				Bag curBag = bags[i];
				if (curBag.weigh > j) {
					dp[i][j] = dp[i - 1][j];
					continue;
				}
				dp[i][j] = Math.max(dp[i - 1][j - curBag.weigh] + curBag.value, dp[i - 1][j]);
			}
		}
		System.out.println(dp[n][k]);
//		print(n, k, dp);
	}

	private static void print(int n, int k, int[][] dp) {
		for (int i = 1; i < n+ 1;i ++) {
			for (int j = 1; j < k + 1; j++) {
				System.out.print(dp[i][j] + "\t");
			}
			System.out.println();
		}
		System.out.println();
	}
}
