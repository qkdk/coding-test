import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	private static int answer = 2;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int n = Integer.parseInt(br.readLine());
		int[][] table = new int[n][n];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				table[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		solve(0, table);
		System.out.println(answer);
	}

	private static void solve(int index, int[][] table) {
		if (index == 5) {
			// 체크
			int maxValue = Integer.MIN_VALUE;
			for (int i = 0; i < table.length; i++) {
				for (int j = 0; j < table.length; j++) {
					maxValue = Math.max(maxValue, table[i][j]);
				}
			}
			answer = Math.max(answer, maxValue);
			return;
		}

		solve(index + 1, moveUp(table));
		solve(index + 1, moveDown(table));
		solve(index + 1, moveRight(table));
		solve(index + 1, moveLeft(table));
	}

	private static void makeLine(Deque<Integer> q, List<Integer> lst) {
		for (int j = 0; j < lst.size(); j++) {
			try {
				if (lst.get(j).equals(lst.get(j + 1))) {
					j++;
					q.add(lst.get(j) * 2);
				} else {
					q.add(lst.get(j));
				}
			} catch (IndexOutOfBoundsException e) {
				// TODO: handle exception
				q.add(lst.get(j));
			}
		}
	}

	private static int[][] moveRight(int[][] table) {
		int[][] resultTable = new int[table.length][table.length];

		int sIndex = table.length - 1;
		for (int i = 0; i < table.length; i++) {
			Deque<Integer> q = new ArrayDeque<>();
			List<Integer> lst = new ArrayList<>();
			for (int j = 0; j < table.length; j++) {
				if (table[i][sIndex - j] == 0) {
					continue;
				}
				lst.add(table[i][sIndex - j]);
			}
			makeLine(q, lst);
			int index = sIndex;
			while (!q.isEmpty()) {
				Integer value = q.poll();
				resultTable[i][index--] = value;
			}
		}
		return resultTable;
	}

	private static int[][] moveLeft(int[][] table) {
		int[][] resultTable = new int[table.length][table.length];

		int sIndex = 0;
		for (int i = 0; i < table.length; i++) {
			Deque<Integer> q = new ArrayDeque<>();
			List<Integer> lst = new ArrayList<>();
			for (int j = 0; j < table.length; j++) {
				if (table[i][j] == 0) {
					continue;
				}
				lst.add(table[i][j]);
			}
			makeLine(q, lst);
			int index = sIndex;
			while (!q.isEmpty()) {
				Integer value = q.poll();
				resultTable[i][index++] = value;
			}
		}
		return resultTable;
	}

	private static int[][] moveUp(int[][] table) {
		int[][] resultTable = new int[table.length][table.length];

		int sIndex = 0;
		for (int i = 0; i < table.length; i++) {
			Deque<Integer> q = new ArrayDeque<>();
			List<Integer> lst = new ArrayList<>();
			for (int j = 0; j < table.length; j++) {
				if (table[j][i] == 0) {
					continue;
				}
				lst.add(table[j][i]);
			}

			makeLine(q, lst);
			int index = sIndex;
			while (!q.isEmpty()) {
				Integer value = q.poll();
				resultTable[index++][i] = value;
			}
		}
		return resultTable;
	}

	private static int[][] moveDown(int[][] table) {
		int[][] resultTable = new int[table.length][table.length];

		int sIndex = table.length - 1;
		for (int i = 0; i < table.length; i++) {
			Deque<Integer> q = new ArrayDeque<>();
			List<Integer> lst = new ArrayList<>();
			for (int j = 0; j < table.length; j++) {
				if (table[sIndex - j][i] == 0) {
					continue;
				}
				lst.add(table[sIndex - j][i]);
			}
			makeLine(q, lst);
			int index = sIndex;
			while (!q.isEmpty()) {
				Integer value = q.poll();
				resultTable[index--][i] = value;
			}
		}
		return resultTable;
	}
}