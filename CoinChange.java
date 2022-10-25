import java.util.Arrays;

public class CoinChange {

	/*
	 * You are given coins of different denominations and a total amount of money.
	 * Write a function to compute the number of combinations that make up that amount.
	 * 
	 */
	
	//public static int[] coins = {1,2,3};
	//public static int amount = 4;
	
	public static void main(String[] args) {
        int[] coins = {1,2,3};
        int amount = 4;
		System.out.println(combo(amount,0,coins));
        String []coins_str="3 25 34 38 26 42 16 10 15 50 39 44 36 29 22 43 20 27 9 30 47 13 40 33".split(" ");
        //Predicate<Integer> even = x -> x % 2 == 0;
        int[] coins2 = Arrays.stream(coins_str).mapToInt(Integer::parseInt).toArray(); 

        System.out.println("case 2: ");
        System.out.println(combo(222,0,coins2));

	}
	
	public static int combo(int amount, int currentCoin,int[] coins){
		
		if( amount == 0)
			return 1;
		
		if( amount < 0)
			return 0;
		
		int nCombos = 0;
		for( int coin = currentCoin; coin < coins.length; coin++){
			nCombos += combo(amount - coins[coin],coin,coins);
		}
		
		return nCombos;
	}
}