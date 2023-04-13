# 자바로 DFS 풀어보기
``` java
import java.util.Scanner;
import java.io.BufferedReader;
// import java.io.BufferedWriter;
import java.io.InputStreamReader;
// import java.io.OutputStreamWriter;

class Main
{
  public static int[][] arr;
	public static int M; // 변
	public static boolean dfs(int i, int j) {

		if (i < 0 || i >= M || j < 0 || j >= M ) {
			return false;  // 범위를 벗어날 경우
		}

    int max = arr[0][0];
    int min = arr[0][0];
    
    if (arr[i][j]> max){
      max = arr[i][j];
    }
    if (arr[i][j] <min){
      min = arr[i][j];
    }

    int num = (max+min)/2;
    
		if (arr[i][j] > num) {
			arr[i][j] = 1;//  방문처리
			
            
            //상하좌우 방문
			dfs(i + 1, j);
			dfs(i - 1, j);
			dfs(i, j + 1);
			dfs(i, j - 1);
		    
			return true;
		}

		return false;
	}
	public static void main(String args[]) throws Exception
	{

		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
		    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    		// BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    		int answer=0;
    		
    		M = Integer.parseInt(br.readLine());
    		
    		arr = new int[M][M];
    
    		for (int i = 0; i < M; i++) {
    			String[] text = br.readLine().split(" ");
    			for (int j = 0; j < M; j++) {
    				arr[i][j] = Integer.parseInt(text[j]);
    			}
    		}
    		
    		for (int i = 0; i < M; i++) {
    			for (int j = 0; j < M; j++) {
    				if(dfs(i,j)) {answer++;}
    			}
    		}
    		
    		String str = String.format("#%d %d", test_case, answer);
          System.out.println(str);
		}
     sc.close();
	}
}
```
